# Lab 7 - Classes

class Students:

    #score = 0 

    def __init__(self, name):
        self.name = name
       # self.score1 = testScore1
       # self.score2 = testScore2
       # self.score3 = testScore3
      #  self.score = score  

    def averageScore(self, testScore1, testScore2, testScore3):
       score = (testScore1 + testScore2 + testScore3) / 3
       return (score)
    

student1 = Students(input("Enter student's name: "))

print ("Student:",student1.name)

#score = 0 

testScore1 = Students(int(input("Enter the score of the first test: ")))
testScore2 = Students(int(input("Enter the score of the second test: ")))
testScore3 = Students(int(input("Enter the score of the third test: ")))

#studentScore = Students(averageScore)

#print (Students.score)

Students.averageScore()

#avgscore = Students.averageScore()

#print(avgscore)