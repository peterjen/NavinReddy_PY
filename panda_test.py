import pandas as pd
df = pd.read_csv("C:\MyPython\PANDA_Corey_Tutorial\data\survey_results_public.csv")
schema_df = pd.read_csv("C:\MyPython\PANDA_Corey_Tutorial\data\survey_results_schema.csv",index_col = 'Column')
# print(df.head(10))
# print(df["Hobbyist"])
# print(df["Hobbyist"].value_counts())

# print(schema_df)
print(schema_df.loc['MgrIdiot','QuestionText'])


