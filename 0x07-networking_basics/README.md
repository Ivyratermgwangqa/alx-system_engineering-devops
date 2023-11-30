```markdown
# Networking Basics Project

This project aims to provide a foundational understanding of networking basics. It covers topics such as the OSI model, types of networks, MAC and IP addresses, TCP and UDP protocols, ports, and network connectivity using ICMP.

## Table of Contents
1. [OSI Model](#osi-model)
2. [Types of Network](#types-of-network)
3. [MAC and IP Address](#mac-and-ip-address)
4. [TCP and UDP](#tcp-and-udp)
5. [TCP and UDP Ports](#tcp-and-udp-ports)
6. [Is the Host on the Network](#is-the-host-on-the-network)

## OSI Model
### What is the OSI model?
The OSI (Open Systems Interconnection) model is a conceptual framework that characterizes the communication functions of a telecommunication system. It consists of seven layers, each serving a specific purpose in network communication.

### How is the OSI model organized?
The OSI model is organized from the lowest to the highest level, with layer 1 dealing with physical transmission and layer 7 handling application-specific communication.

## Types of Network
### What type of network is a computer in a local connected to?
- Internet
- WAN
- LAN

### What type of network could connect offices in different buildings?
- Internet
- WAN
- LAN

### What network is used when browsing www.google.com from a smartphone?
- Internet
- WAN
- LAN

## MAC and IP Address
### What is a MAC address?
A MAC (Media Access Control) address is the unique identifier of a network interface.

### What is an IP address?
An IP (Internet Protocol) address is similar to a postal address for houses, serving as a unique identifier for network devices.

## TCP and UDP
### Which statement is correct for the TCP box?
- It transfers data slowly but surely.
- It transfers data fast and may lose data in the process.

### Which statement is correct for the UDP box?
- It transfers data slowly but surely.
- It transfers data fast and may lose data in the process.

### Which statement is correct for the TCP worker?
- Have you received boxes x, y, z?
- May I increase the rate at which I am sending you boxes?

## TCP and UDP Ports
This script displays listening ports, showing only listening sockets and providing PID and program information.

Usage:
```bash
sudo ./4-TCP_and_UDP_ports
```

## Is the Host on the Network
This script pings an IP address passed as an argument, performing 5 ping requests.

Usage:
```bash
./5-is_the_host_on_the_network {IP_ADDRESS}
```

Note: Replace `{IP_ADDRESS}` with the desired IP address.

---

**Learning Objectives:**
- Understand the OSI model and its layers.
- Differentiate between types of networks.
- Recognize MAC and IP addresses.
- Differentiate between TCP and UDP protocols.
- Identify commonly used TCP/UDP ports.
- Check network connectivity using ICMP.

**Author:** [Lerato Mgwangqa]
