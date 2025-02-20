# Check Age for Voting Eligibility
# Write a Python program that asks the user for their age.
#     If the age is 18 or older, print "You are eligible to vote.",
#     otherwise print "You are not eligible to vote.".

user_age = int(input("enter age: "))
if user_age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")