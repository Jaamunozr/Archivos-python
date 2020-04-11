import os
os.system ('clear')
#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)

#Date
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))


#Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))

"""
Operaciones

En ocasiones tendremos la necesidad de realizar ciertas operaciones con fechas,
ya sea agregar días, restar años o simplemente realizar comparaciones. Con Python
todas estas operaciones podremos realizarlas sin ningún problema.
"""
from datetime import datetime
from datetime import timedelta

#Sumar dos días a la fecha actual
now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

#Comparación
if now < new_date:
    print("La fecha actual es menor que la nueva fecha")


'''Formato de fechas

Aunque las fechas en Python ya poseen un formato legible para los humanos, 
en ocasiones necesitaremos ser más explícitos para no dejar espacio a la ambiguuedad,
para ello, haremos uso del método strftme.'''

now = datetime.now()
format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format)

'''Algo que en lo particular me gusta hacer es definir una función que me permita obtener
un formato mucho más amigable.'''

from datetime import datetime

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

now = datetime.now()
print(current_date_format(now))

