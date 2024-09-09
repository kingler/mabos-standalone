#!/bin/bash

# Clone the WebVOWL repository if it doesn't exist
if [ ! -d "WebVOWL" ]; then
  git clone https://github.com/VisualDataWeb/WebVOWL.git
fi

cd WebVOWL

# Build the Docker image
docker build . -t webvowl:v1

# Run the Docker container
docker-compose up -d

echo "WebVOWL is running at http://localhost:8080"
