# Wombat Stub Python App

This is a simple Python application that logs "wombat active" every 15 seconds. It is designed to run in a Docker container using a virtualenv environment.

## Files
- wombat_app.py: Main application
- Dockerfile: Container build instructions

## Build and Run

1. Build the Docker image:

   docker build -t wombat-stub .

2. Run the container:

   docker run --rm wombat-stub

The app will log a message every 15 seconds.
