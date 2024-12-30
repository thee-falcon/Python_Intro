# we are going learn how to call external programs from our python scripts

# with this module we can spot a child process, A process is basically an instance of a running program
# so with this module we can run other  programs
import subprocess

try:
   complited =  subprocess.run(["python3", "other.py"],
                               capture_output=True,
                               text=True # to remove the 'b' prefex in stdout
                               )
   print("args: ", complited.args)
   print("returncode: ", complited.returncode)
   print("stderr: ", complited.stderr) # stderr if our code return a 1
   print("stdout: ", complited.stdout) # stdout we use when we need to capture the output
except subprocess.CalledProcessError as ex:
    print(ex)