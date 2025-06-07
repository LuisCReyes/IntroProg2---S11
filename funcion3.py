"""
Formula area = pi * (r * r)
"""
import math

def calcular_area(r):
    area= math.pi * r ** 2
    return area

def main():
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area(radio)
    print(f"El area del círculo es: {area:.2f}")
    
    
main()