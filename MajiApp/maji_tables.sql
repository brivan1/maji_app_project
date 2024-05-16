CREATE TABLE User_maji(
username VARCHAR(50) NOT NULL,
email VARCHAR(256) UNIQUE NOT NULL
);


INSERT INTO User_maji(username, email) VALUES ('PetLion', 'PetLion@gmail.com');