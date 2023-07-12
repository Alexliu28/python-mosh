weight = input("please enter your weight: ")
judge = input("L or kg?")
if judge == "L" or  judge =="l":
    print(f"Your weight = {float(weight)*0.5} kg")
elif judge == "KG" or "kg":
    print(f"Your weight haha = {float(weight)*2} pounds")
else:
    print("Try again")