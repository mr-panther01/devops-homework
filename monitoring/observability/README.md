# Observability

Observability is the ability to understand a system's internal state from the telemetry it produces. It helps teams answer both known questions (such as whether CPU is high) and new questions (such as which dependency caused a latency spike) without relying only on manually reproducing a failure.

## Why observability is required

Distributed applications span services, containers, and infrastructure. A user-visible failure may come from any part of that system. Correlated metrics, logs, and traces help operators:

- Detect incidents and performance regressions.
- Locate the affected service and narrow down root causes.
- Measure availability and latency against service-level objectives (SLOs).
- Understand the impact of a deployment or configuration change.
- Reduce time to diagnose and recover from production issues.

Monitoring commonly checks known conditions with dashboards and alerts. Observability uses telemetry to investigate behavior that was not fully anticipated in advance. In practice, monitoring is an important part of an observable system.

## The three pillars

### Metrics

Metrics are numeric measurements recorded over time, usually aggregated and labeled by dimensions such as service, environment, or status code. They are efficient for dashboards, alerting, and identifying trends.

Examples include request rate, error rate, request latency, CPU utilization, memory working set, and the number of healthy replicas.

Common tools: **Prometheus** and **OpenTelemetry Metrics** for collection/instrumentation; **Grafana** for dashboards; **Alertmanager** for routing Prometheus alerts.

### Logs

Logs are timestamped records of individual events. Structured logs (for example JSON with a severity, service name, trace ID, and message) are easier to filter and correlate than unstructured text.

Logs provide detail about what happened in a process, such as an exception, a rejected request, or a failed dependency call. They are usually searched by time range and fields rather than aggregated like metrics.

Common tools: **Loki**, **Elasticsearch / OpenSearch**, **Fluent Bit**, and **OpenTelemetry Collector**.

### Traces

Traces show the path of a request through a distributed system. A trace is composed of spans; each span represents work in a service or dependency and records timing and context. Trace and span IDs can be included in logs to connect a specific event to the request that produced it.

Traces are especially useful for finding latency bottlenecks and locating failed calls across service boundaries.

Common tools: **OpenTelemetry** for instrumentation and context propagation; **Jaeger**, **Grafana Tempo**, and **Zipkin** for storing or exploring traces.

## Kubernetes observability

Kubernetes observability combines application telemetry with signals from the cluster:

1. Instrument applications with OpenTelemetry or a library native to the metrics backend. Expose health probes separately from business metrics.
2. Collect cluster and container resource measurements using components such as kube-state-metrics and cAdvisor, typically surfaced through Prometheus-compatible scraping.
3. Collect container logs from nodes with an agent such as Fluent Bit or the OpenTelemetry Collector, and send them to a log backend.
4. Propagate trace context between services and export spans through an OpenTelemetry Collector to a tracing backend.
5. Use Grafana or another UI to explore dashboards, logs, and traces. Configure alerts for actionable symptoms such as sustained error rates, elevated latency, unavailable targets, or low capacity.
6. Use Kubernetes readiness and liveness probes for traffic eligibility and process recovery. A probe is not a replacement for application-level metrics, logs, or traces.

Choose retention, access control, sampling, and metric labels carefully. High-cardinality labels (for example, unique request IDs) can make metrics storage expensive; put per-request details in logs or traces instead.

## Relation to the demos

- [Monitoring Demo](../monitoring/Readme.md) shows Prometheus metrics and a Grafana data-source connection.
- [GitOps Demo](../gitops/README.md) shows an Argo CD-managed Kubernetes application.

The screenshots illustrate monitoring and GitOps workflows; they do not represent a complete logs-and-traces stack.
