
import numpy as np
import random

class DataLoader:
	def __init__(self, path):
		self.path = path
		
		data = np.loadtxt(self.path, delimiter = ',')
		
		self.x = data[:,:-1]
		self.y = data[:,-1]
		
		self.sampleCount = self.x.shape[0]
	
	def DrawSamples(self, sample_count):
		all_indices = range(self.sampleCount)
		chosen_indices = random.sample(all_indices, sample_count)
		
		chosen_x = self.x[chosen_indices]
		chosen_y = self.y[chosen_indices]
		
		return (chosen_x, chosen_y)
	
loader = DataLoader("train.txt")

(chosen_x, chosen_y) = loader.DrawSamples(3)
print(chosen_x)
print(chosen_y)