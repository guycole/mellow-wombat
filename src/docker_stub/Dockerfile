# Dockerfile for wombat_app
FROM python:3.11-slim

WORKDIR /app

# Copy requirements if you have any, else skip
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# Create and activate virtualenv
RUN python -m venv /app/venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY wombat_app.py ./

CMD ["python", "wombat_app.py"]
