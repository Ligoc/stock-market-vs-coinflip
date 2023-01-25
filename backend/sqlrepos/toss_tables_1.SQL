-- SQLite

DROP TABLE IF EXISTS toss_history;
DROP TABLE IF EXISTS toss_data;

CREATE TABLE toss_history (
    `id` integer primary key autoincrement,
    `date` datetime NOT NULL,
    `toss_count` integer NOT NULL,
    `index` varchar(10) NOT NULL,
    `start_date` datetime NOT NULL
    );

CREATE TABLE toss_data (
    `id` integer primary key autoincrement,
    `start_date` datetime NOT NULL,
    `calucalted_balance` decimal(11, 4) NOT NULL,
    `cumulative_difference` decimal(11, 4) NOT NULL,
    `history_id` integer NOT NULL
    );
