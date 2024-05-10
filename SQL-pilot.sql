CREATE TABLE User_main (
	User_id  INT NOT NULL AUTOINCREAMENT, 
	name VARCHAR,
	password VARCHAR,
	PRIMARY KEY User_id
);

INSERT INTO User_main (name) VALUES (Pet Lion);
INSERT INTO User_main (name) VALUES (tom jerry);
INSERT INTO User_main (name) VALUES (coward dog);
INSERT INTO User_main (name) VALUES (sponge bob);

INSERT INTO User_main (password) VALUES (fierce);
INSERT INTO User_main (password) VALUES (lmfao);
INSERT INTO User_main (password) VALUES (courage);
INSERT INTO User_main (password) VALUES (squarepants);