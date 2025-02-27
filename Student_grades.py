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
    "Mary": 88,
    "Ewan": 79,
    "Park": 62,
}


def new_funct(check):
    score = {}
    for key in check:
        new_score = check[key]
        if new_score >= 85:
            score[key] = "Outstanding"
        elif new_score >= 65:
            score[key] = "Good"
        elif new_score >= 50:
            score[key] = "Acceptable"
        else:
            score[key] = "Fail"
    return score


print(new_funct(student_scores))

# def score_list(student_scores):
#     score = {}
#     score["John"] = "Outstanding"
#     score["Edy"] = "Good"
#     score["Mary"] = "Outstanding"
#     score["Ewan"] = "Good"
#     score["Park"] = "Acceptable"
#     return score


# print(score_list(student_scores))

# convert_grade(student_scores)


# def student_score(score):
#     new_score = {}
#     for name in student_scores:
#         if 85 <= score <= 100:
#             new_score[name] = "Outstanding"
#             return new_score
#
#         elif 65 <= score <= 84:
#             new_score[name] = "Good"
#             return new_score
#
#         elif 50 <= score <= 64:
#             new_score[name] = "Acceptable"
#             # return "Grade = Acceptable"
#             return new_score
#
#         else:
#             new_score[name] = "Fail"
#             return new_score
#
#
# result = student_score(76)
# print(result)
