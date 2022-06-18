
import torch
import numpy as np
import random

class DataLoader:
	def __init__(self, path):
		self.path = path
		
		data = np.loadtxt(self.path, delimiter = ',')
		
		self.x = data[:,:-1]
		
		# SLICING!!! REMOVE AFTER DEMO
		self.x =self.x[:, [0, 2]]
		
		self.y = data[:,-1]
		self.y = self.y.reshape(
			(
				self.y.shape[0],
				1
			)
		)
		
		self.sampleCount = self.x.shape[0]
	
	def DrawSamples(self, sample_count):
		all_indices = range(self.sampleCount)
		chosen_indices = random.sample(all_indices, sample_count)
		
		chosen_x = self.x[chosen_indices]
		
		chosen_y = self.y[chosen_indices]
		
		chosen_x = torch.from_numpy(chosen_x).float().cuda()
		chosen_y = torch.from_numpy(chosen_y).float().cuda()
		
		return (chosen_x, chosen_y)

	def GetData(self):
		x = torch.from_numpy(self.x).float().cuda()
		y = torch.from_numpy(self.y).float().cuda()
		
		return (x, y)

	def Count(self):
		return self.x.shape[0]