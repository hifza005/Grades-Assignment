# assign grades to students based on their scores

# Sample scores for students
scores = [93, 84, 76, 64, 52, 44, 36]

for score in scores:
    if score >= 90:
        grade = 'A+'
    elif score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    elif score >= 40:
        grade = 'E'
    else:
        grade = 'F'
    
    print(f"Score: {score} - Grade: {grade}")