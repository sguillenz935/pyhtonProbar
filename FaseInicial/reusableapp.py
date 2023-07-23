print("Welcome to the conversor to lightyears")
#Establecemos una entrada que sera recibida en forma de str
parsecs_input = input("Input number of parsecs: ")
#Establecemos que la entrada sea tipo int para que pueda ser operada(multiplicacion)
parsecs = int(parsecs_input)
lightyears = parsecs * 3.26
#Mostramos la entrada de texto str y el resultado
print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")