import pandas as pd

import pickle

def pred(test_file_name):
	print("inside predict")
	t= pd.read_csv(test_file_name,usecols=["Pos_Score", "Neg_Score", "d_word_count", "Pro_Count", "Tone", "Tone_Score", "T_12<=4"])
	X_test=t 

	# load the model from disk
	loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
	result = loaded_model.predict(X_test)
	print(result)

	if result==0:
		result2="not depressed"
	else:
		result2="depressed" 
	
	m=X_test
	l1=[]
	l1.append(result2)
	l1.append(m)
	return(l1)
	
	print(result2)
	return(result2)
