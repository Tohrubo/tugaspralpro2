# Buatlah program yang dapat menghitung berat badan yang diperlukan,
# jika diketahui tinggi badan dan nilai Body Mass Index (BMI) yang diharapkan!
# Body Mass Index dihitung dengan cara: BMI = berat/tinggi^2.
# Perhatikan, berat badan dalam satuan kilogram (kg) dan tinggi badan dalam satuan meter (m). 

print("BMI Calculator")
BMI = float(input("What is your BMI scale?: "))
height = float(input("What is your height? (in m): "))

weight = round(BMI * (height**2), 2)


print(f"Your weight is: {weight}kg")