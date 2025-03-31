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


# Design Google Docs backend for real-time collaboration. ￼
https://www.designgurus.io/answers/detail/what-is-a-google-system-design-interview

# Design Google Drive. ￼
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network

# Design Google Calendar. ￼
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network

# Design Google Maps. ￼
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network

# Design YouTube. ￼
https://www.designgurus.io/answers/detail/what-is-a-google-system-design-interview

# Design Twitter. ￼
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network

# Design a search engine. ￼
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network


# Design the server infrastructure for Gmail. ￼
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network

# Design a system that displays advertisements next to search results (based on keywords). 
https://igotanoffer.com/blogs/tech/google-system-design-interview#:~:text=11,applications%20using%20an%20edge%20network