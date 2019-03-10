#!/usr/bin/python
#Author Jeganathan Swaminathan <jegan@tektutor.org> <http://www.tektutor.org>

import subprocess
import json
from os.path import expanduser

def executeDockerCommand(*args):
    return subprocess.check_output(["docker"] + list(args)).strip()

def docker_inspect(fmt, mcn):
    return executeDockerCommand("inspect", "-f", fmt, mcn)

def get_host_vars(m):
    home = expanduser("~")
    ip = [docker_inspect("{{.Config.Hostname}}", m)]


    ssh_vars = {
    }

    hostConnectionDetails = {"hosts": ip, "vars": ssh_vars}
    return hostConnectionDetails

class DockerInventory():
      def __init__(self):
          self.inventory = {} # Ansible Inventory

          machines = executeDockerCommand("ps", "-q").splitlines()
          json_data = {m: get_host_vars(m) for m in machines}

          print json.dumps(json_data,indent=4,sort_keys=True)

DockerInventory()
