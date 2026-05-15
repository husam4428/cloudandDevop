# DevOpsHub - Feedback Collection System

## Project Overview

This project is a microservices-based feedback system developed for "DevOpsHub" startup.  
It consists of two main applications interacting with a shared Redis database to collect user messages and track page visits.

---

## Architecture Description

The system follows a **Producer-Observer** pattern:

### App 1 (Message Collector)
Acts as a **Producer**.  
It increments a visit counter in Redis on every page load and adds user messages to a Redis list.

### App 2 (Dashboard)
Acts as an **Observer**.  
It retrieves the total message count and total visit count from Redis to display them on a dashboard.

### Redis
Acts as the central database for data persistence and communication between services.

---

## Prerequisites

- Docker Desktop installed
- Docker Compose enabled
- Python 3.x

---

## How to Run

1. Navigate to the project root directory:
```bash
cd cloudandDevop
Run the containers:
docker-compose up --build -d



Access Instructions
Message Collector (App 1):
http://localhost:5000
Dashboard (App 2):
http://localhost:5001
Technologies Used
Docker & Docker Compose
Redis
Python Flask
Student Information
Name: Hossam Ahmed
ID: 4428
Name: Abdulmuez Essam
ID: 4913
```bash
cd cloudandDevop
