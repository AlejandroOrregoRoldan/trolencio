import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble  import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv('penguins.csv')
df.dropna(inplace=True)
print(df.info())
print(df['island'].unique())

y= df['species']
x=df[['bill_length_mm','bill_depth_mm',
      'flipper_length_mm', 'body_mass_g',
       'island', 'sex']]

x= pd.get_dummies(x)
y, uniques = pd.factorize(y)

#modelo entrenado
x_train,x_text, y_train, y_text = train_test_split(x, y, test_size=0.8)
rfc=RandomForestClassifier(random_state=15)
rfc.fit(x_train,y_train)
y_pred=rfc.predict(x_text)
score=accuracy_score(y_pred, y_text)
print(score)

#llevarloo a strealit usando libreria pickle
rf_picke = open('random_forest_penguins.pickle','wb')
pickle.dump(rfc, rf_picke)
rf_picke.close()
output_pickle=open('output_penguins.pickle','wb')
pickle.dump(uniques, output_pickle)
output_pickle.close()