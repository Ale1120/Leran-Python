n1 = float(input('agregar numero'))
n2 = float(input('agregar otro numero'))

print(""" Que quieres hacer?
1) sumar
2) Restar
3) Multiplicar""")
opcion = input()

if opcion == '1':
    print("La suma es: ", n1+n2)
elif opcion == '2':
    print("La resta es: ", n1-n2)
elif opcion == '3':
    print("El producto es: ", n1*n2)
else:
    print('comando erroneo')

# ejerccio 2

numero = 0
while numero % 2 == 0:
    numero = int( input('introduce un numero impar:'))

# ejerccio 3 range (inicio,fin,salto)
suma = sum(range(0,101,2))
print(suma)

# ejerccio 4

numeros = int(input("cuantos numeros quieres guardar:"))

suma = 0

for i in range(numeros):
    suma += float(input('agrega un numero:'))

print("se agregaron", numeros, "que se sumaron",suma, "y la media es:",suma/numeros)

# ejerccio 5

numeros = [1,3,6,9]

while True:
    numero = int( input('agrega un numero del 0 a 9'))
    if numero >= 0 and numero <=9:
        break

if numeros in numeros:
    print('El numero', numero, 'se encuentra en la lista', numeros)
else:
    print('El numero', numero, 'no se encuentra en la lista', numeros)

# ejerccio 6

print( list(range(0,11)))
print( list(range(-10,1)))
print( list(range(0,21,2)))
print( list(range(-19,0,2)))
print( list(range(0,51,5)))

# ejerccio 7
l1 = ["h","o","l","a", "", "m","u","n","d","o"]
l2 = ["h","o","l","a", "", "l","u","n","a"]
l3 = []
for i in l1
if l in l2 and l not in l3:
    l3.append(l)

print(l)
