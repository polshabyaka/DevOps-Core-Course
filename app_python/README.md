# DevOps Info Service (Python) (｡•̀ᴗ-)✧

## Overview
DevOps Info Service is a small Python web application that reports information about itself and the system it runs on. Tiny app, serious vibes, useful JSON (ง'̀-'́)ง

It exposes two endpoints:
- `GET /` — detailed service and system info
- `GET /health` — lightweight health check for monitoring and quick status checks (•‿•)

## Prerequisites
Before waking up the app, make sure you have:

- Python 3.11+
- `pip`
- optional virtual environment, because clean environments are happy environments (づ｡◕‿‿◕｡)づ

## Installation

### Create and activate virtual environment

**Windows (Git Bash):**
```bash
python -m venv venv
source venv/Scripts/activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies

From the `app_python/` directory:

```bash
python -m pip install -r requirements.txt
```

## Running the Application

### Default run
From the `app_python/` directory:

```bash
python app.py
```

Default address:
```text
http://127.0.0.1:5000
```

### Run with custom configuration
You can change the port through an environment variable, very DevOps, very fancy (｡•̀ᴗ-)✧

```bash
PORT=8080 python app.py
```

## API Endpoints

### `GET /`
Returns detailed information about:
- the service itself
- the system it runs on
- runtime information
- request metadata

Example:
```bash
curl http://127.0.0.1:5000/
```

### `GET /health`
Returns a simple health response suitable for monitoring and automated checks.

Example:
```bash
curl http://127.0.0.1:5000/health
```

## Configuration

| Variable | Default   | Example     | Description             |
|----------|-----------|-------------|-------------------------|
| `HOST`   | `0.0.0.0` | `127.0.0.1` | Bind address            |
| `PORT`   | `5000`    | `8080`      | Port number             |
| `DEBUG`  | `False`   | `True`      | Enable Flask debug mode |

## Framework Selection

**Chosen framework:** Flask

**Why Flask:** Flask is lightweight, beginner-friendly, and requires very little boilerplate. For a small JSON API with only two endpoints, it is a perfect fit and does not add unnecessary complexity (・ω・)b

## Best Practices Applied

### Clean code organization
- imports are grouped properly
- helper functions are extracted into separate reusable units
- endpoint logic is kept readable and compact

### Error handling
- `404` returns JSON instead of HTML
- `500` returns JSON instead of HTML

### Logging
- startup logging is enabled
- request logging is enabled
- this helps with debugging, monitoring, and knowing what the app is doing instead of guessing into the void (⊙_⊙)

## Docker

### Build image locally
```bash
docker build -t <image-name> .
```

### Run container
```bash
docker run --name <container-name> -p <host-port>:<container-port> <image-name>
```

### Pull from Docker Hub
```bash
docker pull <dockerhub-username>/<repository-name>:<tag>
```

### Run pulled image
```bash
docker run --rm -p <host-port>:<container-port> <dockerhub-username>/<repository-name>:<tag>
```