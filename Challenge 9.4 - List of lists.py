# Write a program that contains the following lists of lists:

# universities = [["California Institute of Technology", 2175, 37704], ["Harvard", 19627, 39849],
#                ["Massachusetts Institute of Technology", 10566, 40732], ["Princeton", 7802, 37000],
#                ["Rice", 5879, 35551], ["Stanford", 19535, 40569], ["Yale", 11701, 40500]]

# Define a function, enrollment_stats(), with a single parameter. This parameter should be a list of lists in which each
#   individual list contains three elements:
# 1. The name of a university
# 2. The Total number of enrolled students
# 3. The annual tuition fees

# enrollment_stats() should return two lists, the first containing all the student enrollment values and the second
# containing all the tuition fees.

# Next, define two functions, mean() and median(), that take a single list arguement and return the mean or median of
# the values in each list, respectively.

# Using universities, enrollment stats(), mean(), median(), calculate the total number of students, the total tuition,
# the mean and the median numbers of students, and the mean and median tuition values.

# Finally, output all values and format the output so that it will look life this:
# Total Students: 77,852
# Total Tuition: $ 271, 905

# Student mean: 11,040.71
# Student median: 10,566

# Tuition mean: $ 38,843.57
# Tuition median: $ 39,849

# answer:

universities = [["California Institute of Technology", 2175, 37704], ["Harvard", 19627, 39849],
                ["Massachusetts Institute of Technology", 10566, 40732], ["Princeton", 7802, 37000],
                ["Rice", 5879, 35551], ["Stanford", 19535, 40569], ["Yale", 11701, 40500]]

def enrollment_stats(lst):
    enrollments = [i[1] for i in lst]
    tuition_fees = [i[2] for i in lst]
    return enrollments, tuition_fees

def mean(lst):
    return sum(lst) / len(lst)

def median(lst):
    lst_sorted = sorted(lst)
    mid = len(lst_sorted) // 2
    if len(lst_sorted) % 2 == 0:
        return (lst_sorted[mid-1] + lst_sorted[mid]) / 2
    else:
        return lst_sorted[mid]

enrollments, tuition_fees = enrollment_stats(universities)


total_students = sum(enrollments)
total_tuition = sum(tuition_fees)

student_mean = mean(enrollments)
student_median = median(enrollments)

tuition_mean = mean(tuition_fees)
tuition_median = median(tuition_fees)

print(f"Total Students: {total_students:,}")
print(f"Total Tuition: $ {total_tuition:,}\n")

print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}\n")

print(f"Tuitions mean: $ {tuition_mean:,.2f}")
print(f"Tuitions median: $ {tuition_median:,}")