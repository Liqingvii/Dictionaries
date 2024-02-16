student = {
    "name":"Liqing Yang",
    "age":22,
    "major":"Management Information System",
    "hobbies":['sleep','eat','study']
}
student['State'] = "Texas"
student['age'] += 1

for key in student:
    print(f'{key: <8}: {student[key]}')