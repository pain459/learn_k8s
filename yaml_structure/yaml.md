# Kubernetes YAML Structure and Variations

This document outlines the structure of Kubernetes YAML files, describes common Kubernetes objects, and provides their variations with examples.

---

## **Basic Structure of a Kubernetes YAML File**

Every Kubernetes YAML file follows this basic structure:

1. **`apiVersion`:** Specifies the API version of the object. Examples include `v1`, `apps/v1`, etc.
2. **`kind`:** Defines the type of Kubernetes object (e.g., Pod, Service, Deployment).
3. **`metadata`:** Contains metadata like name, namespace, and labels.
4. **`spec`:** Specifies the desired state of the object, which varies by object type.

Example:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
```

## **Variations**

### **Pod**

Description: A Pod represents the smallest deployable unit in Kubernetes, usually a single container or a group of tightly coupled containers.

Single Container Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: single-container-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
```

Multi Container Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
  - name: app-container
    image: my-app:latest
  - name: sidecar-container
    image: my-sidecar:latest
```

Pod with Volume
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-volume
spec:
  containers:
  - name: nginx-container
    image: nginx
    volumeMounts:
    - mountPath: /data
      name: my-volume
  volumes:
  - name: my-volume
    emptyDir: {}
```

### **Deployment**

Description: A Deployment ensures that a specified number of replicas of an application are running. It manages scaling and rolling updates.

Basic Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: basic-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: nginx
        image: nginx
```

Deployment with Environment Variables
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-with-env
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app-container
        image: my-app:latest
        env:
        - name: ENV_VAR_NAME
          value: ENV_VAR_VALUE
```

Rolling update Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rolling-update-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app-container
        image: my-app:1.0
```

### **Service**

Description: A Service exposes a group of Pods to the network, enabling communication. Types of Services include ClusterIP, NodePort, LoadBalancer, and ExternalName.

ClusterIP Service (Default):
```yaml
apiVersion: v1
kind: Service
metadata:
  name: clusterip-service
spec:
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: ClusterIP
```

NodePort Service:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nodeport-service
spec:
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30001
  type: NodePort
```

Load Balancer Service:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: loadbalancer-service
spec:
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: LoadBalancer
```

### **ConfigMap**

Description: A ConfigMap is used to store configuration data as key-value pairs that can be consumed by Pods.

Simple ConfigMap:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: simple-config
data:
  key1: value1
  key2: value2
```

ConfigMap with file reference:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: file-config
data:
  app-config.yaml: |
    logging:
      level: debug
```

### **Secret**

Description: A Secret stores sensitive information, such as passwords or tokens, in base64-encoded format.

Opaque Secret:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
data:
  username: YWRtaW4=  # base64 for 'admin'
  password: cGFzc3dvcmQ=  # base64 for 'password'
```

TLS Secret:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: tls-secret
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded-cert>
  tls.key: <base64-encoded-key>
```

### **PersistentVolume (PV)**

Description: A PersistentVolume is a storage resource in the cluster, abstracting storage implementation details.

Example:
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
  - ReadWriteOnce
  hostPath:
    path: /data
```

