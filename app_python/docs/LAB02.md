# Lab 2 — Docker Containerization (｡•̀ᴗ-)✧

## 1. Docker Best Practices Applied

### Specific base image version
I used `python:3.13-slim` instead of `latest`.

Why it matters:
- improves reproducibility
- avoids unexpected image changes between builds
- `slim` is smaller than the full Python image, so the container stays a bit less chonky (•‿•)

Dockerfile snippet:
```dockerfile
FROM python:3.13-slim
```

### Non-root user
The container runs as a dedicated non-root user.

Why it matters:
- improves security
- reduces the impact of a possible compromise
- follows Docker best practices instead of letting the container run around with root privileges like a tiny goblin

Dockerfile snippet:
```dockerfile
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser
```

### Layer caching
I copied `requirements.txt` before copying the application code.

Why it matters:
- Docker can reuse the dependency installation layer
- source code changes do not force reinstall of dependencies every time
- rebuilds become faster, which saves both time and sanity (╯°□°）╯

Dockerfile snippet:
```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appgroup app.py .
```

### Only necessary files copied
I copied only the runtime files instead of the whole repository.

Why it matters:
- smaller image
- cleaner runtime environment
- reduced attack surface
- less random stuff inside the image, which is always nice

### `.dockerignore`
I added a `.dockerignore` file to exclude caches, IDE files, tests, and documentation from the build context.

Why it matters:
- smaller build context
- faster image build
- unnecessary local files are not sent to Docker

---

## 2. Image Information & Decisions

### Base image chosen
`python:3.13-slim`

### Justification
I chose this image because it provides a modern Python runtime while keeping the image smaller than the full Python base image. It is a good balance between functionality and image size.

### Final image size
Real output of:

```bash
docker images
```

```text
                                                                i Info →   U  In Use
IMAGE                               ID             DISK USAGE   CONTENT SIZE   EXTRA
devops-info-service:latest          e64ecc981395        182MB         44.4MB    U
hello-world:latest                  ef54e839ef54       25.9kB         9.52kB    U
janjakrussoyuhuuu/devops-info-service:latest
                                    f468a0957ef5        182MB         44.4MB    U
janjakrussoyuhuuu/devops-info-service:v1
                                    f468a0957ef5        182MB         44.4MB    U
```

Assessment:
The final image size is reasonable for a small Python application using the `python:3.13-slim` base image. The image includes the Python runtime, Flask dependency, and the application itself, while avoiding unnecessary files in the build context.

### Layer structure explanation
The image is built in this order:
1. base image
2. environment variables
3. working directory
4. non-root user creation
5. dependency installation
6. application file copy
7. switch to non-root user
8. startup command

This order is important because it improves build caching and keeps the image structure logical.

### Optimization choices
- used `python:3.13-slim`
- used `PIP_NO_CACHE_DIR=1`
- installed dependencies before source code
- copied only the required runtime file
- added `.dockerignore`

---

## 3. Build & Run Process

### Build output
Real output from:

```bash
docker build -t devops-info-service .
```

```text
[+] Building 2.5s (12/12) FINISHED                             docker:desktop-linux
 => [internal] load build definition from Dockerfile                           0.1s
 => => transferring dockerfile: 404B                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.13-slim            1.7s
 => [auth] library/python:pull token for registry-1.docker.io                  0.0s
 => [internal] load .dockerignore                                              0.0s
 => => transferring context: 144B                                              0.0s
 => [internal] load build context                                              0.0s
 => => transferring context: 63B                                               0.0s
 => [1/6] FROM docker.io/library/python:3.13-slim@sha256:f50f56f1471fc430b394  0.1s
 => => resolve docker.io/library/python:3.13-slim@sha256:f50f56f1471fc430b394  0.1s
 => CACHED [2/6] WORKDIR /app                                                  0.0s
 => CACHED [3/6] RUN addgroup --system appgroup && adduser --system --ingroup  0.0s
 => CACHED [4/6] COPY requirements.txt .                                       0.0s
 => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt            0.0s
 => CACHED [6/6] COPY --chown=appuser:appgroup app.py .                        0.0s
 => exporting to image                                                         0.3s
 => => exporting layers                                                        0.0s
 => => exporting manifest sha256:41e7d5ab030da0d3ceb8f70c2660f4e5ecce53266be3  0.0s
 => => exporting config sha256:5bec1b64a0d9ef08e4b0983462e645bc3c85b2daaec3fa  0.0s
 => => exporting attestation manifest sha256:cb84170960d55f611b37aa8e3de4f2d5  0.1s
 => => exporting manifest list sha256:e64ecc981395900e3067f79bdfd6823c886b127  0.0s
 => => naming to docker.io/library/devops-info-service:latest                  0.0s
 => => unpacking to docker.io/library/devops-info-service:latest               0.0s
```

### Container running output
```text
2026-02-26 18:26:38,884 - devops-info-service - INFO - Starting application on 0.0.0.0:5000 (DEBUG=False) (づ｡◕‿‿◕｡)づ
 * Serving Flask app 'app'
 * Debug mode: off
2026-02-26 18:26:38,900 - werkzeug - INFO - WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
2026-02-26 18:26:38,900 - werkzeug - INFO - Press CTRL+C to quit
```

### Endpoint testing output

`GET /`
```json
{"endpoints":[{"description":"Service information","method":"GET","path":"/"},{"description":"Health check","method":"GET","path":"/health"}],"request":{"client_ip":"172.17.0.1","method":"GET","path":"/","user_agent":"curl/8.12.1"},"runtime":{"current_time":"2026-02-26T18:26:54.887Z","timezone":"UTC","uptime_human":"0 hour(s), 0 minute(s)","uptime_seconds":15},"service":{"description":"DevOps course info service","framework":"Flask","name":"devops-info-service","version":"1.0.0"},"system":{"architecture":"x86_64","cpu_count":12,"hostname":"072b45950b80","platform":"Linux","platform_version":"Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.41","python_version":"3.13.12"}}
```

`GET /health`
```json
{"status":"healthy","timestamp":"2026-02-26T18:26:55.149Z","uptime_seconds":16}
```

### Docker Hub repository URL
`https://hub.docker.com/r/janjakrussoyuhuuu/devops-info-service`

### Push output
```text
The push refers to repository [docker.io/janjakrussoyuhuuu/devops-info-service]
bfd789ec25e4: Pushed
c81b7652c2ff: Pushed
d9d0732b36a8: Pushed
b660c8ea3431: Pushed
ecaaafaadcbd: Pushed
f6b1b5bbc232: Pushed
9c141cfd024a: Pushed
117be4eb1e51: Pushed
206356c42440: Pushed
5b39b1ec4b91: Pushed
latest: digest: sha256:f468a0957ef5bddefffb4c6a3415f0ebb214d8dc4f7e72d7e7f13abff4c8643e size: 856
```

### Pull verification
```text
latest: Pulling from janjakrussoyuhuuu/devops-info-service
Digest: sha256:f468a0957ef5bddefffb4c6a3415f0ebb214d8dc4f7e72d7e7f13abff4c8643e
Status: Image is up to date for janjakrussoyuhuuu/devops-info-service:latest
docker.io/janjakrussoyuhuuu/devops-info-service:latest
```

### Tagging strategy
I used:
- `latest` for the most recent version of the image
- `v1` as a fixed version tag for reproducibility

This strategy makes it easy to pull the newest image and also reference a stable version explicitly.

---

## 4. Technical Analysis

### Why this Dockerfile works the way it does
The Dockerfile installs dependencies before copying the application code, which improves Docker layer caching. It sets `/app` as the working directory, copies only the required files, creates a non-root user, exposes port `5000`, and starts the Flask app with `python app.py`.

### What would happen if the layer order changed
If the application code were copied before `requirements.txt`, Docker would often rebuild the dependency layer after every source code change. That would make rebuilds slower because packages would be reinstalled more often.

### Security considerations
- the application runs as a non-root user
- the `slim` base image reduces unnecessary packages
- only required runtime files are copied into the image

### How `.dockerignore` improves the build
`.dockerignore` excludes files such as caches, virtual environments, IDE settings, tests, and documentation. This reduces the build context size and speeds up the Docker build process. Tiny file, big helper (｡•̀ᴗ-)✧

---

## 5. Challenges & Solutions

### Challenge 1
Docker worked in PowerShell, but Git Bash initially could not find the `docker` command.

### Solution
I restarted Git Bash, after which the Docker CLI became available there as well.

### Challenge 2
At first I tried to access the application while the container was not actively running.

### Solution
I checked container status using `docker ps -a`, inspected logs using `docker logs`, and then ran the container correctly in detached mode.

### Challenge 3
I initially used the wrong activation path for the virtual environment in Git Bash on Windows.

### Solution
I used the correct Windows Git Bash activation command:

```bash
source venv/Scripts/activate
```

### What I learned
I learned how to create a Dockerfile for a Python web application, why non-root users matter, how Docker layer caching works, how `.dockerignore` improves builds, how virtual environments differ between Linux and Windows Git Bash, and how to publish an image to Docker Hub. Overall: many tiny DevOps creatures were successfully tamed (ง'̀-'́)ง