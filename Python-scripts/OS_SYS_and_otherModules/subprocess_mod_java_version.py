import subprocess
import string
#NOTE : shell=True (for windows) and shell=False (and if passing cmds as list for Linux) for ex cmd = ['java','--version']

cmd = "java --version"
# important - java --version output comes in stderr not in stdout

sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

rc = sp.wait #wait for execution 
o,e = sp.communicate() # whether output or error it will pass that value
if rc == 0:
    if bool(o) == True: # never happens as java prints version in stderr
        print(o)
    if bool(o) == False and bool(e) == True:
        print(e)
else:
    print(e)