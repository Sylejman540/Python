costumers = {"Martin", "Jack", "Jones"}
costumer = "Martin"

print(costumer in costumers)

list_my = ["apples", "oranges" "vehicle"]

my_tuple = (1, 3, 4, 6, 6)

print(list_my)
print(my_tuple)

# Store the student GPA and student test score in two variables.
# Using nested conditionals check if the student is eligible for a full scholarship, partial, or no scholarship.
# Scholarship criteria:
# 3.  If a student has a GPA greater or equal to 3.5, and a test score of higher than 65, they’re eligible for a full scholarship.
# a.  If a student has a GPA greater or equal to 3.5, and a test score between 50 and 65, they’re eligible for a partial scholarship.
# b.  If a student has a GPA greater or equal to 3.5 but test score lower than 50, they’re not eligible for a scholarship.
# c.  If a student has a GPA lower than 3.5, they’re not eligible for a scholarship.

GPA = 3.0
test_score = 54

if GPA >= 3.5 and test_score > 65:
    print("Full Scholarship")
elif GPA >= 3.5 and 50 < test_score < 65:
    print("Partial Scholarship")
elif GPA >= 3.5 and test_score < 50:
    print("Not Eligible For A Scholarship")
else:
    print("Not Eligible For A Scholarship")
