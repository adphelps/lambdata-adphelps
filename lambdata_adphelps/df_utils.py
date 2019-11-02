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

class Animal:
	def __init__(self, age):
		self.age = age
	
	def __repr__(self):
		return f'Animal(age={self.age})'
	
	def __str__(self):
		return f"This is an animal that's {self.age} years old"
	
	def age_next_year(self):
		return self.age + 1
	
	def add_one_year(self):
		self.age = self.age + 1
	
	def get_weight(self):
		self.weight = 10


class Dog(Animal):
	def __init__(self, age, weight):
		super().__init__(age)
		self.weight = weight

	num_legs = 4
    
	def bark(self):
		print('woof woof!')
        
	def is_puppy(self):
		if self.age <=1:
			return True
		else:
			return False
					
	def eat(self):
		self.last_time_fed = datetime.datetime.now()
		self.weight = 1.01*self.weight
    
	def get_time_last_fed(self):
		time_sec_since_last_time_fed = (datetime.datetime.now() - self.last_time_fed).total_seconds()
		return time_sec_since_last_time_fed
    
	def is_hungry(self):
		if self.get_time_last_fed() > 10:
			return True
		else:
			return False
        
	def __repr__(self):
		return f'Dog(age={self.age})'
    
	def __str__(self):
		return f"This is a dog that's {self.age} years old"
    
	def __eq__(self, other):
		return (self.age == other.age) and (self.weight == other.weight)
    
	def __lt__(self, other):
		return self.age < other.age

class Cat(Animal):
	def __init__(self, age, weight):
		super().__init__(age)
		self.weight = weight
	
	def meow(self):
		print('meow!')

	def is_kitten(self):
		if self.age < 1:
			return True
		else:
			return False

	def eat(self):
		self.last_time_fed = datetime.datetime.now()
		self.weight = 1.01*self.weight
    
	def get_time_last_fed(self):
		time_sec_since_last_time_fed = (datetime.datetime.now() - self.last_time_fed).total_seconds()
		return time_sec_since_last_time_fed
    
	def is_hungry(self):
		if self.get_time_last_fed() > 10:
			return True
		else:
			return False
        
	def __repr__(self):
		return f'Cat(age={self.age})'
    
	def __str__(self):
		return f"This is a cat that's {self.age} years old"
    
	def __eq__(self, other):
		return (self.age == other.age) and (self.weight == other.weight)
    
	def __lt__(self, other):
		return self.age < other.age