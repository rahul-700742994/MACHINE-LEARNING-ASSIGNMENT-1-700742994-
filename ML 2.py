# QUESTION2
print("solution 2")
dog = {}
print(dog)
dog['name'] = 'denver'
dog['color'] = 'black'
dog['breed'] = 'labrador retriever'
dog['legs'] = 4
dog['age'] = 'one year'
print("dog_dictionary=", dog)
student = {'first_name': 'rahul', 'last_name': 'aleti', 'gender': 'male', 'age': '22', 'maratial status': 'single',
           'skills': ['leadership', 'team work'], 'country': 'USA', 'city': 'NEW YORK', 'address': '7401 W 104'}
print("student_dictionary=", student)
print("the length of the student dictionary is: ", len(student))
student.get('skills')
student['skills'] = ['computer proficiency', 'communication skills']
print("student dictionary with updated skills is student=", student)
print(type(student["skills"]))
keyslist = list(student.keys())
print("student keys as list: ", keyslist)
valueslist = list(student.values())
print("student values as list: ", valueslist)