from concurrent import futures

import grpc
import hello_pb2, hello_pb2_grpc
import logging

class ProductServicer(hello_pb2_grpc.ProductService):
    def NewProduct(self, request, context):
        logging.info(f'NewProduct request received: {request.name}|{request.price}')
        return hello_pb2.NewProductResponse(success=True)

def serve():
    logging.info('Starting server...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_ProductServiceServicer_to_server(ProductServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
    

if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    serve()