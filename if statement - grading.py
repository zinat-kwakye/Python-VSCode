#if statement - grading 

grade = int(input("Please enter the grade: "))

if grade >= 85:
    print ("Distinction")

elif 65 <= grade < 85:  #elif grade >=: you don't need to add the ceiling in elif statement, as it knows that it's not 85.
    print ("Pass")

else:
    print ("Fail")