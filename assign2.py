from operator import le
import pandas as pd
info={'Gender':['Male','Female','Male','Female','Female'],'position':['Head','Asst,prof','Head','Asst.prof','Head']}
df=pd.DataFrame(info)
print(df)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
gender_encoded=le.fit_transform(df['Gender'])
encoded_position=le.fit-transform(df['Position'])
df['Encoded_Gender']=gender_encoded
df['Encoded_position']=encoded_position
print(df)