import socket
import pickle
import time

WINDOW_SIZE = 4
TIMEOUT = 5

class Packet:
    def __init__(self, seq_num, data):
        self.seq_num = seq_num
        self.data = data

def receive_packets(server_socket, total_packets):
    expected_seq_num = 0

    while expected_seq_num < total_packets:
        data, client_addr = server_socket.recvfrom(1024)
        received_packet = pickle.loads(data)
        print(f"Received packet with seq num {received_packet.seq_num}")

        if received_packet.seq_num == expected_seq_num:
            # Simulating acknowledgment packet
            ack_packet = Packet(expected_seq_num, "")
            server_socket.sendto(pickle.dumps(ack_packet), client_addr)
            expected_seq_num += 1
        else:
            print(f"Received out-of-order packet with seq num {received_packet.seq_num}, expected {expected_seq_num}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = ('', 12345)

    server_socket.bind(server_addr)

    total_packets = 10

    receive_packets(server_socket, total_packets)

    server_socket.close()

if __name__ == "__main__":
    main()
