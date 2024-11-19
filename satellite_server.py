import socket
import json
from utils import check_and_correct, verify_checksum, get_local_ip
from logger_config import setup_logger
import os
import random

class SatelliteServer:
    def __init__(self, port=65432):
        # Create logs directory if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        self.logger = setup_logger('SatelliteServer')
        self.host = get_local_ip()
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.received_message = ""
        self.setup_server()
        print("\n=== Space Communication System - Satellite ===")
        print("============================================")
        print("Satellite systems initializing...")

    def setup_server(self):
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            self.logger.info(f"Server initialized on {self.host}:{self.port}")
        except Exception as e:
            self.logger.error(f"Server setup failed: {e}")
            raise

    def _handle_connection(self, conn, addr):
        self.logger.info(f"New transmission detected from {addr}")
        buffer = ""
        
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break

                buffer += data
                try:
                    packet_data = json.loads(buffer)
                    buffer = ""  # Clear buffer after successful parse
                    
                    if packet_data['packet'] == 'END_TRANSMISSION':
                        self.logger.info("End of transmission received")
                        print("\n=== Transmission Complete ===")
                        conn.sendall(b"ACK")
                        break

                    # Show reception visualization
                    print(f"\n{'=' * 50}")
                    print(f"📡 Receiving signal...")
                    print(f"Signal strength: {'▀' * random.randint(1, 10)}")
                    print(f"Frequency: {random.randint(100, 150)} MHz")
                    print(f"{'=' * 50}")

                    if verify_checksum(packet_data['packet'], packet_data['checksum']):
                        packet = check_and_correct(packet_data['packet'])
                        self.received_message += packet
                        self.logger.info(f"Received: {packet}")
                        conn.sendall(b"ACK")
                    else:
                        self.logger.warning("Signal interference detected!")
                        conn.sendall(b"NACK")

                except json.JSONDecodeError:
                    continue  # Wait for more data
                
            except Exception as e:
                self.logger.error(f"⚠️ Signal error: {e}")
                break

        self.logger.info(f"Complete transmission received: {self.received_message}")
        conn.close()

    def start(self):
        self.logger.info("Starting server...")
        while True:
            try:
                conn, addr = self.socket.accept()
                self._handle_connection(conn, addr)
            except KeyboardInterrupt:
                self.logger.info("Server shutting down...")
                break
            except Exception as e:
                self.logger.error(f"Error: {e}")
                continue

        self.socket.close()
        self.logger.info("Server stopped")

if __name__ == '__main__':
    os.system('clear')
    server = SatelliteServer()
    server.start()