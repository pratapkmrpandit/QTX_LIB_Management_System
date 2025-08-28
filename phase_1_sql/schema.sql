create database Lib_Management_system;
use Lib_Management_system;

create table Library(
    library_id int primary key auto_increment,
    name varchar(100) not null,
    campus_location varchar(100) ,
    contact_email varchar(100) unique not null ,
    phone_number varchar(15) ,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
);

create table Author (
    author_id int primary key auto_increment,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    birth_date date ,
    nationality varchar(100),
    biography text,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
);

create table Book (
    book_id int primary key auto_increment,
    title varchar(100) not null,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    publication_date date,
    total_copies int check (total_copies>=0),
    available_copies int check (available_copies>=0),
    library_id int not null,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp,
    foreign key (library_id) references Library (library_id) on delete cascade
);

create table Book_Author (
    book_id int not null,
    author_id int not null,
    primary key (book_id, author_id),
    foreign key (book_id) references Book (book_id) on delete cascade,
    foreign key (author_id) references Author (author_id) on delete cascade
);

create table Category(
    category_id int primary key auto_increment,
    name varchar(100) unique not null,
    description text ,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
);

create table Book_Category (
    book_id int not null,
    category_id int not null,
    primary key (book_id, category_id),
    foreign key (book_id) references Book (book_id),
    foreign key (category_id) references Category (category_id)
);

create table Member(
    member_id int primary key auto_increment,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    email varchar(100) unique not null,
    phone varchar(15) not null,
    member_type varchar(20) check(member_type in ('Student','Faculty')),
    registration_date date,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
);

create table Borrowing(
    borrowing_id int primary key auto_increment,
    member_id int not null,
    book_id int not null,
    borrow_date date not null,
    due_date date not null,
    return_date date,
    late_fee decimal(10,2) check (late_fee >= 0),
    created_at timestamp default current_timestamp, 
    updated_at timestamp default current_timestamp,
    foreign key (member_id) references Member (member_id) on delete cascade,
    foreign key (book_id) references Book (book_id) on delete cascade
);

create table Review(
    review_id int primary key auto_increment,
    book_id int not null,
    member_id int not null,
    rating int check (rating >= 1 and rating <= 5),
    comment text,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp,
    foreign key (book_id) references Book (book_id) on delete cascade,
    foreign key (member_id) references Member (member_id) on delete cascade
);





