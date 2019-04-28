# Stand-alone Spark Cluster with Kubernetes


Install [`kompose`](https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/) utility to convert docker-compose yaml to kubernetes resources.
```
brew kompose
```


Convert docker-compose.yml to kubernetes
```
cd sprkclstr
# generate fully resolved docker-compose yaml file
docker-compose config > ../kubernetes/resolved-docker-compose.yaml

cd ../kubernetes
# convert from docker-compose to kubernetes resources
kompose convert -f resolved-docker-compose.yaml --volumes hostPath -o kubernetes-spark-cluster.yaml
```

Encountered this [issue](https://medium.com/@varunreddydaaram/kubernetes-did-not-work-with-apache-spark-de923ae7ab5c).  This necessitated changing kubernetes service name from `spark-master` to `spark-master-kub`.

Start kubernetes cluster:
```
kubectl apply -f standalone-spark-cluseter.yaml
```

Stop kubernetes cluster:
```
kubectl delete -f standalone-spark-cluster.yaml
```