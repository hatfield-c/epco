import torch
import torch.nn as nn
import numpy as np

import CONFIG

class Model(nn.Module):
	def __init__(self, sizes, isTraining = True):
		super().__init__()
        
		self.depth = len(sizes) - 1
		self.sizes = sizes
		self.layers = []
		self.linear_layers = []
		self.isTraining = isTraining
		
		self.i = 0
		
		for i in range(self.depth):
			size = self.sizes[i]
			next_size = self.sizes[i + 1]
			
			linear = torch.nn.Linear(size, next_size).cuda()
			linear = torch.nn.utils.weight_norm(linear)
			
			#linear.weight_g.requires_grad = False
			
			#for j in range(linear.weight_g.shape[0]):
			#	linear.weight_g[j] = 1
			
			activation = None
			if i == self.depth - 1:
				activation = torch.nn.Sigmoid()
			else:
				activation = torch.nn.ReLU()
			
			self.layers.append(linear)
			self.layers.append(activation)
			
			self.linear_layers.append(linear)

		self.moduleList = torch.nn.ModuleList(self.layers);
		
		self.model_mode = CONFIG.model_mode_separator
		
		#for p in self._parameters:
			#print(p)
		#print(self.linear_layers[0].weight_g)
		#exit()

	def forward(self, data):
		result = data
		
		forward_depth = len(self.layers)

		if not self.isTraining:
			forward_depth = forward_depth - 1
			
		for i in range(forward_depth):
			layer = self.layers[i]
			
			result = layer(result)

		return result

	def SetMode(self, mode):
		self.model_mode = mode

	def PrintWeightMagnitudes(self):
		for i in range(len(self.linear_layers)):
			layer = self.linear_layers[i]
			
			for j in range(layer.weight.shape[0]):
				val = torch.norm(layer.weight[0])
				val = val.cpu().item()
				val = str(val)[:5]
				
				print(val, "", end = "")
			
		print("\n")
			
