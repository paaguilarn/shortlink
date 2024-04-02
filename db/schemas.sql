create database shortlink;

\c shortlink;

create table url (
    id serial primary key,
    original_url varchar,
    short_url varchar(8),
    created_at timestamp not null default now()
);


create table event (
    id serial primary key,
    url_id int references url(id) not null,
    action varchar not null,
    "timestamp" timestamp not null default now()
);