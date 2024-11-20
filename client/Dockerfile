FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker's caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy code files
COPY . .

# Generate gRPC Python files
RUN python -m grpc_tools.protoc -I./protos --python_out=./src/ --grpc_python_out=./src protos/hello.proto