# Search and Recommendation Systems

## ML Model Metrics
### Offline Metrics
#### General
- Retrieval: Recall, nDCG
- Rerank: MRR, AUC
- Classification (Imbalanced): Precision, Recall, F1, Log loss
- Regression: RMSE, MSE
- Ranking: NDCG, MAP, MRR
- Text Generation: BLEU, ROUGE, Perplexity

#### Search & Recommend

Refer to https://www.evidentlyai.com/ranking-metrics

##### Predictive quality metrics
- Precision at K
- Recall at K
- F-score

##### Ranking quality metrics
- MRR, MAP and NDCG
- Hit Rate (online)

##### Behavioral metrics
- Diversity
- Novelty
- Serendipity
- Popularity bias

##### final metrics
- Search: MAP, Recall, Precision, NDCG, R-Precision 
- Fintech: AUC, [KS](https://chatgpt.com/share/67e8bef2-cef0-800d-b4fd-348c4db92de6) for binary classification
- Fraud detection: Recall

### Online Metrics/Business Metrics
- Positive Metrics
  - CTR (Click-Through Rate)
  - ATC (Add-to-Cart)
  - Conversion Rate
  - User engagement metrics
- Negative Metrics
  - Exit Rate
  - Zero Result Rate

### Improvements
- Multi-task training to mitigate gap between business and training objectives (MMoE, PLE)
- Teacher-student model approach: Learning from downstream model instead of ground truth
- Feature engineering: add new features
- Data augmentation: sampling strategy, synthetic data
- Hyperparameter Tuning: neural architecture search (NAS)
- Model architecture optimization: task-specific components, pre-trained models, regularization
- Post-processing: ensemble methods

## Feature Store Management
### Feature Types
- Static Features
  - User profile embeddings
  - Document embeddings
- Dynamic Features
  - Context features
  - In-session information
- Raw Features
  - User logs
  - Interactions
  - Transcription history
- Aggregated Features
  - Rolling statistics
  - Trends (7-day engagement, popularity)
- Embedding Features
  - Sentence embeddings
  - Graph embeddings
- Time Serial Features
  - Recency-based scores
  - Session-level features
- Metadata
  - User side-information (device type, geolocation)
  - Item side-information (content category)

### Challenges
- Latency vs accuracy trade-offs (larger embeddings → more accurate but slower)
- Granularity optimization (cluster numbers, time windows)
- Feature consistency between training and serving
- Missing data handling
- Data freshness & latency: ensuring near real-time updates
- Feature Drift: Models degrading due to distribution shifts
- High storage & Compute Cost: Managing petabytes of data efficiently
- Dependency Management: Tracking feature lineage across teams

## GPU Cluster Performance Optimization
### Model Optimization
- Quantization (FP32 -> FB16 or INT8 for reducing memory footprint)
- Pruning (Removing unnecessary layers/weights)
- Knowledge distillation (training smaller models with teacher guidance)

### Efficient Execution
- TensorRT/ONNX Runtime: converts model for optimized GPU inference. SGLang or TensorRT-LLM could be used here.
- Caching and batching: Combines multiple requests to maximize throughput
- Asynchronous execution: avoid idle GPU time

### Scaling
- Triton Inference servers: Enables multi-GPU and multi-model serving
- Kubernetes + GPU Auto-scaling: Deploys dynamic inference workloads efficiently

## LLM Inference Challenges
### Performance Challenges
- High latency
  - Large models require substantial compute
  - Solutions: KV cache optimization, speculative decoding
- Memory constraints
  - Hosting LLMs requires high VRAM (A100)
  - Solutions: Model partitioning, CPU/RAM offloading. Ray could be used. 
    - vLLM can partition big LLM models to multiple hosts while ollama can only use multiple GPUs in the same host.
    - LWS can load large model from disk with different participant parallel.
      - chunk-based deduplication, Huggingface Xet-core
- Scalability & Cost
  - Running inference at scale is expensive
  - Solutions: MoE (Mixture of Experts), distillation (small models like LLama-7B)
- Token Streaming & Throughput
  - Autoregressive decoding is slow for real-time applications
  - Solutions: FlashAttention, transformer batching
- Latency and flexibility trade-off
- Guardrails control


## LLM training
[The Ultra-Scale Playbook: Training LLMs on GPU Clusters](https://huggingface.co/spaces/nanotron/ultrascale-playbook?section=high_level_overview)



## 🧩 **ML Platform and Infrastructure**

### 1. **Google's internal ML training platform**

-   **Components**: Job scheduler (Kubernetes/Borg), GPU/TPU clusters, data ingestion pipelines, distributed training libraries (TensorFlow/JAX), experiment tracking.
    
-   **Techniques**: Gang scheduling, resource isolation, checkpointing for fault tolerance, automated hyperparameter tuning.
    
-   **Trade-offs**: Scheduling fairness vs. utilization; training speed vs. cluster resource constraints.
    

----------

### 2. **Distributed training across thousands of GPUs/TPUs**

-   **Components**: Parameter server, AllReduce collective algorithms, TensorFlow/JAX distributed runtime.
    
-   **Techniques**: Synchronous vs. asynchronous training, sharding models across hardware.
    
-   **Trade-offs**: Communication overhead vs. scalability; synchronous consistency vs. asynchronous throughput.
    

----------

### 3. **Scalable ML inference infrastructure**

-   **Components**: Load balancer, inference servers (TensorFlow Serving/Triton), auto-scaler, feature store integration.
    
-   **Techniques**: GPU batching, model quantization, predictive scaling, Canary and A/B deployments.
    
-   **Trade-offs**: Latency vs. resource utilization; accuracy vs. inference speed.
    

----------

### 4. **Multi-region ML deployment system**

-   **Components**: Model registry, deployment pipeline (CI/CD), region-based serving clusters, automated monitoring and rollback.
    
-   **Techniques**: Blue-green deployments, automated validation checks, gradual rollouts.
    
-   **Trade-offs**: Deployment speed vs. reliability; regional latency vs. complexity.
    

----------

### 5. **Efficient GPU/TPU resource management and scheduling**

-   **Components**: Resource manager (Borg/Kubernetes scheduler), quota systems, preemption management.
    
-   **Techniques**: Bin-packing scheduling, predictive autoscaling, multi-tenant isolation.
    
-   **Trade-offs**: Fairness vs. utilization; simplicity of scheduling logic vs. efficiency.
    

----------

## 📊 **Data Infrastructure and Management**

### 6. **Scalable feature store**

-   **Components**: Offline store (BigQuery), online store (Redis, Bigtable), feature transformation pipelines, metadata registry.
    
-   **Techniques**: Point-in-time correctness, feature backfilling, streaming joins.
    
-   **Trade-offs**: Freshness vs. latency; complexity of joins vs. speed.
    

----------

### 7. **Scalable ML data ingestion pipeline**

-   **Components**: Data ingestion (Kafka, Pub/Sub), ETL pipelines (Dataflow, Spark), data lake (GCS).
    
-   **Techniques**: Event-driven ingestion, batch vs. streaming pipelines, schema evolution.
    
-   **Trade-offs**: Real-time processing vs. cost/complexity; schema flexibility vs. consistency.
    

----------

### 8. **Dataset management and versioning system**

-   **Components**: Versioned data lake, lineage metadata store, DVC-like versioning system.
    
-   **Techniques**: Hash-based data versioning, automated lineage tracking, metadata tagging.
    
-   **Trade-offs**: Storage overhead vs. reproducibility; flexibility vs. complexity of lineage tracking.
    

----------

## 📈 **Monitoring, Validation, Observability**

### 9. **Real-time monitoring and alerting for ML pipelines**

-   **Components**: Prometheus, Grafana, anomaly detection services, alerting system.
    
-   **Techniques**: Data drift detection, real-time anomaly detection (isolation forest, statistical methods).
    
-   **Trade-offs**: Alert sensitivity vs. alert fatigue; complexity of monitoring pipeline vs. reliability.
    

----------

### 10. **Observability platform for ML workflows**

-   **Components**: OpenTelemetry, distributed tracing (Jaeger), structured logging.
    
-   **Techniques**: End-to-end request tracing, correlation IDs, ML-specific tracing spans.
    
-   **Trade-offs**: Overhead of detailed tracing vs. debugging benefits; logging verbosity vs. storage costs.
    

----------

## 🛠️ **Model Lifecycle Management**

### 11. **End-to-end ML experimentation system**

-   **Components**: Experiment tracking (MLflow/Kubeflow), hyperparameter optimization (Vizier), metadata DB.
    
-   **Techniques**: Automated model comparison, experiment reproducibility via containers.
    
-   **Trade-offs**: Flexibility vs. reproducibility constraints; automation level vs. experiment freedom.
    

----------

### 12. **Automated ML model validation system**

-   **Components**: Validation suite, automated testing frameworks, continuous deployment pipeline.
    
-   **Techniques**: Canary deployments, automated regression testing, rollback automation.
    
-   **Trade-offs**: Validation thoroughness vs. deployment velocity; automation complexity vs. reliability.
    

----------

### 13. **Continuous training and delivery (CT/CD) pipeline**

-   **Components**: Training orchestration (Airflow/Kubeflow Pipelines), CI/CD (Jenkins/Cloud Build), artifact registry.
    
-   **Techniques**: Incremental retraining, automated deployment triggers, continuous monitoring loops.
    
-   **Trade-offs**: Pipeline complexity vs. deployment agility; frequent deployments vs. model stability.
    

----------

## 🔒 **Security and Compliance**

### 14. **Secure ML infrastructure**

-   **Components**: IAM, workload identity, data encryption (KMS), audit logs.
    
-   **Techniques**: Zero-trust access, secure enclave computing, resource isolation (namespaces/projects).
    
-   **Trade-offs**: Security overhead vs. usability; granular security vs. management complexity.
    

----------

### 15. **Audit and compliance framework**

-   **Components**: Audit log store (BigQuery), compliance reporting dashboard, access controls.
    
-   **Techniques**: Data lineage for compliance, automated policy enforcement, audit trails.
    
-   **Trade-offs**: Audit granularity vs. storage cost; compliance flexibility vs. complexity.
    

----------

## ⚙️ **Efficiency, Optimization, Cost Management**

### 16. **Optimizing ML workloads**

-   **Components**: Workload analyzer, resource optimizer, profiling tools.
    
-   **Techniques**: GPU profiling, mixed-precision training, intelligent autoscaling.
    
-   **Trade-offs**: Optimization gains vs. analysis overhead; complexity of optimizations vs. practical improvements.
    

----------

### 17. **ML infrastructure cost analytics and optimization**

-   **Components**: Cost dashboards, optimization recommendation engine, automated rightsizing.
    
-   **Techniques**: Usage forecasting, spot instances utilization, automated shutdown policies.
    
-   **Trade-offs**: Cost savings vs. resource availability; optimization aggressiveness vs. operational stability.
    

----------

## 🌐 **Open-ended Strategic Questions**

### 18. **Proposing new ML infrastructure problem**

-   **Problem**: **Automated ML governance platform**  
    Centralized management of ML models to ensure compliance, fairness, transparency, and operational integrity at scale.
    

----------

### 19. **Strategic roadmap for next 5 years**

-   **Priorities**:
    
    -   Scale TPU utilization efficiently.
        
    -   Invest in automated ML governance.
        
    -   Expand multi-region model serving infrastructure.
        
    -   Enhance real-time monitoring and observability.
        
-   **Reasoning**: Aligns with Google's long-term growth, regulatory demands, and resource efficiency goals.
    

----------

### 20. **Migrating to new hardware technologies**

-   **Approach**:
    
    -   Establish benchmark suites across current infrastructure.
        
    -   Incremental migration with dual deployments.
        
    -   Create tooling for automated migration and validation.
        
-   **Trade-offs**: Migration complexity and temporary operational overhead vs. long-term performance/cost benefits.
    

----------

## 🌟 **Strategic vs. Tactical Contribution**

Throughout these answers, there’s emphasis on a **strategic approach** to ML infrastructure:

-   **Long-term scalability & cost control**
    
-   **Robust compliance and governance**
    
-   **Automation for productivity and reliability**
    
-   **Balancing technical complexity with operational simplicity**
    

These answers provide strategic thinking beyond tactical execution, aligning closely with Google's expectations for senior-level roles.