import subprocess as sb
import json

CONF = json.load(open("Configure.json", "r"))

numberOfFiles =  str(CONF["numberOfConf"])
numberOfJobs =   str(CONF["numberOfJobs"])

command = "python2 makeJobs_510.py " + numberOfFiles + " " + numberOfJobs

sb.call(command, shell=True)        # automatically waits for the process to finish
sb.call("chmod +x source.sh", shell=True)  # automatically waits for the process to finish
sb.call("./source.sh", shell=True)  # automatically waits for the process to finish
