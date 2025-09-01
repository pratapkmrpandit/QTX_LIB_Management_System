import argparse
import json
import logging
from .database import Base, get_engine, get_session
from .api_client import OpenApiClient
from .schema import AuthorSchema, BookSchema
from .model import Author,Book
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Fetch books from OpenLibrary")
    parser.add_argument("--author", required=True, help="Author name to search")                     #get the author name
    parser.add_argument("--limit", type=int, default=10, help="Number of books to fetch")            #number of books to fetch
    parser.add_argument("--db", required=True, help="Database connection string")                    #database connection string
    parser.add_argument("--output", required=True, help="Output file name")                          #output file name
    parser.add_argument("--log", default="INFO", help="Log level (DEBUG, INFO, WARNING, ERROR)")
    args = parser.parse_args()

    logging.basicConfig(level=args.log.upper(), format="%(asctime)s : %(levelname)s : %(message)s")
    logging.info("Starting API data fetching process")

    engine = get_engine(args.db)                          # create_engine by callig get_engine function
    Base.metadata.create_all(engine)
    session = get_session(engine)

    try:
        client = OpenApiClient()
        author_data = client.author_search(args.author)

        if not author_data:
            logging.error("Author not found")
            return

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump({"author": author_data}, f, indent=4)

        first_name = args.author.strip().split()[0]                                                  # from author name get the first name
        last_name = args.author.strip().split()[-1] if len(args.author.strip().split()) > 1 else ""  # get the last name if it exist 

        existing_author = session.query(Author).filter(
            Author.first_name == first_name,
            Author.last_name == last_name
        ).first()                                            # check if author already exists in the database

        if existing_author:
            logging.info("Author already exists in the database")
            db_author = existing_author
        else:
            author_schema = AuthorSchema(                         # create author schema object
                first_name=first_name,
                last_name=last_name,
                birth_date=None,
                nationality=None,
                biography=None
            )
            db_author = Author(**author_schema.model_dump())            # create author model object
            session.add(db_author)                                      # add author to the session
            session.commit()
            logging.info(f"A new author is added: {db_author.first_name} {db_author.last_name}")

        author_work=client.author_work(author_data['key'],args.limit)         # fetch works of the author using author key
        if args.output:
            with open(args.output,"a",encoding="utf-8") as f:
                f.write("/n/n")
                json.dump({"author":author_work},f,indent=4)

        inserted_books = 0
        for work in author_work:
            
            title = work.get("title")
            if not title:
                continue


            publication_date = None
            if work.get("created") and "value" in work["created"]:
                try:
                    publication_date = datetime.strptime(work["created"]["value"], "%Y-%m-%dT%H:%M:%S.%f")
                except ValueError:
                    publication_date = None


            work_id = work.get("key", "").split("/")[-1]         # extract work ID from the key
            if work_id:
                book_detail = client.book_detail(work_id)
                isbn = (book_detail[0].get("isbn_13") or book_detail[0].get("isbn_10") or [None])[0]     # get ISBN from book detail


            existing_book = session.query(Book).filter(
                Book.title == title, Book.author_id == db_author.author_id
            ).first()
            print(existing_book)
            if existing_book:
                existing_book.available_copies += 1           # if book already exists increment the available copies and total copies
                existing_book.total_copies += 1
                session.commit()
                logging.info(f"Book already exists, skipping: {title}")
                continue

            book_schema = BookSchema(
                title=title,
                isbn=isbn,
                publication_date=publication_date,
                total_copies=1,
                available_copies=1,
                author_id=db_author.author_id
            )
            db_book = Book(**book_schema.model_dump())
            try:
                session.add(db_book)
                session.commit()
                inserted_books += 1
                logging.info(f"Inserted Book: {db_book.title}")
            except IntegrityError:
                session.rollback()
                logging.warning(f"Duplicate Book skipped: {db_book.title}")

        logging.info(f"API fetch completed. {inserted_books} books inserted.")


    finally:
        session.close()                 # close the session


if __name__ == '__main__':
    main()