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


## 🚀 **Google AI/ML Infrastructure - Domain Expertise Interview Questions**

### 🧩 **ML Platform and Infrastructure**

1.  **Design Google's internal ML training platform** to efficiently support thousands of researchers training models concurrently.
    
2.  **Design a distributed training system** that scales to thousands of GPUs/TPUs across multiple data centers.
    
3.  **Design a flexible and scalable inference serving infrastructure** for large-scale production ML models, capable of handling millions of requests per second.
    
4.  **Design a multi-region ML model deployment system** with automated model validation, deployment, and rollback mechanisms.
    
5.  **Design an efficient GPU/TPU resource management and scheduling system** for optimizing utilization across teams.
    

----------

### 📊 **Data Infrastructure and Management**

6.  **Design a feature store** to provide low-latency retrieval, feature consistency, versioning, and backfill capabilities across billions of data points.
    
7.  **Design a scalable ML data ingestion pipeline** supporting streaming and batch ingestion, integrated with ML training systems.
    
8.  **Design a dataset management and versioning system** that maintains lineage, reproducibility, and compliance (privacy/GDPR).
    

----------

### 📈 **Monitoring, Validation, and Observability**

9.  **Design a real-time monitoring and alerting system for ML pipelines** to detect data drift, performance degradation, and anomalies in large-scale ML production deployments.
    
10.  **Design an observability platform** to provide end-to-end tracing, logging, and debugging for ML workflows at Google scale.
    

----------

### 🛠️ **Model Lifecycle Management**

11.  **Design an end-to-end ML experimentation system** that handles experiment tracking, A/B testing, hyperparameter tuning, reproducibility, and collaboration.
    
12.  **Design a robust automated ML model validation system** capable of evaluating and deploying hundreds of models daily, with automated fallback mechanisms.
    
13.  **Design a continuous training and delivery pipeline (CT/CD)** for ML models, including retraining, testing, deployment, and monitoring at Google scale.
    

----------

### 🔒 **Security and Compliance**

14.  **Design a secure ML infrastructure** ensuring isolation and security of data, models, and infrastructure across multiple teams and regulatory requirements.
    
15.  **Design an audit and compliance framework** integrated into ML infrastructure, supporting data access controls, privacy constraints, and governance policies at global scale.
    

----------

### ⚙️ **Efficiency, Optimization, and Cost Management**

16.  **Design a system for optimizing ML workloads** to improve resource utilization, reduce training/inference latency, and minimize cloud resource costs.
    
17.  **Design a ML infrastructure cost analytics and optimization platform** to provide visibility, recommendations, and automation of cost control across large ML infrastructure clusters.
    

----------

### 🌐 **Open-ended Strategic Questions**

18.  **Propose a new problem in ML infrastructure** at Google scale that can significantly improve developer productivity and model deployment efficiency.
    
19.  **How would you design a strategic roadmap** for Google's ML infrastructure for the next 5 years? What problems would you prioritize, and why?
    
20.  **Describe how you would handle migrating Google's large-scale ML systems** to new hardware technologies (e.g., next-generation TPUs) or cloud-native platforms.
    

----------

These questions assess your:

-   **Deep technical expertise** in large-scale ML infrastructure.
    
-   **Strategic thinking** vs. purely tactical approaches.
    
-   **Capability to address large-scale, complex, and ambiguous problems** requiring cross-team collaboration.
    
-   **Ability to propose novel solutions and new areas of innovation** within the ML infrastructure domain.