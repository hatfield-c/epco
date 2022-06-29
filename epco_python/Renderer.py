
import time
import cv2
import numpy as np
import torch

import CONFIG

def Render(model, render_index = None):
	start = time.time()
	
	img = np.zeros(shape = CONFIG.render_shape)
	
	positions = []
	pixels = {}
	max_val = -999999999
	min_val = 999999999
	avg_val = 0
	
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
		
		pred = pred[0].cpu().item()
		
		if pred > max_val:
			max_val = pred
			
		if pred < min_val:
			min_val = pred
		
		avg_val = (avg_val + pred) / 2
		
		pix_color = GetColor(pred)
		
		i = pixel_pos[0]
		j = pixel_pos[1]
		
		img[CONFIG.img_size[0] - i - 1, j] = pix_color
		
	path = CONFIG.img_path
	
	if render_index is not None:
		path = CONFIG.video_path + "_" + str(render_index) + ".png"
	
	if render_index is None:
		print("\nMax Pred:", max_val)
		print("Min Pred:", min_val)
		print("Avg Pred:", avg_val)
		print("Render time:", time.time() - start)
		
	cv2.imwrite(path, img)
	
def GetColor(val):
	
	if val <= CONFIG.render_bot_threshold:
		return CONFIG.render_bot_color
		
	if val >= CONFIG.render_top_threshold:
		return CONFIG.render_top_color
	
	lerp_top = None
	lerp_bot = None
	lerp_top_color = None
	lerp_bot_color = None
	
	if val >= CONFIG.render_high_threshold and val <= CONFIG.render_top_threshold:
		lerp_top = val - CONFIG.render_high_threshold
		lerp_bot = CONFIG.render_top_threshold - CONFIG.render_high_threshold
		
		lerp_top_color = CONFIG.render_top_color
		lerp_bot_color = CONFIG.render_high_color
	
	if val >= CONFIG.render_mid_threshold and val <= CONFIG.render_high_threshold:
		lerp_top = val - CONFIG.render_mid_threshold
		lerp_bot = CONFIG.render_high_threshold - CONFIG.render_mid_threshold
		
		lerp_top_color = CONFIG.render_high_color
		lerp_bot_color = CONFIG.render_mid_color
		
		
	
	if val >= CONFIG.render_low_threshold and val <= CONFIG.render_mid_threshold:
		lerp_top = val - CONFIG.render_low_threshold
		lerp_bot = CONFIG.render_mid_threshold - CONFIG.render_low_threshold
		
		lerp_top_color = CONFIG.render_mid_color
		lerp_bot_color = CONFIG.render_low_color
	
	if val >= CONFIG.render_bot_threshold and val <= CONFIG.render_low_threshold:
		lerp_top = val - CONFIG.render_bot_threshold
		lerp_bot = CONFIG.render_low_threshold - CONFIG.render_bot_threshold
		
		lerp_top_color = CONFIG.render_low_color
		lerp_bot_color = CONFIG.render_bot_color
	
	lerp = lerp_top / lerp_bot
	
	lerp_color = (lerp * lerp_top_color) + ((1 - lerp) * lerp_bot_color)
	lerp_color = lerp_color.astype("uint8")
	
	return lerp_color