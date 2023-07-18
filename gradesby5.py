arr = [73,67,38,33]
def gradingStudents(grades):
    res = []
    for x in grades:
        if x < 38:
            res.append(x)
        else:
            residuo = 5 - (x % 5)
            new_x = x + residuo
            if new_x - x < 3:
                res.append(new_x)
            else:
                res.append(x)
    return res

print(gradingStudents(arr))