#!/bin/bash

# Exit on any error
set -e

# Navigate to the project root
cd "$(dirname "$0")/.."

# Build the frontend
echo "Building frontend..."
cd frontend
npm run build
cd ..

# Start the backend server in the background
echo "Starting backend server..."
uvicorn src.api.main:app --reload --ssl-keyfile=localhost.key --ssl-certfile=localhost.crt &
BACKEND_PID=$!

# Wait for the backend to start
echo "Waiting for backend to start..."
sleep 10

# Start the frontend server in the background
echo "Starting frontend server..."
cd frontend
npx serve -s build -l 3000 &
FRONTEND_PID=$!

# Wait for the frontend to start
echo "Waiting for frontend to start..."
sleep 5

# Run the performance tests
echo "Running performance tests..."
node scripts/performance-test.js

# Stop the servers
echo "Stopping servers..."
kill $BACKEND_PID
kill $FRONTEND_PID

echo "Performance tests completed."