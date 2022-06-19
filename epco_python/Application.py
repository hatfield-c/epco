
import CONFIG
import DataLoader
import Trainer
import Model
import Renderer

def main():
	
	dataLoader = DataLoader.DataLoader(CONFIG.train_path)
	model = Model.Model(CONFIG.sizes).cuda()
	trainer = Trainer.Trainer()
	
	trainer.Train(model, dataLoader)
	
	Renderer.Render(model)

main()