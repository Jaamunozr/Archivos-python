from matplotlib import pyplot
import time
import os
Datos=('uno','dos','tres')
valores=(100,12,23)
colores=('red','green','blue')
separado=(0.1,0,0)
pyplot.rcParams['toolbar']='None' #Desactiva el cuadro inferior que se imprime con cualquier grafico
pyplot.ion()


# pyplot.pie(valores, colors=colores) 
'''Con el comando anterior podemos asignar valores a la torta
para posteriormente poder imprimir 
unicamente la grafica de la manera más simple,
se reemplazará por lo siguiente'''

_, _, texto = pyplot.pie(valores, #imprime tora con los valores distribuidos en el circulo
                        colors=colores,#Da color a la torta
                        labels=Datos,#Imprime datos de cada fracción
                        autopct='%1.1f%%', #indica cuantos decimales de la tora posee cada fraccion 
                        explode = separado, #Indica la separación entre los datos, sirve para resaltar un pedazo de torta
                        startangle=90) #Gira la grafica 90 grados, comenzando con "uno" en sentido contrario de reloj
for text in texto:
    text.set_color('white') #Da color a los textos internos de la torta 

pyplot.axis('equal')
pyplot.title('Graficas prueba')
#pyplot.legend(labels=Datos) 
'''otra alternativa para imprimir la legenda, se caracteriza por estar en un cuadro aparte, 
ideal cuando la torta tiene varias divisiones'''

#pyplot.show() #Imprime la torta pero se omite para poder guardar el formato en .png
pyplot.savefig('Prueba torta.png')



time.sleep(5)
os.system("clear")
#os.system("^Z")