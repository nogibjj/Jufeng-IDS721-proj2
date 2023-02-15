# FROM alpine:latest
# RUN apk update && apk add bash

# WORKDIR /app
# COPY repeat.sh /app

# # Use an official Python runtime as a parent image
# FROM python:3.9

# # Set the working directory to /app
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed packages specified in requirements.txt
# # RUN pip install --no-cache-dir -r requirements.txt

# # Run the script.py when the container launches
# CMD ["python", "mylib/list_files.py"]


FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "mylib/list_files.py", "/app"]

