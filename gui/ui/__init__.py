import sys
import os
import coloredlogs

coloredlogs.install(level="INFO")

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/statics/")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/statics/icons")