# Sample Grades Project
# by Britney Duffy

# Write a program that reads in the csv file linked above and outputs the mean, median, and standard deviation
# for the fall & spring semesters. Make sure to write at least two functions in your final solution.
# The more generalizable you make your code, the more you may be able to reuse it for your own project later.
# To receive feedback, please submit a screenshot of your program & its output.

# Read in the CSV file

file = open("sample_grades.csv", 'r')
for line in file:
    print(line)
file.close()

for line in file:
    fall_grades = []
    spring_grades = []

    if "Fall 2016" in row:
        fall_grades.append(float(row[2]))
    elif "Spring 2016" in row:
        spring_grades.append(float(row[2]))





