import warnings
### 去除煩人的 warrning
warnings.filterwarnings('ignore')

import pandas as pd

### 讀入series
df = pd.read_csv('Stocker/price.csv', index_col='date', parse_dates=['date'])
price = df.squeeze()
price.head()
print(df)
print(df.squeeze)

from Stocker.stocker import Stocker
tsmc = Stocker(price)
model, model_data = tsmc.create_prophet_model(days=90)
tsmc.evaluate_prediction()
tsmc.changepoint_prior_analysis(changepoint_priors=[0.001, 0.05, 0.1, 0.2])
tsmc.predict_future(days=100)