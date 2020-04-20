/* ¿Que tipo de entidades? Autores
Nombre: Autores
*/

Nombre
Genero
Fecha de nacimiento
País de origen

columna y el tipo de dato
--Generamos la tabla 
CREATE TABLE autores(

autor_ID INT,--Las columnas se separan por "Comas"
--Estos campos no serán duplicados
nombre VARCHAR(25),  --Columna compuesta 
apellido VARCHAR(25),
genero CHAR(1),--M o F
Fecha_de_nacimiento DATE,
Pais_Origen VARCHAR(40)
);


--Se copia y se pega la creación de la anterior tabla SIN LOS COMENTARIOS


/* 
Tipos de datos
Abrir temario playlist_play

En general, la mayoría de los servidores de base de datos nos permiten almacenar los
mismo tipo de datos, como strings, fechas y número.

En este post, listamos los tipos de datos que más utilizarás en tu día a día.
Alfanuméricos

    CHAR
    VARCHAR

En ambos casos nosotros debemos de especificar la longitud máxima que podrá 
almacenar el campo. Opcionalmente podemos definir el charset que almacenará.

varchar(20) character set utf8


    Con MySQL nosotros podemos establecer el charset que usará la base de datos 
    desde su creación create database nombre character set utf8;

    NOTA: 
    UTF-8 es un formato de codificación de caracteres Unicode e ISO 10646 que 
    utiliza símbolos de longitud variable. UTF-8 fue creado por Robert C. Pike 
    y Kenneth L. Thompson. Está definido como estándar por la RFC 3629 de la 
    Internet Engineering Task Force.​

Números enteros

Tipo 	Rango
Tinyint 	-128 a 127
Smallint 	-32,768 a 32,767
Mediumint 	−8,388,608 a 8,388,607
Int 	−2,147,483,648 a 2,147,483,647
Bigint 	−9,223,372,036,854,775,808 a 9,223,372,036,854,775,807

Números flotantes

Para los flotantes encontraremos dos tipos

    Float
    Double

En ambos casos nosotros debemos de especificar la cantidad de dígitos que almacenará
la columna antes y después del punto (p,s)

precio FLOAT(3, 2)

En este caso la columna podrá almacenar hasta tres dígitos como enteros y dos después
del punto decimal.
Por ejemplo 999.99


Tiempo

Tipo 	Formato default
Date 	YYYY-MM-DD
Datetime 	YYYY-MM-DD HH:MI:SS
Timestamp 	YYYY-MM-DD HH:MI:SS
Time 	HHH:MI:SS
*/
