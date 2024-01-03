import subprocess
import sys

command = "./classic_solvers/MQLib -h BURER2002 -fM " + sys.argv[1] + " -r " + sys.argv[2]

result = subprocess.run( command , shell=True , capture_output=True, check=False)
print(result.stdout.decode('utf-8'))
result_text = result.stdout.decode('utf-8').split(',')
print(result_text[3] + "," + result_text[4])