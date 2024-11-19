# SUPERIOR UNIVERSITY LAHORE
## FACALITY OF CS & IT
### DEPARTMENT OF SOFTWARE ENGINEERING

# Computer Networks
## Final Project Report

### Author(s)
- Muhammad Sameer (BSEM-F21-129)
- Haseeb
- Yonus

### Supervisor
Daniyal Qamar

# Space Communication System - Computer Networks Lab Project

## Project Overview
A comprehensive network-based simulation of Earth-to-Satellite communication implementing TCP/IP protocols and error handling mechanisms. This project:
* Simulates real-world space communication challenges
* Implements industry-standard protocols and error handling
* Demonstrates practical networking concepts in space applications

## Network Architecture

### Physical Layer
The physical layer utilizes simulated radio waves operating in the Ka-band (26.5-40 GHz) range. Key features include:
* QPSK modulation for efficient data transmission
* Ka-band frequency simulation
* Real-world signal propagation modeling

### Data Link Layer
The system implements TCP/IP protocol within a Client-Server Architecture, featuring:
* Default operation on port 65432
* Frame structure:
    * 2-byte header
    * 10-byte payload
    * 4-byte checksum
* Total packet size of 10 bytes

### Network Layer
The network architecture includes:
* Support for both IPv4 and IPv6 addressing
* Direct point-to-point routing
* QoS implementation through priority-based packet handling

### Transport Layer
Transport operations include:
* Custom TCP reliability features
* Sliding window protocol for flow control
* Modified TCP Reno for congestion management

## Key Components

### 1. Earth Station (Client)
The Earth Station functions as a TCP client with:
* Comprehensive message handling capabilities
* Automatic error recovery and retransmission
* Real-time signal strength visualization
* Dynamic power adjustment
* Doppler shift compensation

### 2. Satellite (Server)
The Satellite component features:
* TCP server functionality
* Real-time packet integrity verification
* Multiple transmission session handling
* Orbital position simulation
* Link budget calculations

## Network Reliability Features
System reliability is maintained through:
* Automatic reconnection mechanisms
* Real-time packet acknowledgment
* Session persistence
* Data integrity verification
* Weather condition simulation
* Adaptive coding and modulation
* Load balancing capabilities

## Safety Measures
Safety protocols include:
* Robust timeout handling
* Connection verification
* Error boundary checking
* Resource cleanup procedures
* Safe transmission termination
* Fallback mechanisms
* Emergency shutdown procedures

## Cisco Packet Tracer Simulation

### Network Topology
The space communication system is simulated using:
* Two dedicated routers representing Earth Station and Satellite
* Custom DCE/DTE serial connections mimicking space links
* Multiple switches for ground station distribution
* End devices simulating control terminals

### Configuration Details
The simulation implements:
* Static routing with defined metrics
* Serial interfaces with custom clock rates
* OSPF areas for network segmentation
* ACLs for security implementation

### Core Components

#### Earth Station
* Cisco 2911 Router (Primary Control)
* Layer 3 Switch (Distribution)
* 3x Workstations (Mission Control)
* Redundant Servers
* Dual Dish Antennas

#### Space Segment
* 2x AI-enabled Satellites
* Multiple IoT Devices
* Backup Communication Module

### Enhanced IP Scheme
```
Earth Core: 10.1.0.0/16
Space Segment: 172.16.0.0/16
Satellite Mesh: 192.168.0.0/16
```

### Advanced Features

#### High Availability
```
standby 1 ip 10.1.0.1
standby 1 priority 110
standby 1 preempt
```

#### QoS Implementation
```
class-map match-all CRITICAL-DATA
 match ip dscp ef
policy-map SPACE-QOS
 class CRITICAL-DATA
        priority 256
```

### Security Measures
1. IPSec Tunnels
2. Access Control Lists
3. Port Security
4. VLAN Segregation

### Performance Optimizations
* Implement OSPF for dynamic routing
* Configure load balancing
* Enable compression for data transmission
* Deploy redundant paths

### Monitoring
```
show performance
show satellite status
show link statistics
```

### Advanced Testing
1. Failover scenarios
2. Bandwidth stress testing
3. Latency measurements
4. Signal degradation simulation

## Future Enhancements
* Integration with ground radar systems
* AI-based traffic optimization
* Automated failover procedures
* Deep space communication protocols

## References
* NASA Network Standards
* Cisco Space Communications Guide
* ITU Space Regulations

> Note: Cisco 2911 routers and hubs are used for simulation purposes in Packet Tracer to represent antenna connections.