import pandas as pd

def createDataframe(student_data) -> pd.DataFrame:
    columns = ["ID","Age"]
    df = pd.DataFrame(student_data,columns=columns)
    return df

student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

print(createDataframe(student_data))