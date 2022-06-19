
#import scipy.sparse as spa

import torch
import torch.nn as nn

#from torch.autograd import Variable
#from torch.nn.parameter import Parameter

#import Parameters

class Model(nn.Module):
	def __init__(self, sizes):
		super().__init__()
        
		self.depth = len(sizes) - 1
		self.sizes = sizes
		self.layers = []
		self.linear_layers = []
		
		for i in range(self.depth):
			size = self.sizes[i]
			next_size = self.sizes[i + 1]
			
			linear = torch.nn.Linear(size, next_size).cuda()
			
			activation = None
			if i == self.depth - 1:
				activation = torch.nn.Sigmoid()
			else:
				activation = torch.nn.ReLU()
			
			self.layers.append(linear)
			self.layers.append(activation)
			
			self.linear_layers.append(linear)

		self.moduleList = torch.nn.ModuleList(self.layers);

	def forward(self, data):
		result = data
		
		
		for i in range(len(self.layers)):
			layer = self.layers[i]
			
			result = layer(result)

		return result
	