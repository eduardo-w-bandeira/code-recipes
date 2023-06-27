'''Here's how to launch .py file from a subdir'''
import os, sys, pathlib
os.chdir(pathlib.Path(__file__).parent.parent)
sys.path[0] = str(pathlib.Path(__file__).parent.parent)
