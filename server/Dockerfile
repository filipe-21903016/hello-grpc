FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Generate gRPC Python files
RUN python -m grpc_tools.protoc -I./protos --python_out=./src/ --grpc_python_out=./src protos/hello.proto

# Expose the gRPC server port
EXPOSE 50051

# Set the default command to start the application
CMD ["python", "src/main.py"]
