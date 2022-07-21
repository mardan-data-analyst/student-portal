# Here is 2 methods, First one is evaluate your mark

def gradeStudent(point):
    if point >= 90:
        return 'A'
    elif point >= 80 and point < 90:
        return 'B'
    elif point >= 70 and point < 80:
        return 'C'
    elif point <= 60 and point > 50:
        return 'D'
    else:
        return 'F'

#This method define either you have passed or not
def isPassed(letter):
    if letter == 'F':
        return False
    else:
        return True