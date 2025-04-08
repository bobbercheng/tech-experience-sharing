Google System Design Interview Questions (Senior Level)
# Design a web system to sell concert tickets.


https://serhatgiydiren.com/preparation-guide-for-tech-interviews/#:~:text=Example%20Front%20End%20UI%20Web,system%20to%20sell%20concert%20tickets

This is a typical distributed resource allocation and transaction system.

For distributed transaction I use idempotent with session management. I use sage to rollback failed transactions.
For resource allocation I use pessimistic lock.
I use state machine to manage each seat status with available/reserved/confirmed/sold

In the begin, order model initializes all seat status as available.

For frontend, we use react+nextjs with REST API call to BE services (order, pay)

There is session management and authentication between FE and BE. I use google OAuth for authentication. All BE rest API is protected by token. Session management and authorization are implemented as a FE module. FE also implement API proxy for authentication.

After the use login with session management, session management issues a session id that can be use as idempotent id.

When a reserve request comes, order module acquire lock, select available seats by filter available status, use radom policy to pick up 10 then update these seats as reserved, finally release the lock. Order module also create a reservation detail with all seats for the use. An reservation also has status as init/paid/cancelled

FE shows seats layout with 10 pickup for user confirmation. If the use okay for 10 seats, it call order module to confirmed it. Order module just check all seat status as reserved as confirmation then update all seat as confirmed otherwise cannot confirm the reservation. After order confirmation, it call pay module to pay for it. After pay module complete payment, it will call order model to update order to paid. If the oder cannot be confirmed, the session become invalid and redirect to new session. If user not okay for current pick, it cancel the reservation and restart new reservation again.


Order module runs cron job to release reserved seats with the lock if last it passes 2 minutes after last update time.


Order APIs:
- reserve 10 seats
- get the reservation detail
- cancel the reservation
- confirm the reservation
- delivery the reservation after pay

All update API writes audit logs.

The order API can be scaled up to running in many containers like GCP pod.

For DB, we can use either relation DB like Postgres or NOSQL db like bigtable.

I can add activity tracking between FE and BE if fraud protection is needed. I can add FIFO wait queue with session management if there are massive users.

To improve performance, we can use redis cache for both seats indexed by seat no and reservations id.

The use is safe to retry with session id.

For monitoring and operational excellence, I use Grafana and OpenTelemetry/Prometheus to monitor performance.


## ChatGPT
**Key considerations:**

-   High concurrency (ticket release windows)
    
-   Prevent overselling
    
-   Fairness (first come, first served)
    
-   Bot protection
    

**Components:**

-   Load balancer
    
-   CDN for static assets
    
-   Web servers + Application logic
    
-   Database (PostgreSQL/MySQL) with row-level locking
    
-   Distributed Cache (e.g. Redis) for inventory lookup
    
-   Message Queue (Kafka) for order processing
    
-   Rate limiting service
    

**Special Techniques:**

-   Optimistic locking or atomic counters
    
-   CAPTCHA for bot prevention
    
-   Queue-based ticket reservation flow
    
-   Use Redis for short-term locks


# Design Google Docs backend for real-time collaboration. ￼
https://www.designgurus.io/answers/detail/what-is-a-google-system-design-interview
- See other's change in real time.
- Latency requirement - API interface. REST, web socket or both
- Document management
    - Permission
- Document collaboration session management.
    - Individuate change
    - Mixed change
- Document change log storage.

## ChatGPT

**Key considerations:**

-   Real-time updates
    
-   Conflict resolution
    
-   Scalability
    
-   Latency
    

**Components:**

-   WebSocket or gRPC bi-directional stream
    
-   Operational Transformation (OT) or CRDT
    
-   Document store (e.g. Google Cloud Spanner, BigTable)
    
-   Pub/Sub for change notifications
    
-   Presence service
    

**Special Techniques:**

-   Delta syncs
    
-   Snapshotting with change logs
    
-   Document-level sharding
    
-   Versioning and rollback


# Design Google Drive. ￼
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network
- FE client / SDK
- API interface
- Store/fetch/manage files
- File usage stats/recommendation
- Sharing files
- Quota/subscription management

Challenges:
- Data volume
- Reliability
- Security/Privacy
- Cost



## ChatGPT

**Key considerations:**

-   File storage
    
-   Access control and sharing
    
-   Versioning
    
-   Offline support
    

**Components:**

-   Metadata service (document tree, permissions)
    
-   Blob store (GCS, S3)
    
-   Indexing service (full-text search)
    
-   Sync client
    
-   Auth service (OAuth, ACLs)
    

**Techniques:**

-   Chunked uploads
    
-   Delta sync
    
-   Encryption at rest and in transit
    
-   Change journal for updates

