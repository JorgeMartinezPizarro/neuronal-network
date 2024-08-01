# Use the official Tensorflow image as base image
FROM tensorflow/tensorflow:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt app.py data.json /app

# Install any dependencies specified in requirements.txt
# If you have any additional dependencies, add them to requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir output

# Command to run the Python script
CMD ["python", "app.py"]
