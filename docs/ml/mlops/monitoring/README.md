# ML Monitoring

Monitoring is how you notice that a model still serves traffic but has stopped serving value.

## Current Anchors

- Feature drift PSI (`modules/ml/mlops/feature-drift-psi`)
- KS-style drift detection (`modules/ml/mlops/drift-detection`)
- Prediction monitoring (`modules/ml/mlops/prediction-monitoring`)
- Request-level SLA compliance (`modules/ml/mlops/request-sla`)
- Queue age percentiles (`modules/ml/mlops/queue-age-percentiles`)
- Saturation rate (`modules/ml/mlops/saturation-rate`)
- Error-budget tracking (`modules/ml/mlops/error-budget`)

## Concepts to Cover Well

- Data drift vs prediction drift vs service health
- Slice-based monitoring, not just global aggregates
- Tail latency and queue buildup as early warning signals
- Alert thresholds that reflect user harm, not dashboard noise
- Error budgets as a bridge between SRE and ML quality
- Canary and shadow signals before full rollout
