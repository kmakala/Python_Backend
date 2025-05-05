# Use official Python base image
FROM python:alpine

# Set working directory
WORKDIR /app

# Copy only requirements first (none in our case, but keeping pattern)
COPY requirements.txt .

# Install dependencies (just Flask)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY main.py .

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "main.py"]
