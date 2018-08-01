import pandas as pd
import numpy as np
import tensorflow as tf

california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")

feature_columns = [tf.feature_column.numeric_column("total_rooms")]
print feature_columns
