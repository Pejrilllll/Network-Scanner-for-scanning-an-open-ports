import socket
from datetime import datetime

# Daftar port umum yang sering digunakan

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MYSQL",
    3389: "RDP",
    5900: "VNC",
    8080: "HTTP-Proxy"
}

def scan_host(target, ports):
    print(f"\n[ Scanning Target: {target} ]")
    print(f"Time Started: {datetime.now()}\n")

    open_ports = []

    for port in ports:
        try: 
            # Membuat socket TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5) # batas waktu koneksi
            result = sock.connect_ex((target, port))

            if result == 0: # port terbuka
                service = common_ports.get(port, "Unknown")
                print(f"[+] Port {port} OPEN ({service})")
                open_ports.append((port, service))

                sock.close()

        except KeyboardInterrupt:
            print("\n[!] Scan dihentikan oleh user.")
            break
        except socket.gaierror:
            print("\n[!] Hostname tidak dapat ditemukan.")
            break
        except socket.error:
            print(f"\n[!] Server tidak merespon.")
            break
    
    print("\nScan Selesai.")
    if open_ports:
        print(f"\nHost {target} | Open Ports: ", end="")
        print(", ".join([f"{p}({s})" for p, s in open_ports]))
    else:
        print(f"Tidak ada port terbuka di {target}.")

# ==============
# Main Program
# ==============

if __name__ == "__main__":
    target_ip = input("Masukkan IP target: ")

    port_range = range(1, 1025) # Scan port 1-1024

    scan_host(target_ip, port_range)