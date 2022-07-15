
import torch
import numpy as np
import random

import CONFIG

class SeparatorData:
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
		self.y = ((1 - (2 * CONFIG.label_smooth)) * self.y) + CONFIG.label_smooth

		self.sampleCount = self.x.shape[0]
		
		self.x_torch = torch.from_numpy(self.x).float().cuda()
		self.y_torch = torch.from_numpy(self.y).float().cuda()
		self.torch_data = (self.x_torch, self.y_torch)
	
		self.all_indices = range(self.Count())
	
	def DrawSamples(self, sample_count):
		chosen_indices = random.sample(self.all_indices, sample_count)
		
		chosen_x = self.x_torch[chosen_indices]		
		chosen_y = self.y_torch[chosen_indices]
		
		return (chosen_x, chosen_y)

	def GetData(self):
		return self.torch_data

	def Count(self):
		return self.x.shape[0]