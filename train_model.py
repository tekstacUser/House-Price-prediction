import pandas as pd, joblib
from xgboost import XGBRegressor

df=pd.read_csv('housing.csv')
X=df[['bedrooms','bathrooms','area_sqft']]
y=df['price']
model=XGBRegressor()
model.fit(X,y)
joblib.dump(model,'xgb_house_price_model.pkl')
print('saved')
