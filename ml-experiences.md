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
- Fintech: AUC, KS, binary classification
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
- TensorRT/ONNX Runtime: converts model for optimized GPU inference
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
  - Solutions: Model partitioning, CPU/RAM offloading
- Scalability & Cost
  - Running inference at scale is expensive
  - Solutions: MoE (Mixture of Experts), distillation (small models like LLama-7B)
- Token Streaming & Throughput
  - Autoregressive decoding is slow for real-time applications
  - Solutions: FlashAttention, transformer batching
- Latency and flexibility trade-off
- Guardrails control

## Thanks
Lan, Kai, Yuhan