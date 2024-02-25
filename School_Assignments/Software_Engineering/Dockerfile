# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR .

# Install the Flask library
RUN pip install Flask

# Copy the current directory contents into the container at /app
COPY app.py ./

# Run app.py when the container launches
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
