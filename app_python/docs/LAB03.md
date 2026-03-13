# LAB03 — Continuous Integration (｡•̀ᴗ-)✧

## What I chose

### Testing framework
I chose **pytest** because it is simple, readable, and very comfy to use. It lets me write tests without too much boilerplate, which is especially nice for a small Flask project (•‿•)

### Linter
I chose **ruff** because it is fast, lightweight, and easy to plug into CI. Tiny tool, big help (ง'̀-'́)ง

### Versioning strategy
I chose **CalVer** with the format `YYYY.MM.DD` together with the `latest` tag.

This felt like the most practical option for a small service. It makes image versions easy to read, easy to sort, and easy to connect to the build date without extra confusion (・ω・)b

## What is tested

The tests check the main important things:

- `GET /` returns `200`
- `GET /health` returns `200`
- `/health` returns JSON with `"status": "healthy"`
- unknown endpoint returns `404`
- wrong HTTP method for `/health` returns `405`

So basically: the app responds when it should, and complains properly when it should too (¬‿¬)

## How to run locally

From the `app_python/` directory:

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pytest -v
ruff check .