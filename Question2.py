# Buatlah program yang dapat menghitung hasil dari fungsi f(x) = 2x^3 + 2x + 15/x,
# di mana x merupakan bilangan bulat yang dimasukkan oleh pengguna. 

print("Calculator for f(x) = 2x^3 + 2x + 15/x")
x = int(input("Let x be: "))

result = (2 * (x**3)) + (2*x) + (15/x)
result = round(result, 2)

print(f"f({x}) = {result}")