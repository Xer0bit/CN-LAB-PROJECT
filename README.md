# Space Communication System

A simulated space communication system demonstrating client-server architecture with error handling, packet transmission, and satellite communications.

## Overview

This project simulates a space communication system between an Earth station (client) and a Satellite (server). It implements various networking concepts including:

- TCP/IP communication
- Packet transmission and acknowledgment
- Error detection and correction
- Signal interference simulation
- Logging and monitoring

## Simulation Example

![Packet Simulation](images/packet_simulation.png)
*Network simulation showing packet flow between Earth station and Satellite*

## System Architecture

![System Architecture](images/system_diagram.png)
*High-level architecture diagram of the communication system*

## Components

- `earth_client.py` - Earth station that sends messages
- `satellite_server.py` - Satellite server that receives transmissions
- `utils.py` - Utility functions for error handling and network operations
- `logger_config.py` - Logging configuration and setup
- `satellite.py` - Base satellite class implementation

## Features

- Real-time signal strength visualization
- Packet acknowledgment system
- Automatic reconnection attempts
- Error detection using checksums
- Simulated atmospheric interference
- Comprehensive logging system

## Requirements

- Python 3.6+
- Standard library modules (socket, json, logging)

## Usage

1. Start the satellite server:
```bash
python satellite_server.py
```

2. Launch the earth client:
```bash
python earth_client.py
```

3. Follow the prompts to input the satellite server IP and message to transmit

## Error Handling

The system includes:
- Packet corruption detection
- Automatic retransmission
- Connection loss recovery
- Timeout handling

## Logging

All communications are logged to the `logs` directory with:
- Timestamp information
- Error reports
- Transmission status
- Signal quality metrics

## Credits

Developed by Sameer