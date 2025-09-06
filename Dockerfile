# Use official Python base image (Alpine is a lightweight Linux distribution,
# so this keeps the image small and efficient while still including Python)
FROM python:alpine

# Set the working directory inside the container to /app
# All subsequent commands (COPY, RUN, CMD, etc.) will run relative to this folder.
WORKDIR /app

# Copy requirements.txt into the container at /app
# This is done separately from the code so Docker can cache dependency installs
# and only redo them if requirements.txt changes.
COPY requirements.txt .

# Install dependencies specified in requirements.txt
# --no-cache-dir avoids caching files to reduce final image size.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code (e.g., main.py) into /app
# This happens after installing dependencies, so code changes don’t force
# reinstalling packages unnecessarily.
COPY main.py .

# Expose port 5000 to the host (Flask defaults to running on port 5000).
# This doesn’t actually publish the port by itself — it just serves as metadata.
EXPOSE 5000

# Define the command to run when the container starts.
# Here it runs "python main.py" to start your Flask app.
CMD ["python", "main.py"]
