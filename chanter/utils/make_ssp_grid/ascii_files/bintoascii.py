import sys
import os
import glob

bins = [f for f in sorted(glob.glob(f'Miles_Atlas/Chabrier_IMF/*ised'))]


for i in bins:
    os.system('$bc03/ascii_ised ./' + i)