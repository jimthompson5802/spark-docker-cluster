# Stand-alone Spark Cluster with Kubernetes






Encountered this [issue](https://medium.com/@varunreddydaaram/kubernetes-did-not-work-with-apache-spark-de923ae7ab5c).  This necessitated changing kubernetes service name from `spark-master` to `spark-master-kub`.

Start kubernetes cluster:
```
kubectl apply -f standalone-spark-cluseter.yaml
```

Stop kubernetes cluster:
```
kubectl delete -f standalone-spark-cluster.yaml
```