FROM python:3.11-slim-buster

# Copy the Python script to the container
COPY app.py /app/

# Set the working directory
WORKDIR /app

# Install required dependencies
RUN pip install flask

# Expose the port
EXPOSE 5000

# Define the entrypoint
CMD ["python", "app.py"]