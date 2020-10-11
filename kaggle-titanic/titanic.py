import pandas as pd
import numpy as np

train_dir = './data/train.csv'
test_dir = './data/test.csv' 

train_data = pd.read_csv(train_dir)
test_data = pd.read_csv(test_dir)
