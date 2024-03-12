#Weight converter exercise

w = float(input("Please enter the weight: "))

unit = input("Please enter the unit - kgs or lbs: ")

print ("Weight converting...")

if unit in ("kgs" or "kg" or "kilograms"):
    weight = w / 0.45359237
    print (w,"kg is", weight, "lbs.")

elif unit in ("lbs" or "lb" or "pounds"):
    weight = w / 2.20462262
    print (w,"lbs is", weight, "kgs.")

else:
    print ("Incorrect. Please enter a correct unit")

