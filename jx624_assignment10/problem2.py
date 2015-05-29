import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
random.seed(500)
names = ['Bob','Jessica','Mary','John','Mel']


random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]
births = [random.randint(low=0,high=1000) for i in range(1000)]
BabyDataSet = zip(random_names,births)
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births']).groupby('Names').sum()
df.sort(['Births'], ascending=False,inplace=True)
df.plot(kind='bar',legend=False)
plt.show()