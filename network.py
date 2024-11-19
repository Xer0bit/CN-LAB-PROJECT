import time
import random
from utils import introduce_error, check_and_correct, calculate_checksum, verify_checksum

def send_packet(packet, sender_ip):
    delay = random.uniform(1, 5)  # Simulate delay between 1 to 5 seconds
    time.sleep(delay)
    packet = introduce_error(packet)
    checksum = calculate_checksum(packet)
    with open("packet.txt", "w") as file:
        file.write(f"{sender_ip}\n{packet}\n{checksum}")

def receive_packet():
    with open("packet.txt", "r") as file:
        sender_ip = file.readline().strip()
        packet = file.readline().strip()
        checksum = file.readline().strip()
    if verify_checksum(packet, checksum):
        packet = check_and_correct(packet)
    else:
        packet = "ERROR"
    return packet, sender_ip
