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