USE db;

CREATE TABLE IF NOT EXISTS comments (
    id          INT             NOT NULL    AUTO_INCREMENT,
    teacher_id  INT             NOT NULL,
    title       VARCHAR(255),
    comment     TEXT(20000)     NOT NULL,
    time        TIMESTAMP       NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS teachers (
    id          INT             NOT NULL AUTO_INCREMENT,
    score       INT             NOT NULL,
    name        VARCHAR(255)    NOT NULL,
    description TEXT(1000),
    PRIMARY KEY (id)
);