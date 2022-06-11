import os
import subprocess
import sys


# Check for new version from github
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'git+https://github.com/NathanKuneman/schroompi.git'])

