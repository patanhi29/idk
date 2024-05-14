import socket

def main():
    try:
        a = [30, 40, 50, 60, 70, 80, 90, 100, 110]
        serversocket = socket.socket()
        serversocket.bind(('localhost', 8011))
        serversocket.listen(1)
        print("Waiting for connection")
        client, address = serversocket.accept()
        with client:
            out = client.makefile('wb')
            in_stream = client.makefile('rb')

            print("The number of packets sent is:", len(a))
            # Send the number of frames as a byte
            out.write(len(a).to_bytes(1, byteorder='big'))
            out.flush()

            for i in range(len(a)):
                # Send each frame as a byte
                out.write(a[i].to_bytes(1, byteorder='big'))
                out.flush()

            # Receive the request for retransmitted packet number
            k = int.from_bytes(in_stream.read(1), byteorder='big')

            # Send the retransmitted packet
            out.write(a[k].to_bytes(1, byteorder='big'))
            out.flush()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
