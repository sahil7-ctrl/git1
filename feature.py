import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Sahil"],
    "Marks": [85, 90, 95]
}

df = pd.DataFrame(data)

print("Student Data Analysis")
print(df)

print("Average Marks:", df["Marks"].mean())
