# Task #1: grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93] Sort the grades in descending order and display the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)


# Task #2: Calculate the average grade and display it.

number_of_grades = len(grades)
average_grade = sum(grades) / number_of_grades

print(average_grade)


# Task #3: Replace any grade below 80 with the value Failed. 

