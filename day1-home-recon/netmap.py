#!/usr/bin/env python3
"""
netmap.py: Scans a CIDR network for live hosts via nmap ping-scan
and outputs a JSON-formatted list of devices.
"""

import subprocess
import json
import argparse
import sys

def scan_network(cidr):
    """
    Run `nmap -sn` on the target CIDR and parse the grepable output.
    Returns:
        List[Dict]: [{"ip": "1.2.3.4", "status": "Up"}, ...]
    """
    try:
        result = subprocess.run(
            ["nmap", "-sn", cidr, "-oG", "-"],
            capture_output=True,
            text=True,
            check=True
        ).stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap: {e}", file=sys.stderr)
        sys.exit(1)

    hosts = []
    for line in result:
        if line.startswith("Host:"):
            parts = line.split()
            ip = parts[1]
            status = parts[2].split("/")[0]  # e.g. "Up" from "Status: Up"
            hosts.append({"ip": ip, "status": status})
    return hosts

def main():
    parser = argparse.ArgumentParser(description="Map live hosts in a CIDR network")
    parser.add_argument("cidr", help="Network in CIDR notation (e.g. 192.168.1.0/24)")
    args = parser.parse_args()

    devices = scan_network(args.cidr)
    print(json.dumps({"devices": devices}, indent=2))

if __name__ == "__main__":
    main()
