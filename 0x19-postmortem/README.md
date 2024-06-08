Postmortem Report: Web Service Outage
Issue Summary
Duration:
Start: June 7, 2024, 14:00 UTC
End: June 7, 2024, 16:30 UTC

Impact:
Our primary web service was unavailable for approximately 2.5 hours. During this period, 85% of users experienced either complete downtime or significantly degraded performance. Users were unable to access the website, leading to failed transactions and a considerable number of support tickets.

Root Cause:
The root cause was a misconfiguration in the load balancer, which led to an overload on a subset of backend servers, causing them to crash and resulting in the service outage.

Timeline
14:00 UTC: Issue detected by an automated monitoring alert indicating high error rates.
14:05 UTC: On-call engineer confirmed the issue by checking the monitoring dashboard and observing high 500 error rates.
14:10 UTC: Initial investigation started, focusing on the backend server logs to identify anomalies.
14:30 UTC: Misleading path pursued; suspected database overload due to error logs pointing to connection failures.
15:00 UTC: Escalated to the infrastructure team after backend server investigation showed no clear issues.
15:15 UTC: Infrastructure team began reviewing load balancer configurations and network traffic patterns.
15:45 UTC: Root cause identified as a misconfiguration in the load balancer.
16:00 UTC: Load balancer configuration corrected and servers restarted.
16:15 UTC: Service functionality restored; monitoring confirmed stability.
16:30 UTC: Full resolution confirmed; service back to normal operation.
Root Cause and Resolution
Detailed Cause:
A recent update to the load balancer configuration introduced an incorrect routing rule, causing uneven distribution of traffic. This resulted in some backend servers receiving an overwhelming amount of requests while others remained underutilized. The overloaded servers experienced resource exhaustion and crashed, leading to the service outage.

Detailed Fix:
The load balancer configuration was reviewed, and the erroneous routing rule was identified and corrected. Specifically, the traffic distribution rules were adjusted to ensure even distribution across all backend servers. After making these changes, the affected servers were restarted, and their health was monitored to confirm the fix.

Corrective and Preventative Measures
Improvements and Fixes:

Review and Patch Load Balancer Configuration: Ensure that all routing rules are correct and tested in a staging environment before deployment.
Enhance Monitoring: Implement more granular monitoring for load balancer performance and backend server load to detect imbalance early.
Redundancy and Failover: Improve redundancy in the backend server pool to prevent a single point of failure from causing widespread outage.
Tasks:

Patch Load Balancer Configuration:

Audit current configuration.
Test updated rules in a staging environment.
Deploy tested configuration to production.
Add Monitoring on Load Balancer:

Set up alerts for uneven traffic distribution.
Implement dashboard views for load balancing metrics.
Increase Backend Server Pool:

Provision additional backend servers.
Update load balancer to include new servers.
Test failover scenarios to ensure stability.
Conduct Incident Response Training:

Organize training sessions for engineers to improve detection and response to similar issues.
Develop runbooks for common infrastructure issues.
By addressing these areas, we aim to prevent recurrence of such incidents and ensure better service reliability for our users.






