print("Hello world")

from src.graph_io import *
import os

cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('../graphs/examplegraph.gr', cur_path)
with open(new_path, 'r') as f:
    _graph = load_graph (f)
    print(_graph)
