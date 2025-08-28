# lib_management/data_processor.py
import argparse
import logging
import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Library, Book, Author, Member
from schemas import LibrarySchema, BookSchema, AuthorSchema, MemberSchema

def setup_logger(level):
    logging.basicConfig(
        level=getattr(logging, level),
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def create_tables(engine):
    Base.metadata.create_all(engine)

def process_csv(file_path):
    return pd.read_csv(file_path)

def main():
    parser = argparse.ArgumentParser(description="ETL for Library Management System")
    parser.add_argument('--directory', '-d', required=True, help='Path to CSV directory')
    parser.add_argument('--db', required=True, help='Database URL')
    parser.add_argument('--log-level', default='INFO', help='Logging level')
    args = parser.parse_args()

    setup_logger(args.log_level)
    logging.info("Starting ETL process")

    engine = create_engine(args.db)
    Session = sessionmaker(bind=engine)
    session = Session()
    create_tables(engine)

    summary = {'libraries': 0, 'books': 0, 'authors': 0, 'members': 0, 'errors': 0}

    try:
        # Libraries
        libraries_df = process_csv(os.path.join(args.directory, 'libraries.csv'))
        for _, row in libraries_df.iterrows():
            try:
                lib_data = LibrarySchema(**row.to_dict())
                if not session.query(Library).filter_by(name=lib_data.name).first():
                    session.add(Library(**lib_data.dict()))
                    summary['libraries'] += 1
            except Exception as e:
                logging.error(f"Library row skipped: {e}")
                summary['errors'] += 1

        # Commit libraries first
        session.commit()

        # Books
        books_df = process_csv(os.path.join(args.directory, 'books.csv'))
        for _, row in books_df.iterrows():
            try:
                book_data = BookSchema(**row.to_dict())
                # Check if library exists
                if session.query(Library).filter_by(library_id=book_data.library_id).first():
                    if not session.query(Book).filter_by(isbn=book_data.isbn).first():
                        session.add(Book(**book_data.dict()))
                        summary['books'] += 1
                else:
                    raise ValueError("Referenced library does not exist")
            except Exception as e:
                logging.error(f"Book row skipped: {e}")
                summary['errors'] += 1

        # Authors
        authors_df = process_csv(os.path.join(args.directory, 'authors.csv'))
        for _, row in authors_df.iterrows():
            try:
                author_data = AuthorSchema(**row.to_dict()) 
                # checking for existing author by name
                if not session.query(Author).filter_by(first_name=author_data.first_name, last_name=author_data.last_name).first():
                    session.add(Author(**author_data.dict()))  # if not found add new author
                    summary['authors'] += 1
            except Exception as e:
                logging.error(f"Author row skipped: {e}")
                summary['errors'] += 1                  # if there is an error then it count the error

        # Members
        members_df = process_csv(os.path.join(args.directory, 'members.csv'))
        for _, row in members_df.iterrows():
            try:
                member_data = MemberSchema(**row.to_dict())
                # checking for existing member by email
                if not session.query(Member).filter_by(email=member_data.email).first():
                    session.add(Member(**member_data.dict()))   # if not found add new member
                    summary['members'] += 1
            except Exception as e:
                logging.error(f"Member row skipped: {e}")
                summary['errors'] += 1

        session.commit()
        logging.info(f"ETL completed: {summary}")  #display the summary of successful and failed records
    except Exception as e:
        session.rollback()
        logging.error(f"ETL failed: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    main()
