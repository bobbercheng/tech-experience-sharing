# Domain: Search and Recommendation (E-commerce)

Refer to discussion with Lan.

## 1. ML Model Metrics and Improvements

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

## 2. Feature Store Management

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

## 3. GPU Cluster Performance Optimization
- Vector quantization
- Caching and batching

## 4. LLM Inference Challenges
- Latency and flexibility trade-off
- Guardrails control