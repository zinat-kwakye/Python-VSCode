#Lab 5 - Functions
import statistics

data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(",") 

grades = list(map(int, grades))           #converting string list to integer list

#print(grades)

#Finding min number
print ("The minimum number is:",min(grades))

#Finding max number
print ("The maximum number is:",max(grades))

#Average of the grade to 2 d.p.
average = sum(grades) / len(grades)

print ("The average is:",round(average,2))

#The mean to 2 d.p.
mean = statistics.mean(grades)
print ("The mean number is:",round(mean,2))

#The median to 2 d.p.
print ("The median number is:",statistics.median(grades))

#.string format
print("The average is {} and the mean is {}".format(average,mean))
