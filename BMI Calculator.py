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

while True :
    try:
        weight = int(input("Enter your weight(KG) : "))
        height = int(input("Enter your height(CM) : "))
        if weight <= 0 or height <= 0 :
            print('Enter a Valid number')
        else:
            break 
    except ValueError :
        print("Enter a Number not a Text or Negative Number")
    
print(myfunction(weight, height))