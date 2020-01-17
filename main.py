from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

# Create 4, or more, exercises.

exercise1 = Exercise("Universe Creation", "Python")
exercise2 = Exercise("Lego Ledger", "React")
exercise3 = Exercise("Dream Diary", "JavaScript")
exercise4 = Exercise("Goal Getter", "Python")
# Create 3, or more, cohorts.

cohort35 = Cohort("Cohort 35")
cohort36 = Cohort("Cohort 36")
cohort37 = Cohort("Cohort 37")

# Create 4, or more, students and assign them to one of the cohorts.

samSam = Student("Sam", "Pita", "SamTheSlice", "Cohort 36")
guyGuy = Student("Guy", "Cherkesky", "WhatA", "Cohort 36")
erEr = Student("Erin", "Polley", "ErIn", "Cohort 36")
treyTrey = Student("Trey", "Suitor", "HesASuitor", "Cohort 36")

# Create 3, or more, instructors and assign them to one of the cohorts.

jisie = Instructor("Jisie", "David", "jDavid", "all-around-badass")
joe = Instructor("Joe", "Shepard", "jShep", "the jokes")
jenna = Instructor("Jenna", "Solis", "jSol", "cat babies")
andy = Instructor("Andy", "Smith", "andEE", "scuba diving")
steve = Instructor("Steve", "Jenkins", "@steve", "poetry")   

cohort36.assign_instructor(jisie)
cohort36.assign_instructor(andy)
cohort35.assign_instructor(joe)
cohort36.assign_instructor(jenna) 
cohort37.assign_instructor(steve)

cohort36.list_instructors()
cohort37.list_instructors()
cohort35.list_instructors()

# Have each instructor assign 2 exercises to each of the students. 

jisie.assign_exercise(guyGuy, exercise1, exercise3)
jisie.assign_exercise(samSam, exercise4, exercise3)
joe.assign_exercise(erEr, exercise1, exercise2)
joe.assign_exercise(guyGuy, exercise1, exercise2)
jenna.assign_exercise(treyTrey, exercise2, exercise3)
jenna.assign_exercise(samSam, exercise2, exercise4)
andy.assign_exercise(treyTrey, exercise2, exercise3)
andy.assign_exercise(samSam, exercise2, exercise4)
steve.assign_exercise(treyTrey, exercise2, exercise3)
steve.assign_exercise(samSam, exercise2, exercise4)