"""
DevOps Info Service (Python) ── (｡•̀ᴗ-)✧
Two endpoints:
- GET /       -> full service + system + runtime + request info
- GET /health -> simple health check (monitoring-friendly) (•‿•)
"""

from __future__ import annotations

import logging
import os
import platform
import socket
from datetime import datetime, timezone
from typing import Any, Dict, Tuple

from flask import Flask, jsonify, request

# --- Logging: your app's tiny diary (ง'̀-'́)ง ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("devops-info-service")

# --- App instance (hello, Flask!) (＾▽＾)/ ---
app = Flask(__name__)

# --- Config via env vars (DevOps superpower) (｡•̀ᴗ-)✧ ---
HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", "5000"))
DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

# --- Start time for uptime (⏱️) ---
START_TIME = datetime.now(timezone.utc)


def iso_utc_now() -> str:
    """Current UTC time in ISO format (milliseconds) + Z (UTC) (•‿•)"""
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def get_uptime() -> Tuple[int, str]:
    """Return uptime in seconds + human string (machine + human friendly) (・ω・)b"""
    delta = datetime.now(timezone.utc) - START_TIME
    seconds = int(delta.total_seconds())
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return seconds, f"{hours} hour(s), {minutes} minute(s)"


def get_system_info() -> Dict[str, Any]:
    """Collect system info from the machine running this service (＾▽＾)"""
    return {
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "platform_version": platform.platform(),
        "architecture": platform.machine(),
        "cpu_count": os.cpu_count(),
        "python_version": platform.python_version(),
    }


def get_request_info() -> Dict[str, Any]:
    """Collect request info (who asked & how) (｡•̀ᴗ-)✧"""
    return {
        "client_ip": request.remote_addr,
        "user_agent": request.headers.get("User-Agent"),
        "method": request.method,
        "path": request.path,
    }


def list_endpoints() -> list[dict]:
    """Self-documentation so the API can introduce itself (•‿•)"""
    return [
        {"path": "/", "method": "GET", "description": "Service information"},
        {"path": "/health", "method": "GET", "description": "Health check"},
    ]


@app.get("/")
def main():
    logger.info("Request: %s %s from %s", request.method, request.path, request.remote_addr)

    uptime_seconds, uptime_human = get_uptime()
    data = {
        "service": {
            "name": "devops-info-service",
            "version": "1.0.0",
            "description": "DevOps course info service",
            "framework": "Flask",
        },
        "system": get_system_info(),
        "runtime": {
            "uptime_seconds": uptime_seconds,
            "uptime_human": uptime_human,
            "current_time": iso_utc_now(),
            "timezone": "UTC",
        },
        "request": get_request_info(),
        "endpoints": list_endpoints(),
    }
    return jsonify(data), 200


@app.get("/health")
def health():
    logger.info("Request: %s %s from %s", request.method, request.path, request.remote_addr)

    uptime_seconds, _ = get_uptime()
    data = {
        "status": "healthy",
        "timestamp": iso_utc_now(),
        "uptime_seconds": uptime_seconds,
    }
    return jsonify(data), 200


# --- Error handling: return JSON, not HTML pages (｡•́︿•̀｡) ---
@app.errorhandler(404)
def not_found(_error):
    return jsonify({"error": "Not Found", "message": "Endpoint does not exist"}), 404


@app.errorhandler(500)
def internal_error(error):
    logger.exception("Internal error: %s", error)
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred"}), 500


if __name__ == "__main__":
    logger.info("Starting application on %s:%s (DEBUG=%s) (づ｡◕‿‿◕｡)づ", HOST, PORT, DEBUG)
    app.run(host=HOST, port=PORT, debug=DEBUG)
