"""
Extracts kubernetes port information to setup port forwarding to allow web access
"""

import yaml
from subprocess import Popen, PIPE

K8S_GET_PODS = 'kubectl get pods -o yaml'

# Retrieve pod configuration info
cmd = Popen(K8S_GET_PODS,shell=True,stdout=PIPE)
cmd.wait()

# convert yaml to python dictionary
pods_dict = yaml.safe_load(cmd.stdout)

# loop through all pods looking for ports to forward and build port forwarding
for pod in pods_dict['items']:

    # start building the port forward command
    port_forward_cmd = 'kubectl port-forward ' + pod['metadata']['name']

    # for each container in pod extract ports
    for c in pod['spec']['containers']:
        for p in c['ports']:
            port_forward_cmd += ' ' + str(p['containerPort'])

    # invoke port-forward command
    print('invoke command',port_forward_cmd)
    cmd = Popen(port_forward_cmd + '&', shell=True)
    cmd.wait()
