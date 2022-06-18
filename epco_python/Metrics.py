
class Metrics:
	def __init__(self):
		pass
	
	def Accuracy(self, x, y, model):
		pred = model(x)
		
		total = pred.shape[0]
		error = 0
		
		for i in range(total):
			if pred[i][0] > 0 and y[i][0] == 1:
				continue
			
			if pred[i][0] > 0 and y[i][0] == 0:
				continue
			
			error += 1
			
		
		return (total - error) / total 