from python:3.7.4-slim

WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8090
CMD ["python", "src/server.py"]