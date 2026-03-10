# Breach Bucket Metrics

Breach bucket metrics summarize overload severity after turning capacity breaches into severity buckets.

## Metric Families

- Mass metrics: breach bucket share, mass, cumulative share
- Shape metrics: entropy, slope, curvature, bend, wave
- Threshold-location metrics: quantile, knee, turning point, inflection
- Tail metrics: breach bucket tail, span
- Area metrics: step function, step area

## How to Use Them

- Use share or mass when you want the basic severity distribution across buckets.
- Use entropy when you want to know whether overload is spread across many severities or concentrated.
- Use slope and curvature when you care about abrupt changes from mild to severe overload.
- Use knee or inflection metrics when you need a “where does it get bad” summary.
- Use step-area style metrics when cumulative burden matters more than local shape.

## Good Defaults

- `capacity-breach-rate` before any bucketized analysis
- `breach-bucket-share` as the base distribution view
- `breach-bucket-entropy` for concentration
- `breach-bucket-slope` when abrupt escalation matters
