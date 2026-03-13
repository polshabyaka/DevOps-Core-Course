````md
# LAB01 — Python Web Application

## 1) Framework choice
I chose **Flask** because it is pretty cool and since I am a beginner it was easy to learnd. It requires minimal boilerplate code, which is convenient for a small service with a few endpoints. Flask is enough for returning JSON responses and reading request information so why not.

## 2) How to run the service

### Create and activate venv (Windows Git Bash)
```bash
python -m venv venv
source venv/Scripts/activate
````

### Install dependencies

```bash
cd app_python
python -m pip install -r requirements.txt
```

### Run (default)

```bash
python app.py
```

### Run with custom host/port (optional)

```bash
HOST=127.0.0.1 PORT=8080 python app.py
```

## 3) How to test endpoints

### Health check

```bash
curl http://127.0.0.1:5000/health
```

### Main endpoint

```bash
curl http://127.0.0.1:5000/
```

### Formatted JSON output

```bash
curl -s http://127.0.0.1:5000/ | python -m json.tool
```

## 4) Screenshots (proof of work)

Screenshots are saved in `app_python/docs/screenshots/`:

* `01-main-endpoint.png`
* `02-health-check.png`
* `03-formatted-output.png`

```
::contentReference[oaicite:0]{index=0}
```
