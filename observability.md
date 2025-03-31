Could you please share following experiences:
1. How you improve Observability platform to smoothly integrate into OE?
- self service
- Standardize infrastructure from different layers 


2. How you prevent work/cost of Observability not linearly/exponential increase? 
- standardize, compression + sample
- skipping index, from ingest to query
- object storage, query algorithm
- task allocation optimization

3. How to improve scalability/performance with infrastructure support?
- Integrate infra to application Orchestrator e.g. [Agones](https://agones.dev/site/)
- Bring scalability interface to system design component in early stage and offload it to infra




Standardization is infrastructure.
Application, telemetry.
- Expensive, Sentry/OpenTelemetry, Datadog
- Community,
- Coverage
- Benefit, snowplow
- Trend

Cilium  - Network interface/L4

