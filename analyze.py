from pingtool import ping_host

hosts = ["google.com", "github.com", "yahoo.com"]

results = {}
for host in hosts:
    rtts = ping_host(host, count=5)
    if rtts:
        results[host] = round(sum(rtts) / len(rtts), 2)

print("\n--- Comparison ---")
for host, avg in sorted(results.items(), key=lambda x: x[1]):
    print(f"{host}: {avg} ms avg RTT")
