import subprocess as sb
import json

CONF = json.load(open("Configure.json", "r"))

numberOfFiles =  str(CONF["numberOfConf"])
numberOfJobs =   str(CONF["numberOfJobs"])
workingFolder =  str(CONF["workingFolder"])

command = "python makeJobs_3040.py " + numberOfFiles + " " + numberOfJobs
clean1 = "rm " + workingFolder + "/interpolation/JOBS/pre-job-*"
clean2 = "rm " + workingFolder + "/interpolation/JOBS/job-*.sh"

sb.call(command, shell=True)        # automatically waits for the process to finish
sb.call("chmod +x source.sh", shell=True)  # automatically waits for the process to finish
sb.call("./source.sh", shell=True)  # automatically waits for the process to finish
sb.call(clean1, shell=True)  # automatically waits for the process to finish
sb.call(clean2, shell=True)  # automatically waits for the process to finish
