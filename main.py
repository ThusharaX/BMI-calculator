from os import sys

def main():
    name = input("Enter Name : ")
    height_m = input("Height (m) : ")
    weight_kg = input("Weight (kg) : ")

    height_m = float(height_m)
    weight_kg = float(weight_kg)

    def bmi_calculator(name, height_m, weight_kg):
        bmi = weight_kg / (height_m ** 2)
        print()
        print("BMI :",bmi)
        if bmi < 25:
            return name + " is not overweight"
        else:
            return name + " is OVERWEIGHT"

    result = bmi_calculator(name, height_m, weight_kg)
    print (result)
    print()
    print('''Press ENTER to check again
    Press "q" to quit :''')
    choice = input()
    print()
    if choice == 'q':
        sys.exit(0)
    else:
        main()

main()