import sys
import os
import coloredlogs

coloredlogs.install(level="INFO")

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/ui/")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/ui/statics/")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/ui/statics/icons")

print(os.path.dirname(os.path.abspath(__file__)))