import argparse
import json
import logging
from .database import Base, get_engine, get_session
from .api_client import OpenApiClient
from .schema import AuthorSchema
from .model import Author


def main():
    parser = argparse.ArgumentParser(description="Fetch books from OpenLibrary")
    parser.add_argument("--author", required=True, help="Author name to search")
    parser.add_argument("--limit", type=int, default=10, help="Number of books to fetch")
    parser.add_argument("--db", required=True, help="Database connection string")
    parser.add_argument("--output", required=True, help="Output file name")
    parser.add_argument("--log", default="INFO", help="Log level (DEBUG, INFO, WARNING, ERROR)")
    args = parser.parse_args()

    logging.basicConfig(level=args.log.upper(), format="%(asctime)s : %(levelname)s : %(message)s")
    logging.info("Starting API data fetching process")

    engine = get_engine(args.db)
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

        first_name = args.author.strip().split()[0]
        last_name = args.author.strip().split()[-1] if len(args.author.strip().split()) > 1 else ""

        existing_author = session.query(Author).filter(
            Author.first_name == first_name,
            Author.last_name == last_name
        ).first()

        if existing_author:
            logging.info("Author already exists in the database")
            db_author = existing_author
        else:
            author_schema = AuthorSchema(
                first_name=first_name,
                last_name=last_name,
                birth_date=None,
                nationality=None,
                biography=None
            )
            db_author = Author(**author_schema.model_dump())
            session.add(db_author)
            session.commit()
            logging.info(f"A new author is added: {db_author.first_name} {db_author.last_name}")

        author_work=client.author_work(author_data['key'],args.limit)
        print("/n"*10,author_work)
        if args.output:
            with open(args.output,"a",encoding="utf-8") as f:
                f.write("/n/n")
                json.dump({"author":author_work},f,indent=4)

        

    finally:
        session.close()


if __name__ == '__main__':
    main()
