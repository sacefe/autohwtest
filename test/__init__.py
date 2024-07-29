import coloredlogs
import sys
import os


coloredlogs.install(level="CRITICAL")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

