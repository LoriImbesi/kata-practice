USE plants;
DROP TABLE IF EXISTS plants;
DROP TABLE IF EXISTS plant_types;
DROP TABLE IF EXISTS pots;
DROP TABLE IF EXISTS fertilizers;




CREATE TABLE plant_types (
plant_type_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(200)

);

CREATE TABLE pots (
pot_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(200)

);

CREATE TABLE fertilizers (
fertilizer_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(200)

);
CREATE TABLE plants (
plant_id INT AUTO_INCREMENT PRIMARY KEY,
plant_type_id INT,
pot_id INT,
fertilizer_id INT,
last_fertilized TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (plant_type_id) REFERENCES plant_types(plant_type_id),
FOREIGN KEY (pot_id) REFERENCES pots(pot_id),
FOREIGN KEY (fertilizer_id) REFERENCES fertilizers(fertilizer_id)


);
INSERT INTO plant_types (name) VALUES ('begonia');
INSERT INTO plant_types (name) VALUES ('oxalis');
INSERT INTO plant_types (name) VALUES ('Christmas_cactus');
INSERT INTO plant_types (name) VALUES ('philodendron'),('ficus');
INSERT INTO pots (name) VALUES ('tan crock');
INSERT INTO pots (name) VALUES ('green ceramic');
INSERT INTO fertilizers (name) VALUES ('compost tea'), ('cactus food');
INSERT INTO plants (plant_type_id, pot_id, fertilizer_id) VALUES (1, 1, 1), (1, 2, 2), (3, 1, 1);

SELECT * FROM plant_types;
SELECT * FROM pots;
SELECT * FROM fertilizers;
SELECT * FROM plants
INNER JOIN plant_types ON plants.plant_type_id = plant_types.plant_type_id
INNER JOIN pots ON plants.pot_id = pots.pot_id
INNER JOIN fertilizers ON plants.fertilizer_id = fertilizers.fertilizer_id;