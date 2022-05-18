# Complete the solve function below
if __name__ == '__main__':
    x = lambda a: a.upper()

    print(x("teste"))

    student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

    student['phone']= '555-5555'
    student.update({'name': 'Jane', 'age': 20})

    del student['age']
    print(student.get('phone','Not Found'))


    for item, value in student.items():
        print(item,value)



