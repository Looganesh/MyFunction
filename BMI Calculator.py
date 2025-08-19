def myfunction (weight, height):
    meter = (height / 100) ** 2
    bmi = round(weight / meter)
    print(f"Your BMI are : {bmi}")

    if bmi > 40.0 :
        return "You're Obese (Class III)"
    elif bmi > 35.0:
        return "You're Obese (Class II)"
    elif bmi > 30.0:
        return "You're Obese (Class I)"
    elif bmi > 25.0:
        return "You're Overweight"
    elif bmi > 18.5:
        return "You're Normal weight"
    else:
        return "You're Underweight"

weight = int(input("Enter your weight(KG) : "))
height = int(input("Enter your height(CM) : "))

print(myfunction(weight, height))