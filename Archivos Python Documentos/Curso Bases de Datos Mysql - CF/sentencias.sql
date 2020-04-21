DROP DATABASE libreria_cf;
CREATE DATABASE libreria_cf;

USE libreria_cf;

CREATE TABLE autores(
    autor_ID INT,
    nombre VARCHAR(25),
    apellido VARCHAR(25),
    genero CHAR(1),
    Fecha_de_nacimiento DATE,
    Pais_Origen VARCHAR(40)
);

INSERT INTO autores(autor_ID, nombre, apellido, genero, Fecha_de_nacimiento, Pais_Origen)
VALUES(1,'Test autor','Test autor','M','2020-03-21','Colombia'),
      (2,'Test autor','Test autor','M','2018-03-21','Colombia'),
      (3,'Test autor','Test autor','M','2018-03-21','Colombia'),
      (4,'Test autor','Test autor','M','2018-03-21','Colombia');


SELECT * FROM autores;