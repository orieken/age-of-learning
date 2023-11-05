# Stage 1: Selenium and Chrome setup
FROM selenium/standalone-chrome:latest AS selenium

# Stage 2: Python application
FROM python:3.9-slim

# Install additional packages (if needed)
RUN apt-get update  # \
    # && apt-get install -y

# Copy Selenium and Chrome setup from the first stage
COPY --from=selenium /usr/bin/chromedriver /usr/bin/chromedriver
COPY --from=selenium /opt/bin/entry_point.sh /opt/bin/entry_point.sh

# Install Chrome browser (if needed)
# RUN apt-get install -y google-chrome-stable

# Set display environment variable for headless Chrome
ENV DISPLAY=:99

# Install Python dependencies
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy your test files into the container
COPY tests/ /app/tests/

# Run your tests
CMD ["pytest", "tests/"]
