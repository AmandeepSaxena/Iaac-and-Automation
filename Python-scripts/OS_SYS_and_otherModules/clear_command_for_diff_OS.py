import os
import platform

print("Clearing Screen .....")
if platform.system () == 'Windows':
    os.system("cls")
else:
    os.system("clear")
