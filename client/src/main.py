import os
import random
import grpc
import hello_pb2_grpc 
import hello_pb2
import logging

GRPC_ADDR = os.getenv("GRPC_ADDR")

# Set up the logger
logger = logging.getLogger("ProductServiceLogger")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()

# Custom formatter for prettier logs
formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def main():
    if not GRPC_ADDR:
        logger.error("GRPC_ADDR environment variable not set")
        return

    random_name = f'hello{random.randint(0, 1000)}'
    random_price = random.randint(0, 1000)

    logger.info("Generated random product details: name=%s, price=%d", random_name, random_price)

    with grpc.insecure_channel(GRPC_ADDR) as channel:
        logger.info(f"Connecting to gRPC server on {GRPC_ADDR}")
        stub = hello_pb2_grpc.ProductServiceStub(channel)
        
        try:
            response = stub.NewProduct(hello_pb2.NewProductRequest(name=random_name, price=random_price))
            logger.info("NewProduct response received: %s", response)
        except grpc.RpcError as e:
            logger.error("gRPC call failed with error: %s", e)

if __name__ == '__main__':
    main()
