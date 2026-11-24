FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN groupadd --system app \
    && useradd --system --gid app --home-dir /nonexistent --no-create-home app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app app.py pytania.json wyzwania.json tajne_zadania.json ./
COPY --chown=app:app templates/ ./templates/
COPY --chown=app:app static/ ./static/

USER app

EXPOSE 13001

CMD ["python", "app.py"]
