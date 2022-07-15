
import CONFIG
import SeparatorData
import Trainer
import Model
import Renderer
import EpcoManager
import Agent

import torch

def main():
	
	if CONFIG.action == CONFIG.action_playground:
		model = Model.Model(CONFIG.sizes, True).cuda()
		model.load_state_dict(torch.load(CONFIG.model_save_path))
		model.eval()
		
		agent = Agent.Agent()
		points = agent.GetPoints(model)
		
		canvas = Renderer.GetNewCanvas()
		canvas = Renderer.RenderPField(model, canvas)
		canvas = Renderer.RenderPoints(points, canvas)
		Renderer.SaveFrame(canvas)
	
	if CONFIG.action == CONFIG.action_train_save or CONFIG.action == CONFIG.action_train_video:
		dataLoader = SeparatorData.SeparatorData(CONFIG.train_path)
		model = Model.Model(CONFIG.sizes).cuda()
		trainer = Trainer.Trainer()
		
		trainer.Train(model, dataLoader)
		
		torch.save(model.state_dict(), CONFIG.model_save_path)
	
	if CONFIG.action == CONFIG.action_train_render:
		dataLoader = SeparatorData.SeparatorData(CONFIG.train_path)
		model = Model.Model(CONFIG.sizes).cuda()
		trainer = Trainer.Trainer()
		
		trainer.Train(model, dataLoader)
		
		canvas = Renderer.GetNewCanvas()
		canvas = Renderer.RenderPField(model, canvas)
		Renderer.SaveFrame(canvas)
		
	if CONFIG.action == CONFIG.action_load_render:
		model = Model.Model(CONFIG.sizes, False).cuda()
		model.load_state_dict(torch.load(CONFIG.model_save_path))
		model.eval()
		
		canvas = Renderer.GetNewCanvas()
		canvas = Renderer.RenderPField(model, canvas)
		Renderer.SaveFrame(canvas)
		
	if CONFIG.action == CONFIG.action_inference:
		epco = EpcoManager.EpcoManager(CONFIG.tcp_timeout)
		epco.inference()

main()