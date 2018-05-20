import numpy as np
#from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn import tree
#from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pickle


#def model_prediction(test_file_name):
#clf1 = LogisticRegression(random_state=1)
clf2 = RandomForestClassifier(random_state=1)
#clf3 = GaussianNB()
clf4 = tree.DecisionTreeClassifier()
#clf5 = MLPClassifier()

t= pd.read_csv("dataset_final.csv",usecols=["Pos_Score", "Neg_Score", "d_word_count", "Pro_Count", "Tone", "Tone_Score", "T_12<=4","depressed"])
train=t.drop(['depressed'], axis=1)
target = t['depressed'] 																																																													
#X_all= data.drop(['Criminal'], axis=1)
#y_all= data['Criminal']

#X_train, X_test, y_train, y_test = train_test_split(train,target, test_size=0.20, random_state=42)


#y = target
#X = train
#test = pd.read_csv(test_file_name,usecols=['positive','negative','d_count','p_count'])																							
#eclf1 = VotingClassifier(estimators=[
 #       ('lr', clf1), ('rf', clf2), ('gnb', clf3),('dct',clf4),('mlp',clf5)], voting='hard')
#eclf=[clf4]
#eclf=[clf1,clf2,clf3,clf4,clf5]
#for i in eclf:
model = clf2.fit(train,target)
#predicted= eclf1.predict(test)																																																																																																																																										
#sub2 = pd.DataFrame({'PERID':train.PERID, 'Depressed':predicted})
#sub2 = sub2[['PERID', 'Depressed']]
#sub2.to_csv(i+'.csv', index=False)
#accuracy = accuracy_score(y_test, predicted)
#print(accuracy)
#print(predicted)


filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))


#print('done')
#return(predicted)
#print(predicted)