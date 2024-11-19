import json
import time
import random
import socket
from utils import introduce_error, calculate_checksum, simulate_antenna_transmission
from logger_config import setup_logger
import os

class EarthClient:
    def __init__(self, port=65432):
        # Create logs directory if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        self.logger = setup_logger('EarthClient')
        self.host = input("Enter the Satellite server IP address: ")
        self.port = port
        self.socket = None
        self.packet_size = 10
        self.max_retries = 3
        self.timeout = 10
        self.message = self.get_custom_message()
        self.keep_alive = True
        self.reconnect_attempts = 3
        self.connection_retry_delay = 2

    def get_custom_message(self):
        print("\n=== Earth Station Terminal ===")
        print("Preparing transmission...")
        return input("Enter your message to transmit to satellite: ")

    def connect(self):
        for attempt in range(self.reconnect_attempts):
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.settimeout(self.timeout)
                self.logger.info(f"Connection attempt {attempt + 1}/{self.reconnect_attempts}")
                self.socket.connect((self.host, self.port))
                self.logger.info("Successfully connected to satellite server")
                return True
            except Exception as e:
                self.logger.error(f"Connection error: {e}")
                if attempt < self.reconnect_attempts - 1:
                    self.logger.info(f"Retrying in {self.connection_retry_delay} seconds...")
                    time.sleep(self.connection_retry_delay)
        
        self.logger.error("Failed to connect after all attempts")
        return False

    def send_packet(self, packet, retry_count=0):
        if retry_count >= self.max_retries:
            self.logger.error(f"Failed to send packet after {self.max_retries} attempts")
            return False

        try:
            # Simulate antenna transmission
            packet = simulate_antenna_transmission(packet)
            checksum = calculate_checksum(packet)
            packet_data = {
                'packet': packet,
                'checksum': checksum
            }
            
            self.logger.debug(f"Transmitting: {packet}")
            print(f"\n{'=' * 50}")
            print(f"Transmitting packet through antenna...")
            print(f"Signal strength: {'|' * random.randint(1, 10)}")
            print(f"Frequency: {random.randint(100, 150)} MHz")
            print(f"{'=' * 50}")
            
            self.socket.sendall(json.dumps(packet_data).encode())
            
            # Wait for acknowledgment
            response = self.socket.recv(1024).decode()
            if not response:
                self.logger.error("Lost connection to server")
                if self.connect():  # Try to reconnect
                    return self.send_packet(packet, retry_count)
                return False
            if response == "NACK":
                self.logger.warning(f"Packet transmission failed, retrying... ({retry_count + 1}/{self.max_retries})")
                time.sleep(1)  # Wait before retry
                return self.send_packet(packet, retry_count + 1)
            
            self.logger.info("Packet acknowledged")
            return True

        except socket.timeout:
            self.logger.error("Timeout while sending packet")
            return self.send_packet(packet, retry_count + 1)
        except socket.error as e:
            self.logger.error(f"Socket error: {e}")
            if self.connect():  # Try to reconnect
                return self.send_packet(packet, retry_count)
            return False
        except Exception as e:
            self.logger.error(f"Error sending packet: {e}")
            return False

    def send_data(self):
        if not self.socket:
            self.logger.error("Not connected to server")
            return

        try:
            # Split message into packets
            packets = [self.message[i:i+self.packet_size] 
                      for i in range(0, len(self.message), self.packet_size)]
            
            total_packets = len(packets)
            successful_packets = 0
            
            self.logger.info("Starting data transmission")
            for i, packet in enumerate(packets, 1):
                self.logger.info(f"\nSending packet {i}/{total_packets}")
                time.sleep(random.uniform(1, 3))  # Simulate transmission delay
                if self.send_packet(packet):
                    successful_packets += 1
                else:
                    self.logger.error(f"Failed to send packet {i}")
                    if not self.connect():  # Try to reconnect
                        break

            self.logger.info(f"\nTransmission summary:")
            self.logger.info(f"Total packets: {total_packets}")
            self.logger.info(f"Successfully sent: {successful_packets}")
            self.logger.info(f"Failed: {total_packets - successful_packets}")

        except Exception as e:
            self.logger.error(f"Error during transmission: {e}")
        finally:
            try:
                # Send end transmission signal
                if self.socket:
                    try:
                        end_packet = {
                            'packet': 'END_TRANSMISSION',
                            'checksum': calculate_checksum('END_TRANSMISSION')
                        }
                        self.socket.sendall(json.dumps(end_packet).encode())
                    except:
                        pass
                    self.socket.close()
                self.logger.info("Connection closed")
            except:
                pass

if __name__ == '__main__':
    os.system('clear')
    print("\n🛰️  Space Communication System - Earth Station")
    print("============================================")
    while True:
        client = EarthClient()
        if client.connect():
            client.send_data()
        
        retry = input("\nWould you like to send another message? (y/n): ").lower()
        if retry != 'y':
            break
    
    print("Earth client shutting down")