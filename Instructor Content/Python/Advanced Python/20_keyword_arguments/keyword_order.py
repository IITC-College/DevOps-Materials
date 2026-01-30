#!/usr/bin/env python3
# Keyword arguments can be in any order

def configure_server(hostname, port, protocol, timeout):
    print(f"Hostname: {hostname}")
    print(f"Port: {port}")
    print(f"Protocol: {protocol}")
    print(f"Timeout: {timeout}s")

# Order 1
configure_server(hostname="server1", port=8080, protocol="https", timeout=30)

# Order 2 (different order, same result)
configure_server(timeout=60, protocol="http", hostname="server2", port=80)

# Order 3
configure_server(port=443, timeout=45, hostname="server3", protocol="https")
