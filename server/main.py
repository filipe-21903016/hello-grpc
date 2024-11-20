from concurrent import futures
import grpc
import hello_pb2
import hello_pb2_grpc
import logging

# Set up logger
logger = logging.getLogger("ProductServiceServer")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()

# Custom formatter for clearer and consistent logs
formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

class ProductServicer(hello_pb2_grpc.ProductServiceServicer):
    def NewProduct(self, request, context):
        # Log the request details
        logger.info("NewProduct request received: name=%s, price=%d", request.name, request.price)
        
        # Simulating a response
        response = hello_pb2.NewProductResponse(success=True)
        logger.info("Responding with: success=%s", response.success)
        return response

def serve():
    logger.info("Starting server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_ProductServiceServicer_to_server(ProductServicer(), server)
    
    server_address = "[::]:50051"
    server.add_insecure_port(server_address)
    logger.info("Server listening on %s", server_address)
    
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        logger.info("Shutting down server due to keyboard interrupt")

if __name__ == '__main__':
    serve()