# Design Google Calendar. ￼
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network
PRD:
- Even scheduling
- Multiple views
- Calendar sharing
- Check availability
- Google meeting integration
- Integration
- Multiple calendar

## ChatGPT

**Key considerations:**

-   Recurring events
    
-   Notifications and reminders
    
-   Invite and RSVP
    
-   Time zone handling
    

**Components:**

-   Calendar service (CRUD APIs, recurrence engine)
    
-   Notification service (Email, SMS, Push)
    
-   Time zone conversion module
    
-   User directory service
    

**Data modeling:**

-   Separate event metadata and recurrence rules
    
-   Index by user ID and time
    
-   Caching for recent events


# Design Google Maps. ￼
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network
PRD:
- Show Map with places
- Show my location
- Find places
- Direction
- Dynamic traffic
- Update map

## ChatGPT

**Key considerations:**

-   Geospatial queries
    
-   Traffic data
    
-   Real-time updates
    
-   Scalability
    

**Components:**

-   Tile server (for maps display)
    
-   Geocoding and reverse geocoding service
    
-   Routing engine (Dijkstra/A*)
    
-   Traffic service (stream processing)
    
-   Spatial DB (PostGIS, BigTable + S2 geometry library)


# Design YouTube. ￼
https://www.designgurus.io/answers/detail/what-is-a-google-system-design-interview

Youtube includes:
- Upload video
    - video transform/compression
    - storage/chunk
- Watch video
    - stream video
    - video engagement
- Video recommendation
- Realtime video
    - real time streaming
- Ads/Monetization 
- Analysis/Dashboard

Challenges/tech solutions:
- Scalability: 
    - CDN
    - Streaming tech
    - Live Stream servers in regions

## ChatGPT

**Key considerations:**

-   Video upload, processing, and streaming
    
-   Recommendation engine
    
-   Content moderation
    
-   Monetization
    

**Components:**

-   Upload service (transcoding pipeline)
    
-   CDN for delivery
    
-   Metadata and search service
    
-   Comments and user interaction services
    
-   Ads platform integration

# Design Twitter. ￼
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network

