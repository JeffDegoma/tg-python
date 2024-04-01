FROM python:3.12-alpine

WORKDIR /home

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# ENTRYPOINT ["tail", "-f", "/dev/null"]

ENV FLASK_ENV="docker"
EXPOSE 5000

# CMD ["python", "./app.py"]
# CMD tail -f /dev/null

# CMD ["flask", "run", "--host", "0.0.0.0"]
CMD ["tail", "-f", "/dev/null"]

