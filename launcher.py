import sys
import os
requirements = ['typing', 'matplotlib', 'statistics']
for name in sys.modules:
    if name in requirements:
        requirements.remove(name)
for name in requirements:
    os.system(f'py -m pip install {name}')
os.system('py DarBabies.py')
os.system('cls')
os.system('pause')