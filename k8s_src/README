Application:
===============
-> A simple web app that displays access count, count maintained in redis cache,
-> Comprises two micro services, app and redis service.
-> Service Discovery happens with kuberentes DNS, web service can access redis via service name.

Deployment:
-> Deployed on minikube(single node cluster) with hyperkit(hypervisor/xhyve) driver.
-> Cluster has one node which acts as master and worker node.

Observations:
================
Networking
---------------
-> container process running as pods can access host ports, host serices via host ip.
-> Without creating service, to test process on a pod, get into pod and do a curl to localhost
    ex: kubectl exec web-app -it /bin/bash
        curl localhost:5000/ping
-> A NodePort service also creates a clusterIP service by default. NodePort is used for external access and
   clusterIP is used for access withing cluster. So there are three ways to access a service

    1) Within pod, if its service running on pod, localhost:containerPort.
       If its a different pod must need cluster IP(create a service) or pod IP(kubectl describe pod <pod-name>)
        >kubectl exec app-rc-874nj -it curl http://localhost:5000/hello
         Hello World! I've been accessed b'10' times%   

         From different pod, all three work!!
            Invocation format            Invocation using curl and port        How to get IP:port
            -----------------            --------------------------------      -----------------------
            Pod IP:<container Port>   -  curl http://172.17.0.4:5000/ping       kubectl describe pod <app-pod>)
            Node IP:<nodeport>        -  curl http://192.168.64.4:31101/ping    kubectl get nodes | minikube ip)
            Cluster IP:<port>         - curl http://10.110.153.205:80/ping      # needs a service. kubectl get services
    2) Within cluster, ClusterIP:<port>
        >kubectl exec app-rc-874nj -it curl http://10.110.153.205:80/hello  
         Hello World! I've been accessed b'9' times%                                                            
    3) Outside Cluster(browser/host), NodePort:<ephermal-port> or more precisely NODEIP:<Nodeport>
        >curl http://192.168.64.4:31101/hello
         Hello World! I've been accessed b'11' times%      
                                                                                                            
Labels and Selectors
----------------------
-> Labels and their counterpart selectors are absolutely crucial to map pod(s) to a service.
-> service selector looks for matching labels and only with perfect match, pods are abstraced
   under service.
   Ex: 
    metadata:
        labels:
           name1: value1
           name2: value2
           name3: value3 matches/falls under a service with selector
    
    metadata:
        selector:
            name1: value1
            name3: value2
            name3: value3

-> Always check container status after pod creation, pod creation is fast but container might not be
   up always.

Secret Management
-------------------
-> For pulling images from a  private repository hosted by any registry, k8s provides a way to supply
   creds without supplying actual uname/pwd for example.
   > kubectl create secret docker-registry regcred --docker-server=<your-registry-server> \
    --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
-> This secret can be referred by supplying secret name in pod/rc template.
    spec:
        containers:
            - name: private-reg-container
              image: <your-private-image>
        imagePullSecrets:
            - name: regcred
More info at: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/

Resource requests and limits
-----------------------------
-> To prevent starvation of other processes resource(cpu/memory) request can be supplied in tempalte.
-> This also helps scheduler to schedule a pod on right node.
-> limits sets hard limit for resource usage thus avoiding starvation scenario.
-> vcpu is expressed as decimal or number format.
   The expression 0.1 is equivalent to the expression 100m, which can be read as "one hundred millicpu".
   https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/