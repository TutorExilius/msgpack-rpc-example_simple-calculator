from simple_msgpack_rpc_calculator.calculator import *
import msgpackrpc


def main():
    print("Initialise Server...", flush=True)
    server = msgpackrpc.Server(Calculator())

    print("Start Server...", flush=True)
    port = 18800
    host = "localhost"
    server.listen(msgpackrpc.Address("localhost", 18800))

    print(f"Server is running on: {host}:{port}", flush=True)
    server.start()


if __name__ == '__main__':
    main()
