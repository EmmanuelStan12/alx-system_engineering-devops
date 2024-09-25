# Postmortem: "The Case of the Vanishing Database" - **CatifyMe Social Network Outage**

### **Issue Summary**  
- **Duration**: The outage lasted from **08:00 AM (PST)** on **September 22, 2024**, to **10:30 AM (PST)** on the same day.  
- **Impact**: Approximately **85%** of users were unable to access the **CatifyMe** platform, the premier social network for cat enthusiasts. Key features like **posting cat pictures**, **liking posts**, and **commenting** were affected. Some users encountered a `404 Database Not Found` error, leading to mass panic among our core user base.  
- **Root Cause**: The root cause was a **misconfigured database failover**, which led to our primary database cluster disappearing from the network. 

### **Timeline**
- **07:45 AM (PST)**: A new deployment was made to improve our database performance.
- **08:00 AM (PST)**: Users began reporting issues via Twitter (and ironically, **CatifyMe**).
- **08:10 AM (PST)**: An engineer received a **PagerDuty alert** from our monitoring system regarding multiple failed database connections.
- **08:15 AM (PST)**: Investigation started with an assumption that the database server was experiencing a high load.
- **08:30 AM (PST)**: The issue was escalated to the **Database Team**, who began troubleshooting the primary database cluster.
- **08:45 AM (PST)**: An attempted restart of the database cluster led to no response; the database server appeared to have vanished from our cloud provider.
- **09:00 AM (PST)**: Misleading assumption: the network team was contacted as it was believed to be a **network connectivity issue**.
- **09:30 AM (PST)**: After extensive checks, the database team noticed a misconfiguration in the **database failover settings**, where the failover pointed to a non-existent server in the **backup configuration**.
- **09:50 AM (PST)**: The database was re-pointed to a valid failover instance, and normal operations resumed.
- **10:30 AM (PST)**: Full functionality was restored, and users were able to post their cats once more.

### **Root Cause and Resolution**  
- **Root Cause**:  
  The problem was triggered by a **misconfigured database failover** during a routine deployment aimed at optimizing database performance. Instead of pointing to the backup database, the failover configuration pointed to a **decommissioned server**. When the primary database experienced a minor issue, the system attempted to failover to the backup, but instead it hit a server that no longer existed, effectively **disappearing** the database from the network. 

- **Resolution**:  
  The team manually updated the failover configuration to point to an active backup database. The system was then restarted, and database connections resumed as expected. A thorough review of the database failover and backup policy was initiated to avoid future incidents.

### **Corrective and Preventative Measures**
- **Improvements**:  
  This incident revealed the need for better failover testing and monitoring. Moving forward, we will:
  1. **Perform regular failover testing** in staging environments to ensure backup systems are correctly configured and functioning.
  2. Implement more **granular monitoring** for database health, including automatic detection of non-existent or decommissioned servers.
  3. Review deployment processes for critical systems to prevent accidental configuration errors.

- **Task List**:
  - **Audit failover configurations** for all databases across environments (ETA: 2 days).
  - **Add monitoring for invalid failover targets** to trigger alerts before incidents (ETA: 1 week).
  - **Automate database failover testing** as part of the CI/CD pipeline (ETA: 2 weeks).
  - **Provide training** for engineers on cloud failover best practices (ETA: 1 month).

### **Conclusion**  
We sincerely apologize to our users who, for 2.5 hours, were left without a place to post pictures of their cats. We are already taking steps to prevent this from happening again and assure you that CatifyMe’s kitten-pic posting capabilities are now as secure as ever. A special shoutout to our support team, who had to field hundreds of panicked emails from cat owners needing their daily dose of likes and upvotes.
