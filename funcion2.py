#Sumar dos números

def sumar(num1, num2):
    return num1 + num2


n1 =int(input("Ingresa un número: "))
n2 =int(input("Ingresa otro número: "))

suma = sumar(n1, n2)
print(f"La suma de {n1} y {n2} es: {suma}")