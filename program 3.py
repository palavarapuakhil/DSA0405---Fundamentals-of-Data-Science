import pandas as pd
import numpy as np
np.random.seed(42)

num_students = 100

courses = ['Math', 'Physics', 'History', 'Biology']

data = {
    'Student_ID': np.arange(1, num_students + 1),
    'Course': np.random.choice(courses, num_students),
    'Score': np.random.randint(50, 100, num_students),
    'Hours_Studied': np.random.uniform(5, 30, num_students)
}
student_data = pd.DataFrame(data)

print(student_data.head())
