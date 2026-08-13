# Weight converter

weight = float(input("Enter your weight so I can convert it: "))

unit = input("Kilograms or pounds? (K or L): ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"

elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"

else:
    print(f"{unit} was not valid")

if unit == "Lbs" or unit == "Kgs":
    print(f"Your weight is: {round(weight, 1)} {unit}")