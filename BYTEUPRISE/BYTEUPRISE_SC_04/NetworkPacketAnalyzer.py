from scapy.all import sniff, IP, TCP, UDP, ICMP, conf

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Determine protocol type
        if protocol == 6:
            protocol_type = "TCP"
        elif protocol == 17:
            protocol_type = "UDP"
        elif protocol == 1:
            protocol_type = "ICMP"
        else:
            protocol_type = "Other"

        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {protocol_type}")

        # If it's TCP or UDP, print the payload
        if protocol in [6, 17]:  # TCP or UDP
            payload = packet[IP].payload
            print(f"Payload: {payload}")
        print("-" * 50)

# Start sniffing
def start_sniffing(interface=None):
    # Do not explicitly set conf.L3socket; use the default
    if interface:
        sniff(iface=interface, prn=packet_callback, store=0)
    else:
        sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    print("Starting packet sniffer...")
    start_sniffing(interface=None)