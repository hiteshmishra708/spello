import os
from spello.model import SpellCorrectionModel
sp = SpellCorrectionModel(language='en')
sp.load(os.getcwd() + '/examples/model.pkl')
print(sp.spell_correct('i wnt to ply futbal'))