# Network Delay Measurement Tool

Measures and analyzes latency (RTT) between your machine and remote hosts.

## Features
- Measure RTT using ping
- Compare delay across multiple hosts
- Plot RTT variations over time

## Run
pip install -r requirements.txt
python ping_tool.py google.com
python analyze.py
python plot_rtt.py

## Concepts
- End-to-end delay & queuing delay
- Packet loss detection
- RTT as a measure of propagation + transmission delay
