import pandas as pd
import nltk
import re

file_name = 'C:/Users/satvi/Downloads/CSS5984_Project/Data/satvik_txt/Abigail McNally.txt'
file_name1 = 'C:/Users/satvi/Downloads/CSS5984_Project/Data/Abigail McNally.csv'
text = pd.read_csv(file_name1)

text1 = {}
text1['Sentences'] = list()
text1['Patient_Gender'] = list()
text1['Therapist_Gender'] = list()
for i in text['Column1']:
    if 'THERAPIST:' in i:
        j = i.replace('THERAPIST:','')
        j = j.strip()
        text1['Sentences'].append(j)
        text1['Patient_Gender'].append('Male')
        text1['Therapist_Gender'].append('Female')
        # print(i)
text2 = pd.DataFrame({'Sentences':text1['Sentences'], 'Patient_Gender':text1['Patient_Gender'], 'Therapist_Gender':text1['Therapist_Gender']})
print(text2)
text2.to_csv('C:/Users/satvi/Downloads/CSS5984_Project/Data/test.csv', sep=",", index=False)