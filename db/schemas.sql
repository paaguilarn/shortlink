create database shortlink;

\c shortlink;

create table url (
    id serial primary key,
    original_url varchar,
    short_url varchar(8),
    created_at timestamp not null default now()
)
