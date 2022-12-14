student_scores = input("Input a list of student scores ").split()
highscore = 0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n] > highscore:
    highscore = student_scores[n]
print(student_scores)
print("The highscore is {}".format(highscore))