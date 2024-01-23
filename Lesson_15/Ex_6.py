'''Create a tuple of student names and their corresponding scores. Write a function to find
the student with the highest score.'''


def max_student(students):
    result = ()
    k = (0, students[1][1] - 1)
    for i in students:
        if k[1] < i[1]:
            k = i
            result = i
    return result[0]
