
import torch
import numpy as np
import random

import CONFIG

class SmoothingData:
	def __init__(self, model):
		self.model = model
	
	def DrawSamples(self, sample_count):
		point_list = []
		queries = []
		samples = []
		
		for i in range(5 * sample_count):
			x1 = random.uniform(CONFIG.x_domain[0], CONFIG.x_domain[1])
			x2 = random.uniform(CONFIG.y_domain[0], CONFIG.y_domain[1])
			
			point_list.append([x1, x2])
			
		points = torch.tensor(point_list).cuda()
		results = self.model(points).cpu()
		
		for i in range(5 * sample_count):
			if len(queries) > sample_count:
				break
			
			position = results[i, :-1]
			distance = results[i, -1]
			
			if distance > 0:
				queries.append(position)
				
		
		
		return ("x", "y")

	def GetData(self):
		return self.torch_data

	def Count(self):
		return self.x.shape[0]