"""
This script can be used to test your maze solver.
- create a folder with this file, the maze_env.py (most recent version) file and your python file that contains your solver
- change the indicated line (see below) to include the name of your python file
- run this file
- check the output in the console. If it ONLY reads "TEST PASSED SUCCESFULL" you are good.
- if you have any other output (e.g. a plot or print output) remove them from your code
"""
# ====================================================================== #
# IN THE LINE BELOW CHANGE "YOURFILENAME" TO THE NAME OF YOUR PYTHON FILE 

from Maze.contest.contestWayOut import way_out

# ====================================================================== #

from Maze.contest.maze_env import make

# create a maze environment
env = make(size=101)

# try to execute the solver
try:
    path = way_out(env)

except Exception as e:
    exit(f'TEST FAILED TO RUN way_out(). Error message: {e}')

# validate the path
valid = env.check_path(path)

if valid:
    print('TEST PASSED SUCCESFULL')
    
else:
    print('TEST FAILED')
