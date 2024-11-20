# Hello gRPC

## Build images

Build the server image:
```bash
docker build -t hello-grpc-server server/
```

Build the client image:
```bash
docker build -t hello-grpc-client client/
```

# Run the server

Create a network:
```bash
docker network create hello-grpc-network
```

Run the server container:
```bash
docker run -d --name grpc-server --network hello-grpc-network -p 50051:50051 hello-grpc-server
```

# Send requests to the server

```bash
docker run --rm --network hello-grpc-network -e GRPC_ADDR=grpc-server:50051 hello-grpc-client python src/main.py
```
