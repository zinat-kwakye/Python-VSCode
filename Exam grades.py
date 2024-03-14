#Calculating exam grades with levels

grade = int(input("Enter student's grade: "))




level = int(input("Enter 1 or 2 for student's level: "))



if level == 1:

    if grade < 50:
        print ("Fail.")

    elif 50 <= grade <= 60:
        print ("Pass.")

    elif 61 <= grade <= 70:
        print ("Merit.")

    elif 71 <= grade <= 100:
        print ("Distinction.")
    
    else:
        print ("Grade must be between 0 and 100.")
    

elif level == 2:

    if grade < 40:
        print ("Fail.")

    elif 40 <= grade <= 50:
        print ("Pass.")

    elif 51 <= grade <= 65:
        print ("Merit.")

    elif 66 <= grade <= 100:
        print ("Distinction.")
    
    else:
        print ("Grade must be between 0 and 100.")
    

else:
    print ("Level must be 1 or 2.")
