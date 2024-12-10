
# RedisRabbitScheduler

A distributed task scheduler built using **Redis** and **RabbitMQ**, designed for managing and executing tasks in a scalable, efficient, and fault-tolerant manner. This system supports scheduling tasks for future execution using either single dates or recurring schedules (e.g., cron jobs).

## Features

- **Task Scheduling**: Schedule jobs for future execution or recurring intervals.
- **Scalability**: Distributed design enables horizontal scaling.
- **Fault Tolerance**: Combines the reliability of RabbitMQ with Redis for seamless task management.
- **Dockerized Setup**: Ready-to-deploy environment using Docker Compose.

## Prerequisites

- Docker and Docker Compose installed on your system.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/cdchinmoy/RedisRabbitScheduler.git
   cd RedisRabbitScheduler
   ```

2. **Run the Application**:
   Use Docker Compose to build and start the services.
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**:
   - The scheduler and any associated APIs should now be running locally.

## Architecture Overview

1. **RabbitMQ**:
   - Serves as the message broker, handling task messages between producers and consumers.

2. **Redis**:
   - Functions as the backend for scheduling and task queue management.

3. **Flask Server**:
   - Provides a REST API for interacting with the scheduler, including creating, updating, and deleting jobs.

## API Endpoints (Example)

### 1. Create a Scheduled Job
- **Method**: `POST`
- **Endpoint**: `/jobs`
- **Payload**: 
  ```json
  {
    "task": "example_task",
    "schedule": "cron_expression",
    "data": {}
  }
  ```

### 2. Retrieve All Scheduled Jobs
- **Method**: `GET`
- **Endpoint**: `/jobs`

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
