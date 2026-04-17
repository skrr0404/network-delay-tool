import matplotlib.pyplot as plt
from pingtool import ping_host

host = "google.com"
rtts = ping_host(host, count=20)

plt.figure(figsize=(10, 4))
plt.plot(rtts, marker='o', color='steelblue', linewidth=1.5)
plt.axhline(sum(rtts)/len(rtts), color='red', linestyle='--', label='Avg RTT')
plt.title(f"RTT over time — {host}")
plt.xlabel("Packet #")
plt.ylabel("RTT (ms)")
plt.legend()
plt.tight_layout()
plt.savefig("rtt_plot.png")
plt.show()
