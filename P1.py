import numpy as np
student_scores = np.array([
    [85, 78, 92, 74],
    [88, 82, 79, 90],
    [76, 85, 88, 80],
    [90, 88, 84, 86]
])
subject_averages = np.mean(student_scores, axis=0)
subjects = ['Math', 'Science', 'English', 'History']
highest_average_subject = subjects[np.argmax(subject_averages)]
print("Average score for each subject:", subject_averages)
print("Subject with the highest average score:", highest_average_subject)
