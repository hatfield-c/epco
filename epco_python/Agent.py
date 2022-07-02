import torch
from torch.autograd.functional import hessian

import numpy as np

class Agent:
	def __int__(self):
		pass
	
	def GetPoints(self, model):
		points = []
		
		origin = np.array([2.5, 3.9])
		
		#q = np.array([3.9, 4.1])
		q_0 = np.array(origin)
		q = np.array(origin)
		
		#return [ q ]
		
		q = torch.from_numpy(q).float().cuda()
		q.requires_grad = True
		
		q_0 = torch.from_numpy(q_0).float().cuda()
		q_0.requires_grad = False
		
		for i in range(5000):
			
			q = q.detach()
			
			#q1 = q + (4 * torch.rand([2]).float().cuda() - 1)
			#q2 = q + (4 * torch.rand([2]).float().cuda() - 1)
			#q3 = q + (4 * torch.rand([2]).float().cuda() - 1)
			#q4 = q + (4 * torch.rand([2]).float().cuda() - 1)
			
			#q1 = q1.detach()
			#q2 = q2.detach()
			#q3 = q3.detach()
			#q4 = q4.detach()
			
			q.requires_grad = True
			
			#q1.requires_grad = True
			#q2.requires_grad = True
			#q3.requires_grad = True
			#q4.requires_grad = True
			
			m = model(q)
			#m1 = model(q1)
			#m2 = model(q2)
			#m3 = model(q3)
			#m4 = model(q4)
			
			#d = q - q_0
			f = (0.5 * (m * m)) #+ (0.5 * d.dot(d))
			
			#f1 = (0.5 * (m1 * m1))
			#f2 = (0.5 * (m2 * m2))
			#f3 = (0.5 * (m3 * m3))
			#f4 = (0.5 * (m4 * m4))
			
			f.backward()
			
			#f1.backward()
			#f2.backward()
			#f3.backward()
			#f4.backward()
			
			di = torch.nn.functional.normalize(q.grad, dim = 0)
			
			#di1 = torch.nn.functional.normalize(q1.grad, dim = 0)
			#di2 = torch.nn.functional.normalize(q2.grad, dim = 0)
			#di3 = torch.nn.functional.normalize(q3.grad, dim = 0)
			#di4 = torch.nn.functional.normalize(q4.grad, dim = 0)
			
			di = di.detach()
			
			#di1 = di.detach()
			#di2 = di.detach()
			#di3 = di.detach()
			#di4 = di.detach()
			
			#direction[0] = 1
			#direction[1] = 0
			
			#avg = (di + di1 + di2 + di3 + di4) / 5
			
			qi = q - (0.01 * di)

			#print(qi)

			#print(q, q1, q2, q2, q4)
			#print(di, di1, di2, di3, di4)
			#print(qi)
			
			if i % 100 == 0:
				print(q.grad, di, q)
				
			q = qi
				
			points.append(q)
			
			#if q.grad is not None:
			#	q.grad.zero_()
			
		#exit()
		
		q_t = np.array(origin)
		q_t = torch.from_numpy(q_t).float().cuda()
		q_t.requires_grad = True
		test = model(q_t)
		
		t = 0.5 * test * test
		t.backward()
		
		dit = torch.nn.functional.normalize(q_t.grad, dim = 0)
		print("")
		print(q_0)
		print(q)
		print(dit)
		
		return points