""" Launching and closing Pymol 

Does not work..!!!
"""

import pymol
from pymol import cmd
import time

pymol.finish_launching()
cmd.fetch("1DLO")
print("Sleeping for 1 sec")
time.sleep(1)
print("Quitting Pymol")
cmd.delete('all')
cmd.quit()

raw_input()
print("Starting Pymol again")
pymol.finish_launching()
cmd.fetch("2JPR")
print("Sleeping for 1 sec")
time.sleep(1)
print("Quitting Pymol")
cmd.quit()





