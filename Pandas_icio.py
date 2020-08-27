# %%
import pandas as pd 
import numpy as np
import os
# %% 
current_dir=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_dir,r"C:\Users\jonay\OneDrive\Escritorio\Aythami\ICIO\OUTPUT_2015.csv")
X=pd.read_csv(filename,delimiter=';', decimal='.')

current_dir=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_dir,r"C:\Users\jonay\OneDrive\Escritorio\Aythami\ICIO\TAXSUB_2015.csv")
TAXSUB=pd.read_csv(filename, delimiter=';', decimal='.')

current_dir=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_dir,r"C:\Users\jonay\OneDrive\Escritorio\Aythami\ICIO\VA_2015.csv")
VA=pd.read_csv(filename, delimiter=';', decimal='.')

current_dir=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_dir,r"C:\Users\jonay\OneDrive\Escritorio\Aythami\ICIO\Y_2015.csv")
Y=pd.read_csv(filename,delimiter=';', decimal='.')

current_dir=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_dir,r"C:\Users\jonay\OneDrive\Escritorio\Aythami\ICIO\Z.csv")
Z=pd.read_csv(filename)

# %%
Z=Z.set_index('index')
Y=Y.set_index('Rows')
TAXSUB=TAXSUB.set_index('Rows')
X=X.set_index('Unnamed: 0')
VA=VA.set_index('Unnamed: 0')
# %%
PROD_VASH=VA['VALU']/X['OUTPUT']

# %%

# %%
