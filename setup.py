#file to generate setup.exe
import cx_Freeze

executables=[cx_Freeze.Executable("Snake.py")]

cx_Freeze.setup(
    name="Snake",
    options={"build_exe":{"packages":["pygame"],"include_files":["snakehead.png","apple.png","icon.png"]}}
    #description="Snake Game",
    ,executables=executables
    )
