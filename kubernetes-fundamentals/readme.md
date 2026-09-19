# Kubernetes Fundamentals: A Comprehensive Guide

Welcome to the **Kubernetes Fundamentals** guide. This repository contains essential concepts, architectural overviews, practical configurations, and hands-on examples to help developers, DevOps engineers, and system administrators master Kubernetes (K8s).

---

## 📌 Table of Contents
- [What is Kubernetes?](#what-is-kubernetes)
- [Key Features](#key-features)
- [Kubernetes Architecture](#kubernetes-architecture)
  - [Control Plane Components](#control-plane-components)
  - [Worker Node Components](#worker-node-components)
- [Core Abstractions & Objects](#core-abstractions--objects)
- [Installation & Setup](#installation--setup)
- [Quick Start Guide](#quick-start-guide)
- [Declarative YAML Example](#declarative-yaml-example)
- [Essential `kubectl` Cheat Sheet](#essential-kubectl-cheat-sheet)
- [Best Practices](#best-practices)
- [License](#license)

---

## 💡 What is Kubernetes?

**Kubernetes** (often abbreviated as **K8s**, where 8 stands for the eight letters between 'K' and 's') is an open-source container orchestration platform originally designed by Google and now maintained by the Cloud Native Computing Foundation (CNCF).

It automates the deployment, scaling, management, and networking of containerized applications across clusters of host machines.

---

## ✨ Key Features

- **Automated Rollouts & Rollbacks:** Safely deploy application changes with zero downtime.
- **Service Discovery & Load Balancing:** Automatically expose containers via IP or DNS and distribute network traffic.
- **Storage Orchestration:** Automatically mount local storage, public cloud providers (AWS EBS, GCP PD, Azure Disk), or network storage (NFS, Ceph).
- **Self-Healing:** Restart failed containers, replace dead nodes, and kill non-responsive instances automatically.
- **Secret & Configuration Management:** Manage sensitive data (passwords, tokens, SSH keys) without rebuilding container images.
- **Horizontal Auto-scaling:** Automatically scale applications up or down based on CPU, memory, or custom metrics.

---

## 🏗️ Kubernetes Architecture

A Kubernetes cluster consists of a **Control Plane** (maintains the desired state) and one or more **Worker Nodes** (run the container workloads).

```
+-------------------------------------------------------------------------+
|                              CONTROL PLANE                              |
|                                                                         |
|   +-------------------+   +-------------------+   +-----------------+   |
|   |  kube-apiserver   |   | etcd (Key-Value)  |   | kube-scheduler  |   |
|   +-------------------+   +-------------------+   +-----------------+   |
|             ^                       ^                      ^            |
|             +-----------------------+----------------------+            |
|                                     |                                   |
|                      +-----------------------------+                    |
|                      | kube-controller-manager    |                    |
|                      +-----------------------------+                    |
+-------------------------------------------------------------------------+
                                      |
                +---------------------+---------------------+
                |                                           |
                v                                           v
+-------------------------------+           +-------------------------------+
|         WORKER NODE 1         |           |         WORKER NODE 2         |
|                               |           |                               |
| +---------------------------+ |           | +---------------------------+ |
| |        kubelet            | |           | |        kubelet            | |
| +---------------------------+ |           | +---------------------------+ |
| |       kube-proxy          | |           | |       kube-proxy          | |
| +---------------------------+ |           | +---------------------------+ |
| | Container Runtime (Docker/| |           | | Container Runtime (Docker/| |
| | containerd/CRI-O)         | |           | | containerd/CRI-O)         | |
| +---------------------------+ |           | +---------------------------+ |
| |  [Pod: App Container A]   | |           | |  [Pod: App Container B]   | |
| +---------------------------+ |           | +---------------------------+ |
+-------------------------------+           +-------------------------------+
```

### Control Plane Components

1. **`kube-apiserver`**: The front-end for the Kubernetes control plane. Exposes the Kubernetes API and validates/configures data for API objects.
2. **`etcd`**: A consistent and highly-available key-value store used as Kubernetes' backing store for all cluster data.
3. **`kube-scheduler`**: Watches for newly created Pods with no assigned node and selects a node for them to run on.
4. **`kube-controller-manager`**: Runs controller processes in the background (e.g., Node Controller, ReplicaSet Controller, EndpointSlice Controller).
5. **`cloud-controller-manager`**: Links your cluster into your cloud provider's API (AWS, GCP, Azure, etc.).

### Worker Node Components

1. **`kubelet`**: An agent that runs on each node in the cluster. It ensures that containers described in `PodSpecs` are running and healthy.
2. **`kube-proxy`**: Maintains network rules on nodes to allow network communication to your Pods from network sessions inside or outside of your cluster.
3. **Container Runtime**: The underlying software responsible for running containers (e.g., `containerd`, `CRI-O`).

---

## 🧱 Core Abstractions & Objects

| Object | Description |
| :--- | :--- |
| **Pod** | The smallest deployable computing unit in Kubernetes. Contains one or more tightly coupled containers. |
| **Service** | An abstract way to expose an application running on a set of Pods as a network service. |
| **Deployment** | Provides declarative updates for Pods and ReplicaSets (manages scaling, rolling updates). |
| **ConfigMap** | Stores non-confidential configuration data in key-value pairs. |
| **Secret** | Stores sensitive data like passwords, OAuth tokens, and SSH keys. |
| **Volume / PVC** | Provides persistent storage that outlives the container lifecycle. |
| **Namespace** | Provides virtual cluster isolation within the same physical cluster. |
| **Ingress** | Manages external access (typically HTTP/HTTPS) to services within a cluster. |

---

## ⚙️ Installation & Setup

For local learning and testing, you can use one of the following tools:

- **Minikube:** Runs a single-node Kubernetes cluster inside a VM/Docker on your laptop.
- **Kind (Kubernetes in Docker):** Runs local Kubernetes clusters using Docker container "nodes".
- **`kubectl`:** The command-line tool for communicating with a Kubernetes cluster control plane.

### Quick Install (`kubectl` & `minikube`)

```bash
# Install kubectl (Linux example)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Install Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Start local cluster
minikube start
```

---

## 🚀 Quick Start Guide

Let's deploy a simple Nginx web application step-by-step using `kubectl`.

### 1. Create a Deployment
```bash
kubectl create deployment nginx-app --image=nginx:latest
```

### 2. Verify Deployment and Pod Status
```bash
kubectl get deployments
kubectl get pods
```

### 3. Expose the Deployment as a Service
```bash
kubectl expose deployment nginx-app --type=NodePort --port=80
```

### 4. Access the Application
```bash
minikube service nginx-app
```

---

## 📄 Declarative YAML Example

In production, Kubernetes objects are defined declaratively using YAML manifests.

### `nginx-deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: web-server
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-server
  template:
    metadata:
      labels:
        app: web-server
    spec:
      containers:
      - name: nginx
        image: nginx:1.25.3
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: ClusterIP
  selector:
    app: web-server
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

### Apply the Manifest:
```bash
kubectl apply -f nginx-deployment.yaml
```

---

## 📋 Essential `kubectl` Cheat Sheet

```bash
# Cluster Information
kubectl cluster-info
kubectl get nodes

# Inspecting Resources
kubectl get pods -A                           # Get all pods across all namespaces
kubectl get services                          # List services in default namespace
kubectl describe pod <pod-name>               # Detailed inspection of a pod
kubectl logs <pod-name>                       # View logs of a pod
kubectl exec -it <pod-name> -- /bin/bash      # Interactive shell into container

# Scaling & Updates
kubectl scale deployment <name> --replicas=5  # Scale deployment to 5 replicas
kubectl rollout status deployment/<name>      # Check status of rolling update
kubectl rollout undo deployment/<name>        # Roll back to previous revision

# Cleanup
kubectl delete -f nginx-deployment.yaml
```

---

## 🛡️ Best Practices

1. **Always Define Resource Requests & Limits:** Prevents noisy neighbor issues and ensures cluster stability.
2. **Use Namespaces:** Organize workloads and enforce ResourceQuotas across teams/environments (dev, staging, prod).
3. **Use Declarative Files (`kubectl apply`):** Store all manifests in version control (GitOps approach).
4. **Implement Liveness and Readiness Probes:** Ensure traffic is only routed to healthy pods and automatically restart deadlocked containers.
5. **Keep Secrets Secure:** Use external secret managers (e.g., HashiCorp Vault, AWS Secrets Manager) instead of committing base64-encoded Kubernetes secrets into Git.

---

## 📄 License

This repository and documentation are distributed under the [MIT License](LICENSE).