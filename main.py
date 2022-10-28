#------Funtions------

#find average based on status
def ug( homework, quizzes, midterm, final_exam):
    average = (0.2 * homework) + (0.2 * quizzes) + (0.3 * midterm) + (0.3 * final_exam)
    return(average)

def g( homework, quizzes, midterm, final_exam):
    average = (0.15 * homework) + (0.05 * quizzes) + (0.35 * midterm) + (0.45 * final_exam)
    return(average)

def dl( homework, quizzes, midterm, final_exam):
    average = (0.05 * homework) + (0.05 * quizzes) + (0.4 * midterm) + (0.5 * final_exam)
    return(average)

#Set max % to 100
def max_pert(input):
    if (input > 100.0):
        input = 100.0
    return (input)

#------Input------

#Take first input (student status)
status = str(input())
scores = input()
homework, quizzes, midterm, final_exam = scores.split()

#------Algorithm------

#convert to %
homework = (float(homework) / 800) * 100
quizzes = (float(quizzes) / 400) * 100
midterm = (float(midterm) / 150) * 100
final_exam = (float(final_exam) / 200) * 100

#set 100 as the max %
homework = max_pert(homework)
quizzes = max_pert(quizzes)
midterm = max_pert(midterm)
final_exam = max_pert(final_exam)


#Send error messesge if input is not UG, DL or G and find average based on status
if (status != "UG"):
    if (status != "G"):
        if (status != "DL"):
            print("Error: student status must be UG, G or DL")
            exit(1)
        else:
            average = dl( homework, quizzes, midterm, final_exam)
    else:
        average = g( homework, quizzes, midterm, final_exam)
else:
    average = ug( homework, quizzes, midterm, final_exam)

#------Output------
#print grade
print(f"Homework: {homework:2.1f}%")
print(f"Quizzes: {quizzes:2.1f}%")
print(f"Midterm: {midterm:2.1f}%")
print(f"Final Exam: {final_exam:2.1f}%")

#print average
print(f"{status} average: {average:2.1f}%")

#print course grade
if (average > 90.0):
    print("Course grade: A")
elif (average >80.0):
    print("Course grade: B")
elif (average >70.0):
    print("Course grade: C")
elif (average >60.0):
    print("Course grade: D")
else:
    print("Course grade: F")
