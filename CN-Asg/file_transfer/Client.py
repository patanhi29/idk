import socket
import os

SERVER_ADDRESS = "127.0.0.1"
PORT = 12345

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_ADDRESS, PORT))

            user_input = input
            in_stream = client_socket.makefile('r')
            out_stream = client_socket.makefile('w')

            print("Connected to server.")

            while True:
                display_menu()
                option = user_input("Choose an option: ")
                out_stream.write(option + '\n')
                out_stream.flush()

                if option == "1":
                    print("Server says:", in_stream.readline().strip())
                    out_stream.write("Acknowledged\n")
                    out_stream.flush()
                elif option == "2":
                    file_name = user_input("Enter file name to transfer: ")
                    out_stream.write(file_name + '\n')
                    out_stream.flush()
                    receive_file(in_stream)
                    print("File received successfully.")
                    print_received_file_contents()
                elif option in {"3", "4"}:
                    expression = user_input("Enter expression: ")
                    out_stream.write(expression + '\n')
                    out_stream.flush()
                    result = in_stream.readline().strip()
                    if not result.startswith("Error"):
                        print("Result:", result)
                    else:
                        print("Error occurred:", result)
                else:
                    print("Invalid option.")

    except Exception as e:
        print("Error:", e)

def display_menu():
    print("Options:")
    print("1. Say Hello")
    print("2. File Transfer")
    print("3. Arithmetic Calculator")
    print("4. Trigonometric Calculator")

def receive_file(in_stream):
    try:
        with open("received_file.txt", "w") as file_writer:
            while True:
                line = in_stream.readline().strip()
                if line == "EOF":
                    break
                file_writer.write(line + "\n")

    except Exception as e:
        print("Error:", e)

def print_received_file_contents():
    try:
        with open("received_file.txt", "r") as file_reader:
            print("Contents of received file:")
            for line in file_reader:
                print(line.strip())

    except Exception as e:
        print("Error while reading file:", e)

if __name__ == "__main__":
    main()
