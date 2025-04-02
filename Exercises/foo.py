
def foo(x):
    return f"And FOO you too, {x}"

#%%
import pandas as pd

# Replace with the path to your CSV file
file_path = "/Users/feiz/Dropbox/feiz_dropbox/UCR/courses/stat207/students/2025-04-01T1505_Grades-STAT_207_001_25S.csv"

# Load the CSV into a DataFrame
df = pd.read_csv(file_path)

# Print the available columns so you can identify which column has student names
print("Columns in the CSV:", df.columns)
print(df['Student'])

# %%
# Shuffle the rows of the DataFrame randomly
df_shuffled = df.sample(frac=1).reset_index(drop=True)

# Print the shuffled DataFrame (random order of students)
print("Random order of students:")
print(df_shuffled)

# Optional: if you only need a list of student names (assuming the column is named 'Student')
# student_list = df_shuffled['Student'].tolist()
# print("Random order of student names:")
# print(student_list)

# %%
import random

# Define the list of students
students = [
    "FallahiFard, Behzad",
    "Galicia Lona, Axel",
    "Jones, Nathalie",
    "Lee, Wonkeun",
    "Li, Chuanman",
    "Lin, Pei-Ling",
    "Lin, Ying",
    "Liu, Linlin",
    "Liu, Yuxin",
    "Lopez, Nancy",
    "Olawole, Alice",
    "Qu, Xinhao",
    "Tang, Luhan",
    "Wang, Kaiming",
    "Wu, Yifan",
    "Xue, Yijia",
    "Yang, Chenguang",
    "Zhou, Bufan"
]

# Shuffle the list randomly
random.shuffle(students)
# Print out the random order
print("Random order of students:")
for index, student in enumerate(students, start=1):
    print(f"{index}: {student}")
# %%

# Format each student name with markdown bold and join them with a comma and a space
formatted_students = ", ".join(f"**{student}**" for student in students)

# Print the result
print(formatted_students)
# %%
