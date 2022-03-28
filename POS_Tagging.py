import spacy
import pandas as pd
nlp = spacy.load("en_core_web_sm")
file_name = 'C:/Users/satvi/Downloads/CSS5984_Project/Data/test.csv'
df = pd.read_csv(file_name)

# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

text = {}
text['Word'] = list()
text['Lemma'] = list()
text['POS'] = list()
text['Patient_Gender'] = list()
text['Therapist_Gender'] = list()
for index, row in df.iterrows():
    doc = nlp(row['Sentences'])
    for token in doc:
        if token.pos_ == 'ADJ' or token.pos_ == 'VERB':
            # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            #   token.shape_, token.is_alpha, token.is_stop)
            text['Word'].append(token.text)
            text['Lemma'].append(token.lemma_)
            text['POS'].append(token.pos_)
            text['Patient_Gender'].append(row['Patient_Gender'])
            text['Therapist_Gender'].append(row['Therapist_Gender'])
text1 = pd.DataFrame({'Word':text['Word'], 'Lemma':text['Lemma'], 'POS':text['POS'], 'Patient_Gender':text['Patient_Gender'], 'Therapist_Gender':text['Therapist_Gender']})
text1.to_csv('C:/Users/satvi/Downloads/CSS5984_Project/Data/test_pos1.csv', sep=",", index=False)