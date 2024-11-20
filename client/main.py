import random
import grpc
import hello_pb2_grpc 
import hello_pb2

def main():
    random_name = f'hello{random.randint(0, 1000)}'
    random_price = random.randint(0, 1000)

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.ProductServiceStub(channel)
        response = stub.NewProduct(hello_pb2.NewProductRequest(name=random_name, price=random_price))
        print("NewProduct response received:", response)


if __name__ == '__main__':
    main()