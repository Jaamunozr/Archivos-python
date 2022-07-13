/*
/// Prueba LED
#include <Arduino.h>
#define onboard 13

void setup() {
  pinMode(onboard, OUTPUT);
}

void loop() {
  digitalWrite(onboard,LOW);
  delay(100);
  digitalWrite(onboard,HIGH);
  delay(100);
    digitalWrite(onboard,LOW);
  delay(1000);
  digitalWrite(onboard,HIGH);
  delay(1000);
}
*/
///-----------------------------------------------------
/*
///    PRUEBA SENSOR TEMPERATURA
#include <OneWire.h>
#include <DallasTemperature.h>

#define DATO 2

OneWire ourWire (DATO);
DallasTemperature sensors (&ourWire);
 

void setup() {
  delay(1500);
  Serial.begin (9600);
  sensors.begin ();
}
void loop() {
  sensors.requestTemperatures ();

  Serial.print (sensors.getTempCByIndex (0));
  Serial.print (" Grados Centigrados \n");
  delay (1000);
}

*/



/*
--------------------------------------------------------------------------------------

    ARDUINO NANO
    33. CONEXION CON PANTALLA OLED DE 0,96" POR I2C CON CONTROLADOR SSD1306
    AUTOR : JOSE MARIA MENDEZ RUIZ
    FECHA : NOVIEMBRE 2021

    Libreria del I2C que maneja el LCD OLED : Adafruit_SSD1306 y Adfruit-GFX-Library.
    Estas librerías las descargamos desde el propio entorno de programación a través del menú superior > Herramientas> Administrar Bibliotecas y busca SSD1306, de entre las que salgan busca Adafruit_SSD1306 y 
    después sino se muestra de forma automática instalar GFX , buscaremos GFX y de las que salgan seleccionamos la indicada Adafruit.

    También podéis bajarlas de :
    
    https://github.com/adafruit/Adafruit_SSD1306
    https://github.com/adafruit/Adafruit-GFX-Library
        
    CODIGO LIBRE PARA UTILIZAR COMO QUIERAS
    
*/
 /*
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
 
// DECLARAMOS LAS VARIABLES QUE INDICAN LOS PINES QUE VAMOS A UTILIZAR
// TODO LO HACEMOS MEDIANTE EL CANAL I2C

String frase;                  // Para la frase que queremos mostrar en el lcd
int ancho = 128;               // ancho pantalla en puntos
int alto = 64;                 // alto pantalla en puntos

Adafruit_SSD1306 display(ancho, alto, &Wire, -1);
 
void setup() {
 
  // Iniciamos la pantalla y si no esta, entrara en un bucle sin fin
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    while (true);
  }  
  display.clearDisplay();               // Limpiamos pantalla  
}
 
void loop() {

    display.drawRect(20, 18, 20, 28, SSD1306_WHITE); // Dibuja un rectángulo

    frase = "! Hola !";
    display.setTextSize(2);               // Tamaño del texto  
    display.setTextColor(SSD1306_WHITE);  // Color WHITE para que se vea el texto, el color sera el del propio lcd
    display.setCursor(0, 1);              // Posición del texto en puntos 
    display.println(frase);               // Imprimimos la frase
    display.display();                    // Volcamos la información en el display para mostrarla

    // Mueve todo el contenido de la pantalla de izquierda a derecha
    display.startscrollright(0x00, 0x0F);
    delay(5000);
    display.stopscroll();
  
    // Mueve todo el contenido de la pantalla de derecha a izquierda
    display.startscrollleft(0x00, 0x0F);
    delay(5000);
    display.stopscroll();
  
}
//-----------------------------------------------------------------------------------

*/

/*
///    PRUEBA SENSOR TEMPERATURA  ---- 1 SOLO SENSOR ---- SI FUNCIONÓ


#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define DATO 2  //ENTRADA SENSOR DE TEMPERATURA

OneWire ourWire (DATO);
DallasTemperature sensors (&ourWire);
// DECLARAMOS LAS VARIABLES QUE INDICAN LOS PINES QUE VAMOS A UTILIZAR
// TODO LO HACEMOS MEDIANTE EL CANAL I2C
String frase;                  // Para la frase que queremos mostrar en el lcd
int ancho = 128;               // ancho pantalla en puntos
int alto = 64;                 // alto pantalla en puntos
Adafruit_SSD1306 display(ancho, alto, &Wire, -1);

void setup() {
  sensors.begin ();
   // Iniciamos la pantalla y si no esta, entrara en un bucle sin fin
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    while (true);
  }  
  display.clearDisplay();               // Limpiamos pantalla  
}

void loop() {
   sensors.requestTemperatures ();
   frase = sensors.getTempCByIndex (0);
   delay (1000);
   display.setTextSize(1);               // Tamaño del texto  
   display.setTextColor(SSD1306_WHITE);  // Color WHITE para que se vea el texto, el color sera el del propio lcd
   display.setCursor(30,1); // Posición del texto en puntos 
   display.println("TEMPERATURA"); 
   display.drawLine(0,15,128,15, WHITE);  // IMPRIMIR LÍNEA
   display.setTextSize(3,4);               // Tamaño del texto               // Imprimimos la frase
   display.setCursor(2, 25); // Posición del texto en puntos 
   display.println(frase + " C");               // Imprimimos la frase
   display.drawCircle(100, 27, 4, WHITE);
   display.drawLine(0,60,128,60, WHITE);  // IMPRIMIR LÍNEA
   display.display();                    // Volcamos la información en el display para mostrarla
   display.clearDisplay();
}

*/




