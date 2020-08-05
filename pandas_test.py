import pandas as pd



data = pd.read_csv('/opt/Trycatch/otherprogram/test.csv')
# print(data)
# print(type(data))
# print(data.columns.values)
# print(data['Branch'])
# print(data[['Student Id', 'Chemistry','Physics']])
data = data.fillna(0)
# print(data)
data['Total']= data['Maths']+data['Physics']+data['Chemistry']
# print(data)
# print(data[data['Total']>200])
# more_than_80_in_maths_phy = data[(data['Maths']>80) & (data['Physics']>80)]
# print("ans",more_than_80_in_maths_phy)
# print(data[(data['Maths']>80) & (data['Physics']>80)][['Student Id','Total']])
# print(more_than_80_in_maths_phy[['Student Id','Total']])
# print(data['Student Id'].tolist())
# data = data.drop(['Physics','Maths'],axis=1)
# print(data['Total'].sum())
# print(data)
data['Chemistry_result']= data['Chemistry'].apply(lambda x:'Pass' if x>35 else 'Fail')
print(data)
data.to_csv('new_test.csv')
