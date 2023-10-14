DROP TABLE IF EXISTS account CASCADE;

CREATE TABLE account (
    id serial PRIMARY KEY,
    username varchar(40) NOT NULL,
    birthday date NOT NULL
    );

DROP TABLE IF EXISTS post CASCADE;

CREATE TABLE post (
    id serial PRIMARY KEY,
    account_id int NOT NULL,
    created_on timestamp NOT NULL,
    content text NOT NULL,
    FOREIGN KEY (account_id) REFERENCES account(id)
    );

DROP TABLE IF EXISTS like_post CASCADE;

CREATE TABLE like_post (
    id serial PRIMARY KEY,
    account_id int NOT NULL,
    post_id int NOT NULL,
    FOREIGN KEY (account_id) REFERENCES account(id),
    FOREIGN KEY (post_id) REFERENCES post(id)
    );