import sys, os
#sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import model.package_model.Databasex as Databasex
db = Databasex.Databasex()