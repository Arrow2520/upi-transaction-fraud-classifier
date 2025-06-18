import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sn
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
import pydotplus as pdot
from supr import KNNbasic


pmf_df = pd.DataFrame({'success': range(0, 30),
                       'pmf': list(stats.poisson.pmf(range(0, 30), 10))})

plt.bar(pmf_df.success, pmf_df.pmf)
plt.xticks(list(range(0, 30)))
plt.ylabel('pmf')
plt.xlabel('Number of calls received')
plt.title('Poisson Distribution (λ = 10)')
plt.show()



