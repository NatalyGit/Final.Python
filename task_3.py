# Задание 3. Взаимосвязь между зарплатой и бонусами 
# Создайте точечный график, где по оси X будет отображаться зарплата (salary), а по оси Y —бонусы (bonus). 
# Размер точек на графике должен быть пропорционален количеству лет в компании (years_at_company). 
# Этот график позволит исследовать взаимосвязь между зарплатой и бонусами и оценить влияние стажа на размер бонусов.

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplotasplt 
df=pd.read_csv('data.csv') 
sns.scatterplot(x='salary',y='bonus',size='years_at_company', data=df) 
plt.title('SalaryvsBonuswithYearsatCompany') 
plt.xlabel('Salary') 
plt.ylabel('Bonus') 
plt.show()
