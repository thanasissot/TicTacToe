# import cx_Freeze

# executables = [cx_Freeze.Executable('ttt2.py')]

# cx_Freeze.setup(
# 	name = 'Tic_Tac_Toe',
# 	options = {
# 		'build_exe' : {
# 			'packages' : ['pygame'], 
# 			'include_files' : ['x.png', 'o.png']
# 				}
# 			},
# 	description = 'My First Game Created with pygame, its a tic tac toe',
# 	executables = executables

# 	)

import sys
from cx_Freeze import setup, Executable

build_exe_options = {
	"packages": ["os", "pygame"], 
	"excludes": ["tkinter"], 
	"include_files" :["x.png", "o.png"]
	}

base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(  name = "TicTacToe",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("ttt2.py", base=base)]
        )