\# DevOpsHub - Feedback Collection System



\## Project Overview

\[cite\_start]This project is a microservices-based feedback system developed for "DevOpsHub" startup\[cite: 6]. \[cite\_start]It consists of two main applications interacting with a shared Redis database to collect user messages and track page visits\[cite: 14, 15].



\## Architecture Description

\[cite\_start]The system follows a \*\*Producer-Observer\*\* pattern\[cite: 15]:

\* \*\*App 1 (Message Collector):\*\* Acts as a \*\*Producer\*\*. \[cite\_start]It increments a visit counter in Redis on every page load and adds user messages to a Redis list\[cite: 15].

\* \*\*App 2 (Dashboard):\*\* Acts as an \*\*Observer\*\*. \[cite\_start]It retrieves the total message count and total visit count from Redis to display them on a dashboard\[cite: 15].

\* \[cite\_start]\*\*Redis:\*\* Central database for data persistence and communication between services\[cite: 9, 18].



\## Prerequisites

\* \[cite\_start]Docker and Docker Compose installed\[cite: 27].

\* Python 3.x (used for application development).



\## How to Run

1\. Navigate to the project root directory `cloudandDevop`.

2\. Run the following command:

&#x20;  ```bash

&#x20;  docker-compose up --build -d

Access InstructionsMessage Collector (App 1): http://localhost:5000   Dashboard (App 2): http://localhost:5001   Technologies UsedDocker \& Docker Compose (Containerization)   Redis (Data Persistence \& Message Queue)   Python Flask (Web Framework)

\---







\## Student Information

\- \*\*Name:\*\* \[Your Name]

\- \*\*ID:\*\* \[Your ID]



&#x20; 

