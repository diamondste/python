-- Create 3 new Dojos
INSERT INTO dojos (name)
VALUES ('Free dojo'), ('Cat dojo'), ('Ninja dojo');

-- Delete the 3 dojos you just created 
SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

-- Create 3 more dojos
INSERT INTO dojos (name)
VALUES ('Japan dojo'), ('Code dojo'), ('Senesi dojo');

-- Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
VALUES ('Piggy', 'Banks', 25, 10), ('Gary', 'Bot', 27 , 10), 
('Raven', 'Dyer', 28, 10 );

-- Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
VALUES ('Lily', 'Flower', 22, 11), ('Mike', 'Love', 29 , 11), 
('Paige', 'Roberts', 26, 11 );

-- Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
VALUES ('Andy', 'Park', 22, 12), ('Jay', 'Green', 29 , 12), 
('Paul', 'Cast', 26, 12);

-- Retrieve all the ninjas from the first dojo 
Select * FROM ninjas
WHERE dojo_id = 10;

-- Retrieve all the ninjas from the first dojo 
Select * FROM ninjas
WHERE dojo_id = 12;

-- Retrieve the last ninja's dojo 
SELECT dojos.name
FROM ninjas 
JOIN dojos 
ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 12;







