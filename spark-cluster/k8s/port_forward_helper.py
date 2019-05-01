"""
Extracts kubernetes port information to setup port forwarding to allow web access

python port_forward_helper.py  setup|teardown

"""

import yaml
from subprocess import Popen, PIPE, DEVNULL
import argparse
import os

PID_LIST_FILE = './port-forward-pids'


parser = argparse.ArgumentParser(description='Port forwarding helper.')

parser.add_argument('operation', nargs='?', choices=['setup', 'teardown'],
                    default='setup',
                    help="'setup' or 'teardown' port forwarding")

args = parser.parse_args()

if args.operation == 'setup':
    # setup port forwarding

    K8S_GET_PODS = 'kubectl get pods -o yaml'

    # Retrieve pod configuration info
    cmd = Popen(K8S_GET_PODS,shell=True,stdout=PIPE)
    cmd.wait()

    # convert yaml to python dictionary
    pods_dict = yaml.safe_load(cmd.stdout)

    # loop through all pods looking for ports to forward and build port forwarding
    pid_string = ""
    for pod in pods_dict['items']:

        # start building the port forward command
        port_forward_cmd = 'kubectl port-forward ' + pod['metadata']['name']

        # for each container in pod extract ports
        for c in pod['spec']['containers']:
            for p in c['ports']:
                port_forward_cmd += ' ' + str(p['containerPort'])

        # invoke port-forward command
        print('invoke command',port_forward_cmd)
        cmd = Popen(port_forward_cmd, shell=True, stdout=DEVNULL)
        print('started pid:', cmd.pid)
        pid_string += str(cmd.pid) + " "

    # write port-forwarding pids to file for teardown
    with open(PID_LIST_FILE,"w") as f:
        f.write(pid_string)

else:

    # tear down the port-forwarding processes
    with open(PID_LIST_FILE,'r') as f:
        pid_string = f.read()

    Popen("kill " + pid_string,shell=True)

    os.remove(PID_LIST_FILE)

