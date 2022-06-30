
import CONFIG
import DataLoader
import Trainer
import Model
import Renderer
import EpcoManager

import torch

def main():
	
	if CONFIG.action == CONFIG.action_train_save or CONFIG.action == CONFIG.action_train_video:
		dataLoader = DataLoader.DataLoader(CONFIG.train_path)
		model = Model.Model(CONFIG.sizes).cuda()
		trainer = Trainer.Trainer()
		
		model = trainer.Train(model, dataLoader)
		
		torch.save(model.state_dict(), CONFIG.model_save_path)
	
	if CONFIG.action == CONFIG.action_train_render:
		dataLoader = DataLoader.DataLoader(CONFIG.train_path)
		model = Model.Model(CONFIG.sizes).cuda()
		trainer = Trainer.Trainer()
		
		trainer.Train(model, dataLoader)
			
		Renderer.Render(model)
		
	if CONFIG.action == CONFIG.action_load_render:
		model = Model.Model(CONFIG.sizes, False).cuda()
		model.load_state_dict(torch.load(CONFIG.model_save_path))
		model.eval()
		
		Renderer.Render(model)
		
	if CONFIG.action == CONFIG.action_inference:
		epco = EpcoManager.EpcoManager(CONFIG.tcp_timeout)
		epco.inference()

main()