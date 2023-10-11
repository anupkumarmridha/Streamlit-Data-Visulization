# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Create a working directory
WORKDIR /streamlit-data-visualization

# Copy the current directory contents into the container at /streamlit-data-visualization
COPY . /streamlit-data-visualization/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define the command to run your Streamlit app
CMD ["streamlit", "run", "my_app.py"]
