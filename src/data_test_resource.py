import data
import data.one
from data import two
import os

data_dir = os.path.join(os.path.dirname(__file__), 'tests', 'data')
data_path = os.path.join(data_dir, 'message.eml')
with open(data_path, encoding='utf-8') as fp:
    eml = fp.read()