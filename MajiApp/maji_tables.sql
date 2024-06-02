CREATE TABLE User_maji(
username VARCHAR(50) NOT NULL,
password VARCHAR(256) UNIQUE NOT NULL
);


INSERT INTO User_maji(username, password) VALUES ('PetLion', 'PetLion@gmail.com');

