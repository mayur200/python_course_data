import pandas as pd 

data = pd.read_csv('Berkeley.csv')
# print(data)

accepted_male_dept_A = data[(data['Admit']== 'Admitted') & (data['Gender'] == 'Male') & (data['Dept'] == 'A')]
accepted_female_dept_A = data[(data['Admit']== 'Admitted') & (data['Gender'] == 'Female') & (data['Dept'] == 'A')]
accepted_male_freq_g8_300 = data[(data['Admit']== 'Admitted') & (data['Gender'] == 'Male') & (data['Freq'] > 300)]
accepted_female_freq_g8_100 = data[(data['Admit']== 'Admitted') & (data['Gender'] == 'Female') & (data['Freq'] > 100)]
rejected_male_dept_E = data[(data['Admit']== 'Rejected') & (data['Gender'] == 'Male') & (data['Dept'] == 'E')]
rejected_female_dept_C = data[(data['Admit']== 'Rejected') & (data['Gender'] == 'Male') & (data['Dept'] == 'C')]
rejected_female_freq_g8_100 = data[(data['Admit']== 'Rejected') & (data['Gender'] == 'Female') & (data['Freq'] > 100)]


#percentage of female accepted department B of total accepted female
accepted_female_dept_B = data[(data['Admit']== 'Admitted') & (data['Gender'] == 'Female') & (data['Dept'] == 'B')]
total_accepted_female = data[(data['Admit'] == 'Admitted') & (data['Gender']=='Female')]
list_accpted_female= total_accepted_female['Gender'].tolist()
list_acceptd_female_dept_B = accepted_female_dept_B['Gender'].tolist()
count_accepted_female = len(list_accpted_female)
count_accepted_female_dept_B = len(list_acceptd_female_dept_B)
percentage_accepted_female_dept_B_from_all_accepted_female = (count_accepted_female_dept_B*100)/count_accepted_female
print(percentage_accepted_female_dept_B_from_all_accepted_female,'%')

#percentage of  rejected admit of female from all the admitt
reject_admit_female = data[(data['Admit']=='Rejected') & (data['Gender']=='Female')]
list_reject_admit_female = reject_admit_female['Admit'].tolist()
len_of_total_admint = len(list_reject_admit_female)
list_all_data = data['Admit'].tolist()
len_of_all_data = len(list_all_data)
percentage_reject_admit_female = (len_of_total_admint*100)/len_of_all_data
print(percentage_reject_admit_female,'%')


