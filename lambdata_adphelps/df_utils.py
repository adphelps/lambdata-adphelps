import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
from sklearn.model_selection import train_test_split

def plot_confusion_matrix(y_true, y_pred):
     labels = unique_labels(y_true)
     columns = [f'Predicted {label}' for label in labels]
     index = [f'Actual {label}' for label in labels]
     table = pd.DataFrame(confusion_matrix(y_true, y_pred),   columns=columns, index=index)
     return sns.heatmap(table, annot=True, fmt='d', cmap='viridis')

def train_val_test_split(df):
    temp, test = train_test_split(df, test_size=0.2, train_size=0.8, random_state=200)
    train, val = train_test_split(temp, test_size=0.2, train_size=0.8, random_state=200)
    return train, val, test