/*

//PRUEBA DIVIDIENDO LA PANTALLA EN DOS, SOLO UN SENSOR, MISMA LECTURA

#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define DATO 2  //ENTRADA SENSOR DE TEMPERATURA

OneWire ourWire (DATO);
DallasTemperature sensors (&ourWire);
// DECLARAMOS LAS VARIABLES QUE INDICAN LOS PINES QUE VAMOS A UTILIZAR
// TODO LO HACEMOS MEDIANTE EL CANAL I2C
String frase;                  // Para la frase que queremos mostrar en el lcd
int ancho = 128;               // ancho pantalla en puntos
int alto = 64;                 // alto pantalla en puntos
Adafruit_SSD1306 display(ancho, alto, &Wire, -1);

void setup() {
  sensors.begin ();
   // Iniciamos la pantalla y si no esta, entrara en un bucle sin fin
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    while (true);
  }  
  display.clearDisplay();               // Limpiamos pantalla  
}

void loop() {
   sensors.requestTemperatures ();
   frase = sensors.getTempCByIndex (0);
   delay (1000);
   display.drawLine(0,0,128,0, WHITE);  // IMPRIMIR LÍNEA
   display.setTextSize(1);               // Tamaño del texto  
   display.setTextColor(SSD1306_WHITE);  // Color WHITE para que se vea el texto, el color sera el del propio lcd
   display.setCursor(10,2); // Posición del texto en puntos 
   display.println("TEMPERATURA INTERNA"); 
   display.drawLine(0,10,128,10, WHITE);  // IMPRIMIR LÍNEA
   display.setTextSize(2);               // Tamaño del texto               // Imprimimos la frase
   display.setCursor(25,13); // Posición del texto en puntos 
   display.println(frase + " C");               // Imprimimos la frase
   display.drawCircle(112, 15, 3, WHITE);
   display.drawLine(0,31,128,31, WHITE);  // IMPRIMIR LÍNEA
   display.setTextSize(1);
   display.setCursor(10,33); // Posición del texto en puntos 
   display.println("TEMPERATURA EXTERNA");
   display.drawLine(0,42,128,42, WHITE);  // IMPRIMIR LÍNEA
   display.setTextSize(2,2);               // Tamaño del texto               // Imprimimos la frase
   display.setCursor(25, 46); // Posición del texto en puntos 
   display.println(frase + " C");
   display.drawCircle(112, 48, 3, WHITE);               // Imprimimos la frase
   display.drawLine(0,63,128,63, WHITE);  // IMPRIMIR LÍNEA
   display.display();                    // Volcamos la información en el display para mostrarla
   display.clearDisplay();
}

*/
//PRUEBA DIVIDIENDO LA PANTALLA EN DOS, SOLO UN SENSOR, MISMA LECTURA

#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define DATO 2  //ENTRADA SENSOR DE TEMPERATURA

OneWire ourWire (DATO);
DallasTemperature sensors (&ourWire);
// DECLARAMOS LAS VARIABLES QUE INDICAN LOS PINES QUE VAMOS A UTILIZAR
// TODO LO HACEMOS MEDIANTE EL CANAL I2C
String TEMP_A;                  // Para la frase que queremos mostrar en el lcd
String TEMP_B;                  // Para la frase que queremos mostrar en el lcd
int ancho = 128;               // ancho pantalla en puntos
int alto = 64;                 // alto pantalla en puntos
Adafruit_SSD1306 display(ancho, alto, &Wire, -1);

void setup() {
  sensors.begin ();
   // Iniciamos la pantalla y si no esta, entrara en un bucle sin fin
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    while (true);
  }  
  display.clearDisplay();               // Limpiamos pantalla  
}

void loop() {
   sensors.requestTemperatures ();
   TEMP_A = sensors.getTempCByIndex (0);
   TEMP_B = sensors.getTempCByIndex (1);
   delay (1000);
   display.drawLine(0,0,128,0, WHITE);  // IMPRIMIR LÍNEA
   display.setTextSize(1);               // Tamaño del texto  
   display.setTextColor(SSD1306_WHITE);  // Color WHITE para que se vea el texto, el color sera el del propio lcd
   display.setCursor(10,2); // Posición del texto en puntos 
   display.println("TEMPERATURA INTERNA"); 
   display.drawLine(0,10,128,10, WHITE);  // IMPRIMIR LÍNEA
   display.setTextSize(2);               // Tamaño del texto               // Imprimimos la frase
   display.setCursor(25,13); // Posición del texto en puntos 
   display.println(TEMP_A + " C");               // Imprimimos la frase
   display.drawCircle(112, 15, 3, WHITE);
   display.drawLine(0,31,128,31, WHITE);  // IMPRIMIR LÍNEA
   display.setTextSize(1);
   display.setCursor(10,33); // Posición del texto en puntos 
   display.println("TEMPERATURA EXTERNA");
   display.drawLine(0,42,128,42, WHITE);  // IMPRIMIR LÍNEA
   display.setTextSize(2,2);               // Tamaño del texto               // Imprimimos la frase
   display.setCursor(25, 46); // Posición del texto en puntos 
   display.println(TEMP_B + " C");
   display.drawCircle(112, 48, 3, WHITE);               // Imprimimos la frase
   display.drawLine(0,63,128,63, WHITE);  // IMPRIMIR LÍNEA
   display.display();                    // Volcamos la información en el display para mostrarla
   display.clearDisplay();
}
