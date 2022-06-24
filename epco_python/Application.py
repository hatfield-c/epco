
import CONFIG
import DataLoader
import Trainer
import Model
import Renderer
import EpcoManager

def main():
	
	if CONFIG.action == CONFIG.action_train_render:
		dataLoader = DataLoader.DataLoader(CONFIG.train_path)
		model = Model.Model(CONFIG.sizes).cuda()
		trainer = Trainer.Trainer()
		
		trainer.Train(model, dataLoader)
			
		Renderer.Render(model)
		
	if CONFIG.action == CONFIG.action_inference:
		epco = EpcoManager.EpcoManager(CONFIG.tcp_timeout)
		epco.inference()

main()