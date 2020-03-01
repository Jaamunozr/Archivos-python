from matplotlib import pyplot
import time
import os
Datos=('uno','dos','tres')
valores=(100,12,23)
colores=('red','green','blue')
separado=(0.1,0,0)
pyplot.rcParams['toolbar']='None'


# pyplot.pie(valores, colors=colores) 
'''Con el comando anterior podemos imprimir 
unicamente la grafica de la manera más simple,
se reemplazará por el siguiente'''

_, _, texto = pyplot.pie(valores, colors=colores,labels=Datos,
                        explode = separado, #Indica la separación entre los datos, sirve para resaltar un pedazo de torta
                        startangle=90) #Gira la grafica 90 grados, comenzando con "uno" en sentido contrario de reloj
for text in texto:
    text.set_color('white')

pyplot.axis('equal')
pyplot.title('Graficas prueba')
#pyplot.legend(labels=Datos) #otra alternativa para imprimir la legenda
#pyplot.show() #Imprime la torta pero se omite para poder guardar el formato en .png
pyplot.savefig('Pruba torta.png')



time.sleep(1)
os.system("clear")