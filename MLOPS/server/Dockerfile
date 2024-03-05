 # server/Dockerfile

FROM python:3.9-slim

# Set the working directory to /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

COPY app.py app.py
COPY model.pkl model.pkl
# Command to run the Uvicorn server

CMD ["uvicorn", "--reload", "--host", "0.0.0.0", "app:app"]





