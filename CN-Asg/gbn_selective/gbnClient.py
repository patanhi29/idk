import socket
import pickle
import time

WINDOW_SIZE = 4
TOTAL_PACKETS = 10
TIMEOUT = 5

class Packet:
    def __init__(self, seq_num, data):
        self.seq_num = seq_num
        self.data = data

def send_packets(client_socket, server_addr, total_packets):
    base = 0
    next_seq_num = 0
    total_frames_sent = 0

    while base < total_packets:
        while next_seq_num < base + WINDOW_SIZE and next_seq_num < total_packets:
            packet = Packet(next_seq_num, "")
            client_socket.sendto(pickle.dumps(packet), server_addr)
            print(f"Sending Frame {packet.seq_num}...")
            total_frames_sent += 1
            next_seq_num += 1

        # Receive acknowledgments
        ack_set = set()
        start_time = time.time()
        while time.time() - start_time < TIMEOUT:
            try:
                ack_data, _ = client_socket.recvfrom(1024)
                ack_packet = pickle.loads(ack_data)
                ack_set.add(ack_packet.seq_num)
            except socket.timeout:
                pass

        # Move window based on acknowledgments received
        for i in range(base, min(base + WINDOW_SIZE, total_packets)):
            if i not in ack_set:
                print(f"Timeout!! Frame number: {i} Not Received")
                next_seq_num = i
                break
        base = next_seq_num

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(TIMEOUT)
    server_addr = ('localhost', 12345)

    send_packets(client_socket, server_addr, TOTAL_PACKETS)

    client_socket.close()

if __name__ == "__main__":
    main()
