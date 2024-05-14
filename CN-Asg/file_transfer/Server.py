import socket
import math

PORT = 12345

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('localhost', PORT))
            server_socket.listen(5)
            print("Server is listening...")

            while True:
                client_socket, address = server_socket.accept()
                print("Connected to client:", address)

                handle_client(client_socket)

                client_socket.close()
                print("Client disconnected.")

    except Exception as e:
        print("Error:", e)

def handle_client(client_socket):
    try:
        with client_socket:
            in_stream = client_socket.makefile('r')
            out_stream = client_socket.makefile('w')

            while True:
                option = in_stream.readline().strip()

                if not option:
                    break

                if option == "1":
                    print("Client selected: Say Hello")
                    say_hello(out_stream, in_stream)
                elif option == "2":
                    print("Client selected: File Transfer")
                    file_transfer(in_stream, out_stream)
                elif option == "3":
                    print("Client selected: Arithmetic Calculator")
                    arithmetic_calculator(in_stream, out_stream)
                elif option == "4":
                    print("Client selected: Trigonometric Calculator")
                    trigonometric_calculator(in_stream, out_stream)
                else:
                    print("Client selected: Invalid option")
                    out_stream.write("Invalid option.\n")
                    out_stream.flush()

    except Exception as e:
        print("Error:", e)

def say_hello(out_stream, in_stream):
    out_stream.write("Hello from server!\n")
    out_stream.flush()
    print("Server responded: Hello sent")

    print("Waiting for client's acknowledgment...")
    acknowledgment = in_stream.readline().strip()
    print("Client's acknowledgment:", acknowledgment)

def file_transfer(in_stream, out_stream):
    try:
        file_name = in_stream.readline().strip()
        with open(file_name, 'rb') as file:
            for line in file:
                out_stream.write(line.decode())
                out_stream.flush()
        print("File sent successfully.")
        out_stream.write("EOF\n")
        out_stream.flush()

    except FileNotFoundError:
        print("File not found.")
        out_stream.write("File not found.\n")
        out_stream.flush()

    except Exception as e:
        print("Error:", e)

def arithmetic_calculator(in_stream, out_stream):
    try:
        expression = in_stream.readline().strip()
        result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt})
        out_stream.write(str(result) + '\n')
        out_stream.flush()
        print("Result sent:", result)

    except Exception as e:
        out_stream.write("Error evaluating expression: " + str(e) + '\n')
        out_stream.flush()
        print("Error occurred:", e)

def trigonometric_calculator(in_stream, out_stream):
    try:
        expression = in_stream.readline().strip()
        result = eval(expression, {"__builtins__": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan})
        out_stream.write(str(result) + '\n')
        out_stream.flush()
        print("Result sent:", result)

    except Exception as e:
        out_stream.write("Error evaluating expression: " + str(e) + '\n')
        out_stream.flush()
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
