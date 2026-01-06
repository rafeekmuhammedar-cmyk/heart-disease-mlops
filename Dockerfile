# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt requirements.txt
COPY logistic_regression_pipeline.pkl logistic_regression_pipeline.pkl
COPY app.py app.py

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
