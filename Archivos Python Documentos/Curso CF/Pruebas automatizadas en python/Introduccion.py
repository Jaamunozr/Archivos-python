class hola():
    def saludo(texto):
        return print("Lo que usted dijitó fue: ",texto)

def fibonacci(Numero):
    if Numero == 0: return 0
    if Numero == 1: return 1
    else: return fibonacci(Numero-1) + fibonacci(Numero-2)

def holala():
    return

print (fibonacci(12))
hola.saludo("hola mundo")