[Twitter's Recommendation Algorithm](https://blog.x.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm)

[Twitter's Recommendation Algorithm from Code](https://bobbercheng.github.io/blog/ml/2025/04/04/twitter-recommendation.html)

## Requirement
- Provide timeline tweets post for billon users
- distill about 500 million tweets to a handful of top tweets on your timeline
- Balance in-network sources and out-of-network sources
- filter I saw, NSFW etc.
- increase diversity etc.
- mix ads, features etc
- rank

## Challenge
- Lots of users, tweets, engagements

## ChatGPT

**Key considerations:**

-   Timelines
    
-   Mentions, hashtags
    
-   Rate limits
    
-   Search indexing
    

**Components:**

-   Tweet service (write-heavy, fan-out model)
    
-   User timeline service (precomputed vs dynamic)
    
-   Notification service
    
-   Inverted index for search
    

**Storage:**

-   Tweets: Cassandra/BigTable
    
-   User Graph: Redis/Graph DB
    
-   Timeline cache: Redis


# Design a search engine.
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network

## ChatGPT

**Key considerations:**

-   Web crawling
    
-   Indexing and ranking
    
-   Query suggestions
    

**Components:**

-   Crawler (distributed agents)
    
-   Indexer (inverted index, sharded)
    
-   Ranker (BM25, PageRank)
    
-   Query engine (auto-complete, spell check)
    

**Storage:**

-   Document store
    
-   Inverted index (Lucene/Solr/ElasticSearch)

# Design the server infrastructure for Gmail.
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network

## ChatGPT

**Key considerations:**

-   Storage efficiency
    
-   Spam filtering
    
-   Real-time delivery
    
-   Search
    

**Components:**

-   SMTP/IMAP gateway
    
-   Mail delivery agent
    
-   Storage (e.g. mailbox shards)
    
-   Spam filter service
    
-   Indexing for fast search
    

**Techniques:**

-   Deduplication
    
-   Quota enforcement
    
-   Threading logic (conversations)

# Design a system that displays advertisements next to search results (based on keywords).
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network

## ChatGPT

**Key considerations:**

-   Keyword targeting
    
-   Bid auction model
    
-   Real-time latency
    
-   Click tracking
    

**Components:**

-   Ad matching engine (match query to keywords)
    
-   Auction engine (choose highest bids)
    
-   Delivery system (track impressions, clicks)
    
-   Budget management service
    

**Techniques:**

-   Index ads by keyword
    
-   Use real-time bidding algorithms
    
-   Fraud detection service

# OpenAI


### an in-memory database


### 1. Design a ride-sharing system (e.g., Uber/Lyft)

**Key considerations:** Matching, location indexing, fairness, dynamic pricing **Components:**

-   Location service (spatial indexing using S2 or Geohash)
    
-   Matching service (pub/sub + priority queues)
    
-   Pricing engine (real-time supply/demand)
    
-   Trip management and billing
    

**Techniques:**

-   Use Redis or Cassandra for geo queries
    
-   Stream trip logs via Kafka
    
-   Async matching with ML-based ETA predictions
    

----------

### 2. Design an LLM-powered enterprise search platform

**Key considerations:** Latency, context injection, semantic ranking **Components:**

-   Ingestion pipeline (documents, metadata)
    
-   Vector index (FAISS/Weaviate)
    
-   Retriever + reranker model
    
-   Query frontend with embedding generation
    

**Techniques:**

-   Hybrid retrieval (BM25 + semantic)
    
-   Prompt engineering for query + context fusion
    
-   Caching and rate limiting
    

----------

### 3. Design a webhook/event notification system

**Key considerations:** Reliability, retries, ordering **Components:**

-   Event producer + router
    
-   Delivery queue
    
-   Retry scheduler (exponential backoff)
    
-   Audit logging
    

**Techniques:**

-   Use HTTP 2 + webhook signature verification
    
-   Store undelivered events with TTL for retry
    
-   Dashboard for delivery status


# Anthropic

### 1. Design an autoscaling inference system for LLMs

**Key considerations:** GPU resource usage, latency, concurrency **Components:**

-   Inference gateway
    
-   Model server cluster
    
-   Autoscaler (based on queue depth, load)
    
-   Token budget tracker
    

**Techniques:**

-   Use batching to improve GPU utilization
    
-   Implement warm pools of models
    
-   Load shed via backpressure
    

----------

### 2. Design a secure system for human feedback collection

**Key considerations:** Privacy, UX, consistency, logging **Components:**

-   Frontend task interface
    
-   Feedback submission service
    
-   Secure data store
    
-   Reviewer dashboard
    

**Techniques:**

-   Encrypt feedback at client level
    
-   Store provenance info (who/when/what)
    
-   Differential privacy or anonymization for analysis
    

----------

### 3. Design a logging pipeline for billions of LLM interactions/day

**Key considerations:** Volume, indexing, query performance **Components:**

-   Log collector (e.g., FluentBit)
    
-   Stream processor (Kafka + Flink)
    
-   Indexing and search engine (ClickHouse, Elastic)
    
-   Data lake for cold storage (S3 + Iceberg)
    

**Techniques:**

-   Partition logs by time + tenant
    
-   Use columnar formats (Parquet)
    
-   Async aggregation jobs for analytics


# DeepMind


### 1. **Design a system to train a reinforcement learning (RL) agent at scale**

#### 🧱 Core Components

-   **Simulation workers (envs)**
    
-   **Learner nodes (model trainers)**
    
-   **Replay buffer (experience storage)**
    
-   **Parameter server**
    
-   **Coordination & scheduling service**
    

#### ⚙️ Techniques

-   **Distributed RL framework** like IMPALA or R2D2
    
-   **Experience prioritization** (PER)
    
-   **gRPC for fast inter-node communication**
    
-   **TensorFlow or JAX with XLA for performance**
    

#### 🔁 Trade-offs

-   **On-policy vs off-policy**: On-policy has fresher data, off-policy is more sample-efficient.
    
-   **Centralized vs decentralized replay**: Centralized is simpler but bottlenecked.
    
-   **Synchronous vs asynchronous updates**: Sync is stable, async is fast but harder to debug.
    

----------

### 2. **Design a distributed GPU job scheduler for large ML workloads**

#### 🧱 Core Components

-   **Job submission API**
    
-   **Cluster state tracker**
    
-   **Resource allocator**
    
-   **Execution agents (e.g., Kubernetes pods)**
    
-   **Priority & preemption logic**
    

#### ⚙️ Techniques

-   **Fair-share + priority queues**
    
-   **Node labeling for GPU type**
    
-   **Gang scheduling** for multi-GPU jobs
    
-   **Checkpointing for preempted jobs**
    

#### 🔁 Trade-offs

-   **Utilization vs fairness**: Higher utilization may starve some jobs.
    
-   **Preemption vs job progress**: Preemption adds overhead.
    
-   **Bin-packing vs speed**: Better GPU packing takes time to calculate.
    

----------

### 3. **Design a multi-modal data platform (text + image + video)**

#### 🧱 Core Components

-   **Ingestion layer**
    
-   **Schema service with modality metadata**
    
-   **Storage backends: blob store (S3/GCS) + DB for metadata**
    
-   **Indexing and search service**
    
-   **Data versioning**
    

#### ⚙️ Techniques

-   **Unified metadata schema across modalities**
    
-   **Deduplication by perceptual hashing**
    
-   **Content filtering pipeline**
    
-   **Lazy loading & partial retrieval (e.g., video frames)**
    

#### 🔁 Trade-offs

-   **Storage cost vs retrieval latency**
    
-   **Strict schema vs flexibility**: Unified schema simplifies pipeline, but can restrict features.

# Design a scientific research data platform with version control and collaboration


# 🧠 Meta (AI/FAIR teams)

### 1. Design a large-scale recommendation engine

**Key considerations:** Latency, personalization, freshness **Components:**

-   Feature store (real-time + batch)
    
-   Candidate generator
    
-   Ranking model service
    
-   Logging and feedback loop
    

**Techniques:**

-   Train embeddings for users/items
    
-   Use caching layers for hot items
    
-   Click-through-rate prediction model
    

----------

### 2. Design a feature store for ML models

**Key considerations:** Reusability, consistency, low latency **Components:**

-   Online store (Redis/Cassandra)
    
-   Offline store (S3 + Hive)
    
-   Transformation engine
    
-   Registry and versioning
    

**Techniques:**

-   Materialize features ahead of time
    
-   Join feature values by entity IDs
    
-   Time-travel support for backtesting
    

----------

### 3. Design a distributed training system for billion+ parameter models

**Key considerations:** Scalability, fault tolerance, throughput **Components:**

-   Trainer orchestrator (Horovod, DeepSpeed)
    
-   Parameter sharding and checkpointing
    
-   Gradient accumulator
    
-   Elastic cluster manager
    

**Techniques:**

-   Pipeline + data parallelism
    
-   Mixed precision + gradient clipping
    
-   TensorBoard/metrics tracking


🧪 Cohere / Mistral / Inflection AI
Design a system to serve embedding-as-a-service at scale

Design a caching system for frequently queried vector search results

Design an API rate-limiting gateway with customer-specific SLAs

Design a low-latency chat system with streaming LLM responses

📊 Scale AI / Weights & Biases / Hugging Face
Design a labeling platform to support real-time data annotation

Design a dashboard system for tracking experiment metrics over time

Design a scalable backend for running thousands of fine-tuning jobs

Design a system to evaluate LLM model performance across benchmarks


# 🧮 Open-Source ML Infra Projects (e.g., Ray, Kubeflow, MLFlow)

# Design a DAG-based ML pipeline orchestration system (e.g., like Airflow but real-time)
**Key considerations:** 
- Real-time execution,
- dependency resolution
- retries
- logging 

**Components:**
- Workflow/DAG engine
- Job Queue
- DB
- UI/Monitor
- Plugin system for extension
    

**Techniques:**
- Use task queue/retry
- Persist internal states to DB
- Support task parallels, priorities
- Integrate logging/tracking/Telemetry tools


# Design a distributed parameter server for model training

**Key considerations:** 
- Parameter synchronization, consistency, scalability

**Components:**
- Workers(trainers)
- Parameter servers (stateful services)
- Synchronization protocol (Async vs. Sync SGD)
- Load balancer
    

**Techniques:**
- Use gRPC or custom RPC for update
- shard parameters across servers
- Implement staleness-tolerant updates (e.g. SSP)
- Snapshot and restore functionality

# Design a plugin-based system for experiment tracking (like MLFlow)

#### 🧱 Core Components

-   **Tracking server (API + UI)**
    
-   **Artifact store**
    
-   **Metrics DB**
    
-   **Plugin interface for custom loggers**
    

#### ⚙️ Techniques

-   **Immutable run records**
    
-   **Versioning via run UUIDs**
    
-   **Plugin hooks: before_run, after_run, on_error**
    
-   **Offline logging mode**
    

#### 🔁 Trade-offs

-   **Centralized vs decentralized logging**: Centralized is easier to manage; decentralized is more resilient.
    
-   **Flat vs nested experiment metadata**: Nested improves organization but complicates queries.

# Design a model reproducibility and lineage tracking service

#### 🧱 Core Components

-   **Model registry**
    
-   **Data source lineage system**
    
-   **Experiment config snapshots**
    
-   **Audit logs + hashes**
    

#### ⚙️ Techniques

-   **Hash every component (code, data, env)**
    
-   **Immutable model versions**
    
-   **Integration with git and DVC**
    
-   **Graph-based lineage explorer**
    

#### 🔁 Trade-offs

-   **Auditability vs overhead**: Full snapshots are reliable but slow.
    
-   **Strict versioning vs dev velocity**: May slow fast iteration.

# Kubernetes
## Extending Kubernetes
[Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/)

7 extension points:
- Plugins
- API Access Extensions
- API extensions
- Scheduling extensions
- Controllers
- Network Plugins
- Device Plugins