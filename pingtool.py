import subprocess
import sys
import re

def ping_host(host, count=10):
    print(f"\nPinging {host} ({count} packets)...\n")
    rtts = []

    for i in range(count):
        result = subprocess.run(
            ["ping", "-c", "1", host],
            capture_output=True, text=True
        )
        match = re.search(r"time=([\d.]+)", result.stdout)
        if match:
            rtt = float(match.group(1))
            rtts.append(rtt)
            print(f"RTT {i+1}: {rtt} ms")
        else:
            print(f"RTT {i+1}: Request timed out")

    if rtts:
        print(f"\nMin RTT   : {min(rtts)} ms")
        print(f"Max RTT   : {max(rtts)} ms")
        print(f"Avg RTT   : {sum(rtts)/len(rtts):.2f} ms")
        print(f"Packet Loss: {((count - len(rtts)) / count) * 100:.0f}%")
    return rtts

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "google.com"
    ping_host(host)