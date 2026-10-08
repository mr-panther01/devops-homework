# Monitoring Demo

This demo uses Prometheus to collect and query metrics and Grafana to connect to Prometheus and display metric data.

## Prometheus

The screenshots show the Prometheus container starting, the metrics endpoint, and example PromQL queries. The `up` metric reports whether a Prometheus scrape target is reachable (`1` means up; `0` means down).

![Prometheus container startup](image-5.png)
![Prometheus query page](image.png)
![Prometheus metrics endpoint](image-1.png)
![Querying process CPU time](image-2.png)
![Querying HTTP request counters](image-7.png)
![Querying the up metric](image-12.png)

## Grafana

Grafana is connected to Prometheus as a data source. The screenshots show the connection test and Grafana dashboard and panel screens.

![Grafana containers running](image-10.png)
![Grafana home](image-3.png)
![Grafana Prometheus data-source settings](image-4.png)
![Grafana panel editor](image-6.png)
![Successful Prometheus data-source test](image-14.png)

## What to observe

- **Metrics:** Prometheus exposes numeric, timestamped measurements that can be queried with PromQL.
- **CPU:** `process_cpu_seconds_total` is cumulative CPU time, not a percentage. For a CPU usage rate, query `rate(process_cpu_seconds_total[5m])`.
- **Memory:** Memory graphs require a memory metric from the application or a host/container exporter. This screenshot set does not show a configured memory exporter.
- **Health:** `up` indicates whether Prometheus can scrape a target; application health endpoints and Kubernetes readiness/liveness probes provide additional health signals.
- **Alerts:** Prometheus can evaluate alert rules against metrics and send firing notifications through Alertmanager. Alert rules and notification delivery are not shown in these screenshots.
- **Logs:** This demo focuses on metrics. A log backend such as Loki or Elasticsearch is needed to collect and search logs.

See [Observability](../observability/README.md) for the three observability pillars and common Kubernetes patterns, and [GitOps Demo](../gitops/README.md) for the Argo CD walkthrough.
