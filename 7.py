def map_function(student_scores):
    """
    Emits tuples of student_id and score.
    """
    mapped_data = []
    for student_id, score in student_scores:
        mapped_data.append((student_id, score))
    return mapped_data

def reduce_function(mapped_data):
    """
    Assigns grades based on scores.
    """
    grades = {}
    for student_id, score in mapped_data:
        if score > 80:
            grade = 'A'
        elif score > 60:
            grade = 'B'
        elif score > 40:
            grade = 'C'
        else:
            grade = 'D'
        grades[student_id] = grade
    return grades

def map_reduce(student_scores):
    """
    Simulates the MapReduce process for assigning grades to students based on scores.
    """
    mapped_data = map_function(student_scores)

    return reduce_function(mapped_data)

student_scores = [
    (1, 85),
    (2, 75),
    (3, 55),
    (4, 35),
    (5, 90)
]

grades = map_reduce(student_scores)

for student_id, grade in grades.items():
    print(f"Student {student_id} has been assigned grade {grade}.")
