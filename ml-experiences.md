# Domain: Search and Recommendation (E-commerce)

Refer to discussion with Lan.

## ML Model Metrics

### Offline Metrics
- **Retrieval**: Recall, nDCG
- **Rerank**: MRR, AUC

### Online Metrics
- **Positive Metrics**
  - CTR (Click-Through Rate)
  - ATC (Add-to-Cart)
  - Purchase Rate
- **Negative Metrics**
  - Exit Rate
  - Zero Result Rate

### Improvements
- Multi-task training to mitigate gap between business and training objectives (MMoE, PLE)
- Teacher-student model approach: Learning from downstream model instead of ground truth

## Feature Store Management

### Feature Types
- **Static Features**
  - User profile embeddings
  - Document embeddings
- **Dynamic Features**
  - Context features
  - In-session information

### Challenges
- Latency vs accuracy trade-offs (larger embeddings → more accurate but slower)
- Granularity optimization (cluster numbers, time windows)
- Feature consistency between training and serving (logging)
- Missing data handling

## GPU Cluster Performance Optimization
- Vector quantization
- Caching and batching

## LLM Inference Challenges
- Latency and flexibility trade-off
- Guardrails control

# Domain: Recommendation

Refer to discussion with Luokkk

## ML Model Metrics and Improvements
### ML  Metrics
For classification with imbalanced data, we use Precision, Recall, F1. We use log loss to measure logistic output.
For Regression, we use RMSE, MSE.
For Ranking, we use NDCG, MAP, MRR
For LLM text generation, we use BLEU, ROUGE.
For new LLM model, we can use perplexity or human evaluation.

### Improvements
1. Feature engineering: add new features
2. Data augmentation: it covers sampling strategy, synthetic data.
3. Hyperparameter Tuning: we may use neural architecture search (NAS)
4. Model architecture optimization: It depends on task and baseline. We can use change model components for different tasks. e.g. change pre-trained model; use different regularization tech. For quick inference, use compact model. For local deployment, compress model. To increase model precision, increase model capacity.
5. Post-processing: ensemble 



## Feature Store Management
### Feature Types
Fore recommendation:
Raw features: user logs, interactions, transcription history.
Aggregated features: Rolling statistics, trends(7-day engagement, most popular)
Embedding features: Sentence embeddings, graph embeddings
Time serial features: Recency-based scores, session-level features.
Metadata: user side-information (device type, user geolocation), item side-information (content category). 

### Challenges
Data freshness & latency: ensuring near real-time updates while keeping batch and streaming pipelines consistent.
Feature Drift: Models degrading due to distribution shifts in stored features.
High storage & Compute Cost: Managing petabytes of structured/unstructured data efficiently.
Consistency across training & Inference: Need feature serving consistency between batch training and real-time inference. like item embedding, fraud-tagged log
Dependency Management: Keeping track of feature lineage when multiple teams contributes.



## GPU Cluster Performance Optimization

### Model optimization: 
Quantization (FP32 -> FB16 or INT8 for reducing memory footprint)
Pruning (Removing unnecessary layers/weights)
Knowledge distillation (training smaller models with teacher guidance)

### Efficient execution on GPUs:
TensorRT or ONNX Runtime: converts model fro optimized GPU inference.
Batching: Combines multiple requests to maximize GPU throughput.
Asynchronous execution: use async calls to avoid idle GPU time.

### Scaling on GPU Clusters
Triton Inference servers: Enables multi-GPU and multi-model serving.
Kubernetes + GPU Auto-scaling: Deploys dynamic inference workloads efficiently.

## LLM Inference Challenges

### Hight latency
Large models require substantial compute.
Solutions: Use KV cache optimization, speculative decoding for lower response times.

### Memory constraints
Hosting LLMs on GPUS requires high VRAM (A100)
Solutions: partition models across GPUs. offloaded layers to CPU/RAM when needed.

### Scalability & Cost
Running inference at scale is expensive
Solutions: uses MoE(Mixture of Experts), distillation (small models like LLama-7B) for cost reduction.

#### Token Streaming & Throughput issues:
Autoregressive decoding is slow for real-time applications.
Solutions: Use FlashAttention, batching multiple queries in transformer models.