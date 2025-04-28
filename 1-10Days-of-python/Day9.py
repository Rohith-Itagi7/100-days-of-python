# An example dictionary
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}
# Grading Program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
 
student_grades = {}
 

for student in student_scores:
    score = student_scores[student]

    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
 
 
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
print(travel_log["France"][1])

# Nesting Lists inside other Lists

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nesting a Dictionary inside a Dictionary
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}
print(travel_log["Germany"]["cities_visted"][2])