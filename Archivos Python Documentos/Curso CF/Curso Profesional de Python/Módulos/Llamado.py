#Cuando llamamos un archivo se crea otro llamada "__pycache__", esto se genera cuando 
#importamos el archivo la primera vez o cuando el archivo importado sufre modificaciones

import Operaciones #Importo el archivo "Operaciones" y .....
import os 
os.system('clear')

print (Operaciones.producto(1,2)) #........ debo citar de donde llamo "suma"

#-------------------------------------------------------------------------------------------------------

from Operaciones import * #Importo todos los módulos de "Operaciones".......
resultado=Operaciones.suma(1,2)#....... Sin llamar el archivo citado


#-------------------------------------------------------------------------------------------------------

from Operaciones import resta #Importo los módulos de "Operaciones" que necesito unicamente 
from Operaciones import (suma, 
                        resta,
                        division)
print(suma(1,2))
print(division(1,2))
#-------------------------------------------------------------------------------------------------------

from Operaciones import suma as su #Importo los módulos de "Operaciones" que necesito y los renombro 
print(su(1,2))

#-------------------------------------------------------------------------------------------------------

#LLAMANDO UN PAQUETE
#Un paquete es una carpeta que contiene módulos, los módulos son archivos.py
from paquete.animal import (Perro, Gato)

Perro().nombre()
Gato().nombre("Felix") 