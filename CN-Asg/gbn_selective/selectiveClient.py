import socket

def main():
    try:
        v = [0] * 9
        n = 0
        addr = socket.gethostbyname("localhost")
        print(addr)
        connection = socket.socket()
        connection.connect((addr, 8011))

        with connection:
            out = connection.makefile('wb')
            in_stream = connection.makefile('rb')
            
            # Read the number of frames as a byte
            p = int.from_bytes(in_stream.read(1), byteorder='big')
            print("No of frame is:", p)

            for i in range(p):
                # Read each frame as a byte
                v[i] = int.from_bytes(in_stream.read(1), byteorder='big')
                print("Received frame is:", v[i])

            v[5] = -1
            
            for i in range(p):
                if v[i] == -1:
                    print("Request to retransmit packet no", i+1, "again!!")
                    n = i
                    # Send the requested packet number to the server
                    out.write(n.to_bytes(1, byteorder='big'))
                    out.flush()

            print()
            
            # Read the retransmitted packet
            v[n] = int.from_bytes(in_stream.read(1), byteorder='big')
            print("Received frame is:", v[n])

            print("Quitting")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
