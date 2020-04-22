DROP DATABASE IF EXISTS libreria_cf;
CREATE DATABASE IF NOT EXISTS libreria_cf;

USE libreria_cf;

CREATE TABLE IF NOT EXISTS autores(
    autor_ID INT NOT NULL,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25)NOT NULL,
    seudonimo VARCHAR(50) UNIQUE,
    genero CHAR(1) NOT NULL,
    Fecha_de_nacimiento DATE NOT NULL,
    Pais_Origen VARCHAR(40) NOT NULL,
    Fecha_Creación DATETIME DEFAULT current_timestamp
);

INSERT INTO autores(autor_ID, nombre, apellido, genero, Fecha_de_nacimiento, Pais_Origen)
VALUES(1,'Test autor','Test autor','M','2020-03-21','Colombia'),
      (2,'Test autor','Test autor',"M",'2018-03-21','Colombia'),
      (3,'Test autor','Test autor','M','2018-03-21','Colombia'),
      (4,'Test autor','Test autor','M','2018-03-21','Colombia');

INSERT INTO autores(autor_ID, nombre, apellido,seudonimo ,genero, Fecha_de_nacimiento, Pais_Origen)
VALUES(10,'Javier','Muñoz',"Javi M",'M','1993-12-19','Colombia');


SELECT * FROM autores;



