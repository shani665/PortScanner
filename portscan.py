import socket

def scan_ports(target_ip, start_port, end_port):
    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except socket.gaierror:
            print("Invalid host. Please check the IP address.")
            break
        except socket.error:
            print("Socket error.")
            break

    if not open_ports:
        print("\nNo open ports found.")
    else:
        print(f"\nScan complete. Open ports: {open_ports}")

# Input handling
def get_user_input():
    try:
        target = input("Enter IP address to scan: ").strip()
        socket.inet_aton(target)  # validate IP
        start = int(input("Enter start port: "))
        end = int(input("Enter end port: "))
        if start < 0 or end > 65535 or start > end:
            print("Invalid port range. Must be 0–65535 and start < end.")
            return
        scan_ports(target, start, end)
    except ValueError:
        print("Invalid input. Ports must be numbers.")
    except socket.error:
        print("Invalid IP address.")

# Run the scanner
get_user_input()

