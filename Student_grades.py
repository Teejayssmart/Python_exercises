# Implement a function which takes a dictionary as a parameter
# in which student scores are stored and converts their scores to
# grades and return it as new dictionary.
#
# This is the scoring criteria:
#
# Scores 85 - 100: Grade = "Outstanding"
# Scores 65 - 84: Grade = "Good"
# Scores 50 - 64: Grade = "Acceptable"
# Scores 50 lower: Grade = "Fail"
# Example
#
# student_scores = {
#   "John": 90,
#   "Edy": 68,
#   "Marry": 88,
#   "Ewan": 79,
#   "Park": 62,
# }
# convert_grade(student_scores)



student_scores = {
  "John": 90,
  "Edy": 68,
  "Marry": 88,
  "Ewan": 79,
  "Park": 62,
}
#convert_grade(student_scores)


def student_score(score):
    new_score = {}
    if 85 <= score <= 100:
        print("Grade = Outstanding")
    elif 65 <= score <= 84:
        print("Grade = Good")
    elif 50 <= score <= 64:
        print("Grade = Acceptable")
    else:
        print ("fail")

    new_score["john"] = score = 90

