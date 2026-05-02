#Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
def computegrade(score):
    print('Enter score: ', score)
    try:
        grade = 'F'
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
        print(grade)
    except:
        print('Bad score')

computegrade(0.95)
computegrade('perfect')
computegrade(10.0)
computegrade(0.75)
computegrade(0.5)