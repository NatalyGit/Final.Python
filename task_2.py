# Задание2. Анализ расходов повозрасту. 
# Постройте линейный график, где по оси X будет отображаться возраст (age), а по оси Y —баллпорасходам (spending_score). 
# Этот график поможет визуализировать, как изменяются расходы в зависимости от возраста сотрудников. 
# Проанализируйте тренды и выявите возможные закономерности.

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
df = pd.read_csv('data.csv')
print(df.columns) 
sns.lineplot(x='age', y='spending_score', data=df) 
plt.title('Age vs Spending Score') 
plt.xlabel('Age') 
plt.ylabel('Spending Score') 
plt.show()

