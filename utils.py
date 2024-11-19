import random
import hashlib
import socket
import time

def introduce_error(message):
    # Introduce a random bit flip error
    if random.random() < 0.1:  # 10% chance of error
        index = random.randint(0, len(message) - 1)
        message = message[:index] + chr(ord(message[index]) ^ 1) + message[index + 1:]
    return message

def check_and_correct(message):
    # Simple parity check (for demonstration purposes)
    # In a real scenario, more sophisticated error correction would be used
    return message  # Assuming no error correction for simplicity

def calculate_checksum(message):
    return hashlib.md5(message.encode()).hexdigest()

def verify_checksum(message, checksum):
    return calculate_checksum(message) == checksum

def get_local_ip():
    try:
        # Create a socket connection to an external server to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"  # Fallback to localhost if unable to get IP

def simulate_antenna_transmission(message):
    """Simulate signal going through antenna with possible interference"""
    # Simulate transmission delay based on "atmospheric conditions"
    weather_delay = random.uniform(0.1, 0.5)
    time.sleep(weather_delay)
    
    # Simulate signal interference
    if random.random() < 0.2:  # 20% chance of interference
        interference_chars = ['*', '#', '&', '%']
        pos = random.randint(0, len(message) - 1)
        message = message[:pos] + random.choice(interference_chars) + message[pos + 1:]
    
    return message
