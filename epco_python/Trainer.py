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
		loss_func = nn.BCELoss()
	
		self.TrainPhase(model, dataLoader, loss_func, CONFIG.epoch_list[0])
		
		#model.SetMode(CONFIG.model_mode_smooth)
		#self.TrainPhase(model, dataLoader, loss_func, CONFIG.epoch_list[1])
		
		#model.SetMode(CONFIG.model_mode_separator)
		#self.TrainPhase(model, dataLoader, loss_func, CONFIG.epoch_list[2])
	
	def TrainPhase(self, model, dataLoader, loss_func, epochs):	
		optimizer = optim.Adam(
			model.parameters(), 
			lr = CONFIG.learning_rate, 
			weight_decay = CONFIG.weight_decay
		)
		
		avgTime = 1
		start_total = time.time()
	
		canvas = Renderer.GetNewCanvas()
		canvas = Renderer.RenderPField(model, canvas)
		Renderer.SaveFrame(canvas)
	
		for e in range(epochs):
			
			if self.ShouldPrint_E(epochs, e):
				print("\nEpoch:", e)
			
			for b in range(CONFIG.epoch_size):
				start_b = time.time()
				
				batch_data, batch_targets = dataLoader.DrawSamples(CONFIG.batch_size)
				
				preds = model(batch_data)
				loss = loss_func(preds, batch_targets)
				optimizer.zero_grad()
				loss.backward()
				optimizer.step()
 
				self.PrintUpdate(epochs, e, b, avgTime, loss)
					
				if CONFIG.action == CONFIG.action_train_video:
					render_index = str(e) + "-" + str(b)
					
					canvas = Renderer.GetNewCanvas()
					canvas = Renderer.RenderPField(model, canvas)
					Renderer.SaveFrame(canvas, render_index)
					
				avgTime = (avgTime + (time.time() - start_b)) / 2

		print("\nCompleted in", int((time.time() - start_total) / 60), "minutes.")
		print("Final loss:", loss.item())
			
		return model
	
	def PrintUpdate(self, epochs, e, b, avgTime, loss):
		remaining_epochs = epochs - e - 1
		
		if self.ShouldPrint_B(epochs, b) and self.ShouldPrint_E(epochs, e):
			remaining_batches = (CONFIG.epoch_size - b - 1) + (remaining_epochs * CONFIG.epoch_size)
			eta = avgTime * remaining_batches
			eta = str(eta / 60)
			eta = eta
			
			completion = str(100 *(b / (CONFIG.epoch_size)))
			completion = completion[:4] + "%"
			
			print("   [", b, "/", CONFIG.epoch_size - 1, ":", completion,  "]")
			print("    Loss	 :", loss.item())
			print("")
			print("    Batches left :", remaining_batches)
			print("    Avg. Time    :", "{:.2f}".format(avgTime), "s")
			print("    ETA	      :", eta, "mins")
			print("\n")
	
	def ShouldPrint_E(self, epochs, e):
		if epochs < CONFIG.print_every_epoch:
			return True
		
		return e % CONFIG.print_every_epoch == 0 or e == CONFIG.epochs - 1
	
	def ShouldPrint_B(self, epochs, b):
		if epochs < CONFIG.print_every_batch:
			return True
		
		return b % CONFIG.print_every_batch == 0 or b == CONFIG.epoch_size - 1