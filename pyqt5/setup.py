import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this for Windows GUI applications

executables = [Executable("calculator.py", base=base)]

setup(
    name="Calculator",
    version="1.0",
    description="Use this for easy calculation",
    executables=executables
)
