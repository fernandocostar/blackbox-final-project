from TrainedModels import vgg_model
from Solver import Solver

imgs = ['49081', '38678', '27758', '26446', '39566', '16585', '21329', '27980']

solver = Solver(vgg_model, imgs, '/Users/fernandocr/Documents/uff/tcc/images/')
print("cheguei no predict")
solver.predict('20037.png')
