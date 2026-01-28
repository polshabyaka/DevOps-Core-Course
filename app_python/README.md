````md
# DevOps Info Service (Python) (｡•̀ᴗ-)✧

## Overview
DevOps Info Service is a small Python web application that reports information about itself and the system it runs on (hostname, OS/platform, CPU count, Python version, uptime, and request metadata) (•‿•).  
It exposes two endpoints: `GET /` for detailed service/system info and `GET /health` for a lightweight health check used by monitoring tools (ง'̀-'́)ง.

## Prerequisites
- Python 3.11+ (Python 3.12 works great too) (＾▽＾)/
- `pip` (usually comes with Python)
- (Recommended) Virtual environment (`venv`) so dependencies stay tidy (｡•̀ᴗ-)✧

## Installation

### Create and activate virtual environment (venv) (づ｡◕‿‿◕｡)づ
**Windows (Git Bash):**
```bash
python -m venv venv
source venv/Scripts/activate
````

**Linux/Mac:**

```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies (let’s feed the app its snacks )

From the `app_python/` directory:

```bash
python -m pip install -r requirements.txt
```

## Running the Application

### Default run (simple & comfy) (・ω・)b

From the `app_python/` directory:

```bash
python app.py
```

Default address: `http://127.0.0.1:5000`

### Run with custom configuration (DevOps-style)

```bash
PORT=8080 python app.py
```

## API Endpoints

* `GET /` — Service and system information
  Example:

  ```bash
  curl http://127.0.0.1:5000/
  ```

* `GET /health` — Health check
  Example:

  ```bash
  curl http://127.0.0.1:5000/health
  ```

## Configuration (Environment Variables) (≧▽≦)

| Variable |   Default |     Example | Description                 |
| -------- | --------: | ----------: | --------------------------- |
| `HOST`   | `0.0.0.0` | `127.0.0.1` | Bind address to listen on   |
| `PORT`   |    `5000` |      `8080` | Port number for the service |
| `DEBUG`  |   `False` |      `True` | Enable Flask debug mode     |

```
::contentReference[oaicite:0]{index=0}

## Framework selection

**Chosen framework:** Flask.

**Why Flask:** Flask is lightweight and beginner-friendly. It requires minimal boilerplate and is enough for a small JSON API with a couple of endpoints.

### Comparison table

| Framework | Pros | Cons | Why not chosen |
|---|---|---|---|
| Flask | Simple, minimal code, easy to learn | Fewer built-in features | N/A (chosen) |
| FastAPI | Modern, async, auto docs | More concepts (async, pydantic) | Not needed for 2 endpoints |
| Django | Full-featured, ORM, admin | Heavy for this lab | Overkill for simple service |

## Best practices apply

### Clean code organization
- Imports grouped (standard library first, then third-party).
- Helper functions extracted: `get_system_info()`, `get_uptime()`, `get_request_info()`.

### Error handling
- Implemented JSON error handlers:
  - 404 Not Found returns JSON message.
  - 500 Internal Server Error returns JSON message.

### Logging
- Configured logging using Python `logging`.
- Logs application startup and each request (method/path/client IP).

## API documentation

### GET /
Test:
```bash
curl http://127.0.0.1:5000/

```
