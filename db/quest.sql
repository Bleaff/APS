
CREATE TABLE IF NOT EXISTS quest(
    id serial NOT NULL,
    rubrics text NOT NULL,
    text text NOT NULL,
    created_date timestamp without time zone NOT NULL
);

CREATE UNIQUE INDEX ON quest (id,md5(text));

