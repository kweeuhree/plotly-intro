import pandas as pd
import numpy as np
import cufflinks as cf
import chart_studio.plotly as py
import seaborn as sns
import plotly.express as px


# create numpy array with random values
arr_1 = np.random.rand(50,4) # 50 values with 4 columns
# define a dataframe
df_1 = pd.DataFrame(arr_1, columns=['A', 'B', 'C', 'D'])
df_1.head() # show first five items

# compare old plots
df_1.plot()

## line plots

