import os, csv
from spello.model import SpellCorrectionModel
sp = SpellCorrectionModel(language='en')
sp.train(['what is encapsulation', 'what is java', 'abvantage of java', 'why python', 'i want to play football'])
sp.save(model_save_dir=os.getcwd() + '/examples')