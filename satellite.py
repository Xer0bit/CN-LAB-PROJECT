from network import receive_packet

class Satellite:
    def __init__(self):
        self.ip_address = "192.168.1.2"
        self.received_message = ""

    def receive_data(self):
        print(f"Satellite ({self.ip_address}): Waiting for data...")
        while True:
            packet, sender_ip = receive_packet()
            if packet == "END":
                break
            self.received_message += packet
            print(f"Satellite ({self.ip_address}): Received packet from {sender_ip} - {packet}")
        print(f"Satellite ({self.ip_address}): Complete message received - {self.received_message}")

if __name__ == "__main__":
    satellite = Satellite()
    satellite.receive_data()
