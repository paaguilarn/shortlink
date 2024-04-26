create database shortlink;

\c shortlink;

create table url (
    id bigserial primary key,
    original_url varchar,
    short_url varchar(11),
    created_at timestamp not null default now()
);


create table event (
    "uuid" uuid primary key default gen_random_uuid(),
    url_id bigint references url(id) not null,
    action varchar not null,
    "timestamp" timestamp not null default now()
);