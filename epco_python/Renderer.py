
import time
import cv2
import numpy as np
import torch

import CONFIG

def Render(model):
	start = time.time()
	
	img = np.zeros(shape = CONFIG.img_size)
	
	positions = []
	pixels = {}
	
	index = 0
	for i in range(CONFIG.img_size[0]):
		y = i * CONFIG.y_step
		
		for j in range(CONFIG.img_size[1]):
			x = j * CONFIG.x_step

			positions.append([x, y])
			pixels[index] = [i, j]

			index += 1

	positions = np.array(positions)
	positions = torch.from_numpy(positions).float().cuda()
	
	preds = model(positions)
	
	for index in range(preds.shape[0]):
		pred = preds[index]
		pixel_pos = pixels[index]
		
		pred = pred.cpu().item()
		
		if pred > 0.5:
			i = pixel_pos[0]
			j = pixel_pos[1]
			
			img[CONFIG.img_size[0] - i - 1, j] = 1
	
	cv2.imwrite(CONFIG.img_path, 255 * img)
	
	print("Render time:", time.time() - start)
	
	cv2.imshow('image', img)
	cv2.waitKey(0)