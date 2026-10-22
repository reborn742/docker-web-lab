# Docker Compose Task Manager

A containerized task management web application built with Flask, PostgreSQL, Nginx, and Docker Compose.

## Features

- Create, view, complete, and delete tasks
- Store tasks persistently in PostgreSQL
- REST API built with Flask
- Nginx serves the frontend and reverse-proxies API requests
- Health-check endpoint for application status
- Multi-container deployment using Docker Compose
- Automatic database initialization

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **Web Server / Reverse Proxy:** Nginx
- **Containerization:** Docker and Docker Compose

## Architecture

```text
Browser
   |
   v
Nginx :8080
   |
   v
Flask API :5000
   |
   v
PostgreSQL :5432
```

Nginx serves the frontend and forwards API requests to Flask. Flask communicates with PostgreSQL to store and retrieve tasks. The services communicate through a Docker Compose network.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Run the application

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd docker-web-lab
```

Start the application:

```bash
docker compose up -d --build
```

Open the application in your browser:

http://localhost:8080

### Stop the application

```bash
docker compose down
```

Task data is stored in a named Docker volume. Stopping the containers without deleting that volume preserves the database data.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API and database health |
| GET | `/tasks` | List tasks |
| POST | `/tasks` | Create a task |
| PATCH | `/tasks/<id>` | Update task completion |
| DELETE | `/tasks/<id>` | Delete a task |

## What I Learned

- Containerizing a Python web application
- Configuring services with Docker Compose
- Connecting Flask to PostgreSQL
- Configuring Nginx as a reverse proxy
- Managing container networking and persistent volumes
- Debugging container startup and service connectivity

## Future Improvements

- Environment-based secrets management
- Automated tests
- CI/CD with GitHub Actions
- Improved validation and error handling
- Deployment to a cloud server

---

**Author:** Faisal Rahman
# Docker Compose Task Manager

A containerized task management web application built with Flask, PostgreSQL, Nginx, and Docker Compose.

## Features

- Create, view, complete, and delete tasks
- Store tasks persistently in PostgreSQL
- REST API built with Flask
- Nginx serves the frontend and reverse-proxies API requests
- Health-check endpoint for application status
- Multi-container deployment using Docker Compose
- Automatic database initialization

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **Web Server / Reverse Proxy:** Nginx
- **Containerization:** Docker and Docker Compose

## Architecture

```text
Browser
   |
   v
Nginx :8080
   |
   v
Flask API :5000
   |
   v
PostgreSQL :5432
```

Nginx serves the frontend and forwards API requests to Flask. Flask communicates with PostgreSQL to store and retrieve tasks. The services communicate through a Docker Compose network.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Run the application

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd docker-web-lab
```

Start the application:

```bash
docker compose up -d --build
```

Open the application in your browser:

http://localhost:8080

### Stop the application

```bash
docker compose down
```

Task data is stored in a named Docker volume. Stopping the containers without deleting that volume preserves the database data.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API and database health |
| GET | `/tasks` | List tasks |
| POST | `/tasks` | Create a task |
| PATCH | `/tasks/<id>` | Update task completion |
| DELETE | `/tasks/<id>` | Delete a task |

## What I Learned

- Containerizing a Python web application
- Configuring services with Docker Compose
- Connecting Flask to PostgreSQL
- Configuring Nginx as a reverse proxy
- Managing container networking and persistent volumes
- Debugging container startup and service connectivity

## Future Improvements

- Environment-based secrets management
- Automated tests
- CI/CD with GitHub Actions
- Improved validation and error handling
- Deployment to a cloud server

---

**Author:** Faisal Rahman

