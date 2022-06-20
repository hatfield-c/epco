import time

import torch.nn as nn
import torch.optim as optim

import CONFIG
import Metrics
import Renderer

class Trainer:
	def __init__(self):
		pass
	
	def Train(self, model, dataLoader):
		orig_x, orig_y = dataLoader.GetData()
		
		optimizer = optim.Adam(model.parameters(), lr = CONFIG.learning_rate)
		metrics = Metrics.Metrics()
		
		avgTime = 1
		start_total = time.time()
	
		Renderer.Render(model, "start")
	
		for e in range(CONFIG.epochs):
			remaining_epochs = CONFIG.epochs - e - 1
			
			if self.shouldPrint_e(e):
				print("\nEpoch:", e)
			
			for b in range(CONFIG.epoch_size):
				start_b = time.time()
				
				batch_data, batch_targets = dataLoader.DrawSamples(CONFIG.batch_size)
				
				preds = model(batch_data)
				loss = nn.BCELoss()(preds, batch_targets)
				optimizer.zero_grad()
				loss.backward()
				optimizer.step()
	
				if self.shouldPrint_b(b) and self.shouldPrint_e(e):
					remaining_batches = (CONFIG.epoch_size - b - 1) + (remaining_epochs * CONFIG.epoch_size)
					eta = avgTime * remaining_batches
					eta = str(eta / 60)
					eta = eta
					
					completion = str(100 *(b / (CONFIG.epoch_size)))
					completion = completion[:4] + "%"
					
					print("   [", b, "/", CONFIG.epoch_size - 1, ":", completion,  "]")
					print("    Loss	 :", loss.item())
					#print("    Accuracy :", metrics.Accuracy(orig_x, orig_y, model))
					print("")
					print("    Batches left :", remaining_batches)
					print("    Avg. Time    :", "{:.2f}".format(avgTime), "s")
					print("    ETA	      :", eta, "mins")
					print("\n")
					
				Renderer.Render(model, str(e) + "-" + str(b))
					
				avgTime = (avgTime + (time.time() - start_b)) / 2
				
			
				
		print("\nCompleted in", int((time.time() - start_total) / 60), "minutes.")
		print("Final loss:", loss.item())
			
		return model
	
	def shouldPrint_e(self, e):
		if CONFIG.epochs < CONFIG.print_every_epoch:
			return True
		
		return e % CONFIG.print_every_epoch == 0 or e == CONFIG.epochs - 1
	
	def shouldPrint_b(self, b):
		if CONFIG.epoch_size < CONFIG.print_every_batch:
			return True
		
		return b % CONFIG.print_every_batch == 0 or b == CONFIG.epoch_size - 1