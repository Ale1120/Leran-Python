# para poder abrir ficheros  con io desde un script
from io import open

texto = "Una linea con texto\nOtra linea con texto"

# #creando ficheros open(nombre, tipo) de escritura
# fichero = open('fichero.txt','w')
#
# # escribiendo dentro de un fichero
# fichero.write(texto)

# crear un fichero de modo lectura
#fichero = open('fichero.txt','r')

# pasando contenido al fichero de modo lectura
# texto = fichero.read()
# print(texto)

# leer las lineas
# lineas = fichero.readlines()
# print(lineas)

# abriendo fichero en modo extension se escribe al final
# fichero = open("fichero.txt", 'a')
# fichero.write("\nCuarta linea")
#
#
# # leer linea por linea
# fichero = open("fichero.txt", 'r')
# linea = fichero.readline()
# print("Primera linea: ", linea)
# linea = fichero.readline()
# print("Segunda linea: ", linea)
# linea = fichero.readline()
# print("Trimera linea: ", linea)
# linea = fichero.readline()
# print("Cuarta linea: ", linea)
#
#
# # lectura linea a linea con ciclos
# with open('fichero.txt','r') as fichero:
#     for linea in fichero:
#         print(linea)


# apuntando a un lugar especifico con seek
fichero = open('fichero.txt','r')
fichero.seek(10)
fichero.read()
