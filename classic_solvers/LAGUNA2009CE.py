import subprocess
import sys

command = "./classic_solvers/MQLib/bin/MQLib -h LAGUNA2009CE -fM " + sys.argv[1] + " -r " + sys.argv[2]

result = subprocess.run( command , shell=True , stdout=subprocess.PIPE, check=False)
result_text = result.stdout.decode('utf-8').split(',')
print(result_text[3] + "," + result_text[4])