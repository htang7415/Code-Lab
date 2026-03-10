# ML Serving

Serving is the operational layer between a trained model and a real user-facing workload.

## Current Anchors

- Offline vs online inference (`modules/ml/mlops/offline-online-inference`)
- Batch vs real-time inference (`modules/ml/mlops/batch-vs-realtime`)
- Canary deployment (`modules/ml/mlops/canary-deployment`)
- Canary rollout progression (`modules/ml/mlops/canary-rollout`)
- Online shadow mode (`modules/ml/mlops/online-shadow-mode`)
- Request batching (`modules/ml/mlops/request-batching`)
- Admission control (`modules/ml/mlops/admission-control`)
- Queue delay (`modules/ml/mlops/queue-delay`)
- Request-level SLA compliance (`modules/ml/mlops/request-sla`)
- Continuous batching (`modules/ml/systems/continuous-batching`)

## Concepts to Cover Well

- Offline, batch, streaming, and online serving modes
- Canary, shadow, and rollback strategies
- Queueing, batching, and admission control under load
- SLA design around latency, reliability, and throughput
- Cost / latency / accuracy trade-offs in production
- How serving architecture changes evaluation and monitoring needs
