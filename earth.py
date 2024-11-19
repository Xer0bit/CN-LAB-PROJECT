import time
import random
from network import send_packet

class Earth:
    def __init__(self):
        self.ip_address = "192.168.1.1"
        self.message = "Hello, Satellite! This is a test message from Earth."
        self.packet_size = 10

    def send_data(self):
        print(f"Earth ({self.ip_address}): Sending data...")
        packets = [self.message[i:i+self.packet_size] for i in range(0, len(self.message), self.packet_size)]
        for packet in packets:
            send_packet(packet, self.ip_address)
        print(f"Earth ({self.ip_address}): Data sent.")

if __name__ == "__main__":
    earth = Earth()
    earth.send_data()
