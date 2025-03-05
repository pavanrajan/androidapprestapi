# question number 1)

# Write a regex to extract all the numbers with orange color background from 
# the below text in italics (Output should be a list).

# Answer:

import re

# Provided text
text = """{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}"""

# Regex pattern to extract specific numbers
pattern = r'(?<="id":)(1|2|3|4|5|6|7|8|9|10)(?=\})'

# Find all matches
matches = re.findall(pattern, text)

# Print the result
print(matches)

# Problem Set 3
# A. Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a 
list of ISINs every 24 hours). Why did you choose it? Is it reliable enough; Or will it scale? If not, what are the problems
with it? And, what else would you recommend to fix this problem at scale in production?

# Answer:

A system to schedule periodic tasks is a mechanism that enables specific actions or processes to occur at 
regular intervals. These tasks can include activities like data scraping, backups, sending reminders, or refreshing data.

Key Components of a Periodic Task Scheduler
1,Task Scheduling Software
2,Task Definition
3,Scheduling Rules
4,Execution Environment
5,Task Execution
6,Monitoring and Logging

I Choose Celery

Why Choose Celery?
Flexibility: Celery excels at handling periodic tasks and can integrate seamlessly 
with frameworks like Django (which aligns with your experience).

Asynchronous Processing: Celery supports both task scheduling (via celery-beat) and 
asynchronous job execution, allowing for high versatility.

Task Reliability: Using a robust message broker like Redis ensures that tasks are 
queued and retried upon failures.

Ease of Use: The integration of Celery with celery-beat provides periodic scheduling
capabilities, making it a simple yet effective solution.

Is it Reliable Enough?
Yes, Celery is a mature and battle-tested library with a large community. It has proven 
reliability in production environments.

Will it Scale?
Celery can scale horizontally by adding more workers, which makes it suitable for moderate workloads. 
However, scalability largely depends on how you configure it and the infrastructure in place.

Potential Problems

High Broker Load: 
Redis or RabbitMQ may become a bottleneck if the task queue grows excessively.

Difficult Debugging:
Debugging distributed tasks can be challenging without proper observability tools.

Complexity: 
Celery's complexity increases when you start dealing with task dependencies or long-running tasks.

Alternative Recommendations for Scaling in Production

Use Kubernetes for Autoscaling:
        Deploy Celery workers in Kubernetes pods to handle task spikes.
        Auto-scale based on CPU/memory usage or queue length.

Use a More Lightweight Alternative:
        RQ (Redis Queue): If Redis is already in use and your workload doesn't 
        require all the features of Celery.
        Dramatiq: A simpler message broker with built-in support for Redis.

Event-Driven Architecture:
        Use tools like Apache Kafka for streaming data and event-driven task execution. 
        This is better for high-throughput systems.

Serverless Functions:
        Tools like AWS Lambda or Google Cloud Functions can handle periodic tasks without the need
        to maintain a dedicated task scheduler.

Database-Based Scheduling:
        For simpler use cases, rely on database-scheduling solutions like Django's management commands 
        combined with cron jobs or APScheduler.

# B:In what circumstances would you use Flask instead of Django and vice versa? 

# Answer

Use Flask When:

You Need Simplicity and Flexibility:
        Flask is minimalistic and doesn't enforce a specific structure, allowing

you to design your application the way you prefer.

The Project is Small or Prototyping:
        Flask is great for creating small projects, single-page applications,
or prototypes where rapid development is key.

You Need High Customization:
        Flask is best when you require fine-grained control over components
like routing, authentication, and database integration.

You Don't Need a Lot of Built-In Features:
        If your project only requires basic functionalities like routing, 
request handling, and a few API endpoints.

You Want to Learn the Core Concepts of Web Development:
        Because Flask is minimal, it's an excellent choice for learning and
understanding how web frameworks work internally.

