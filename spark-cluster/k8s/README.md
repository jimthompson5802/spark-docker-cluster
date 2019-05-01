# Stand-alone Spark Cluster with Kubernetes

## Set up

Encountered this [issue](https://medium.com/@varunreddydaaram/kubernetes-did-not-work-with-apache-spark-de923ae7ab5c).  This necessitated changing kubernetes service name from `spark-master` to `spark-master-kub`.

### Specify Location of `project` and `data` directories

For the location of Jupyter Notebooks, update the `path:` key with the host directory, in the following:
```
  hostPath:
    path: "/top_level_dir/subdirx/project_dir"
```

in this portion of the `k8s-spark-cluster.yaml` file

```
# Volume containing project source code
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: project-pv-volume
  labels:
    type: local
spec:
  storageClassName: project-dir
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/top_level_dir/subdirx/project_dir"
```

For the location of shared data, update the `path:` key with the host directory, in the following:
```
  hostPath:
    path: "/top_level_dir/subdirx/data_dir"
```

in this portion of the `k8s-spark-cluster.yaml` file

```
# Volume simulating distributed file system
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: data-pv-volume
  labels:
    type: local
spec:
  storageClassName: spark-data
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/top_level_dir/subdirx/data_dir"
```

## Starting Stand-alone Spark Cluster
Start kubernetes cluster:
```
cd spark-cluster/k8s
kubectl apply -f k8s-spark-cluster.yaml
```

To verify the cluster successfully started, run the `kubectl get all -o=wide` command.  
The output should look similar to below.  
```
NAME                                 READY     STATUS    RESTARTS   AGE       IP          NODE
pod/pyspnb-client-7fd5b77c56-zwl8p   1/1       Running   0          1m        10.1.1.62   docker-for-desktop
pod/spark-master-7b4ff7f484-hg9s6    1/1       Running   0          1m        10.1.1.60   docker-for-desktop
pod/spark-worker1-5468c78c4b-s6vj7   1/1       Running   0          1m        10.1.1.59   docker-for-desktop
pod/spark-worker2-7d8cb4b589-h22jj   1/1       Running   0          1m        10.1.1.61   docker-for-desktop

NAME                       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)             AGE       SELECTOR
service/kubernetes         ClusterIP   10.96.0.1    <none>        443/TCP             10h       <none>
service/pyspnb-client      ClusterIP   None         <none>        8888/TCP,4040/TCP   1m        app=pyspnb-client
service/spark-master-kub   ClusterIP   None         <none>        8080/TCP            1m        app=spark-master
service/spark-worker1      ClusterIP   None         <none>        18081/TCP           1m        app=spark-worker1
service/spark-worker2      ClusterIP   None         <none>        28081/TCP           1m        app=spark-worker2

NAME                            DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE       CONTAINERS      IMAGES               SELECTOR
deployment.apps/pyspnb-client   1         1         1            1           1m        pyspnb-client   spark-pyspnb:2.4.1   app=pyspnb-client
deployment.apps/spark-master    1         1         1            1           1m        spark-master    spark-master:2.4.1   app=spark-master
deployment.apps/spark-worker1   1         1         1            1           1m        spark-worker1   spark-worker:2.4.1   app=spark-worker1
deployment.apps/spark-worker2   1         1         1            1           1m        spark-worker2   spark-worker:2.4.1   app=spark-worker2

NAME                                       DESIRED   CURRENT   READY     AGE       CONTAINERS      IMAGES               SELECTOR
replicaset.apps/pyspnb-client-7fd5b77c56   1         1         1         1m        pyspnb-client   spark-pyspnb:2.4.1   app=pyspnb-client,pod-template-hash=3981633712
replicaset.apps/spark-master-7b4ff7f484    1         1         1         1m        spark-master    spark-master:2.4.1   app=spark-master,pod-template-hash=3609939040
replicaset.apps/spark-worker1-5468c78c4b   1         1         1         1m        spark-worker1   spark-worker:2.4.1   app=spark-worker1,pod-template-hash=1024734706
replicaset.apps/spark-worker2-7d8cb4b589   1         1         1         1m        spark-worker2   spark-worker:2.4.1   app=spark-worker2,pod-template-hash=3847606145
Jim-MacBook-Pro:k8s jim$
```

## Shutdown Stand-alone Spark Cluster
Stop kubernetes cluster:
```
cd spark-cluster/k8s
kubectl delete -f k8s-spark-cluster.yaml
```

## Web Access to the Stand-alone Spark Cluster

Before using the web UIs, kubernetes port forwarding must be established by the following command.
```
cd spark-cluster/k8s
python port_forward_helper.py setup
```

Output from the above should be similar to this:
```
Jim-MacBook-Pro:k8s jim$ python port_forward_helper.py setup
invoke command kubectl port-forward pyspnb-client-69f57c5564-j9gv5 8888 4040
started pid: 4201
invoke command kubectl port-forward spark-master-57fbf6bc58-8qlmc 8080
started pid: 4202
invoke command kubectl port-forward spark-worker1-645bc4765d-bj2b8 18081
started pid: 4203
invoke command kubectl port-forward spark-worker2-767678476-l97g9 28081
started pid: 4204
```

To verify that port forwarding has been established execute this command `ps -ef | grep port-forward`.  Output from 
this command should look similar to the following:
```
Jim-MacBook-Pro:k8s jim$ ps -ef | grep port-forward
  501  4201     1   0 10:16PM ttys001    0:00.13 kubectl port-forward pyspnb-client-69f57c5564-j9gv5 8888 4040
  501  4202     1   0 10:16PM ttys001    0:00.12 kubectl port-forward spark-master-57fbf6bc58-8qlmc 8080
  501  4203     1   0 10:16PM ttys001    0:00.13 kubectl port-forward spark-worker1-645bc4765d-bj2b8 18081
  501  4204     1   0 10:16PM ttys001    0:00.12 kubectl port-forward spark-worker2-767678476-l97g9 28081
  501  4216  1573   0 10:16PM ttys001    0:00.00 grep port-forward
```

After establishing port forwarding, the following web UI can be accessed.

|WEB UI|URL|
|------|---|
|PySpark Jupyter Notebook Server|`http://localhost:8888`|
|Spark Master Web UI|`http://localhost:8080`|

Execute the following command to shutdown port-forwarding.
```
cd spark-cluster/k8s
python port_forward_helper.py teardown
```


