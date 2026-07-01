import platform
import socket
import psutil
from datetime import datetime

print("=" * 60)
print("          LINUX SYSTEM MONITOR")
print("=" * 60)

# ---------------- SYSTEM INFO ----------------
print("\nSYSTEM INFORMATION")
print("-" * 60)
print("Hostname          :", socket.gethostname())
print("Operating System  :", platform.system(), platform.release())
print("Machine           :", platform.machine())
print("Processor         :", platform.processor())

# ---------------- CPU ----------------
print("\nCPU INFORMATION")
print("-" * 60)
cpu = psutil.cpu_percent(interval=1)
print("CPU Usage         :", cpu, "%")

# ---------------- MEMORY ----------------
print("\nMEMORY INFORMATION")
print("-" * 60)
memory = psutil.virtual_memory()
print("Total Memory      :", round(memory.total/(1024**3), 2), "GB")
print("Available Memory  :", round(memory.available/(1024**3), 2), "GB")
print("Memory Usage      :", memory.percent, "%")

# ---------------- DISK ----------------
print("\nDISK INFORMATION")
print("-" * 60)
disk = psutil.disk_usage("/")
print("Total Disk        :", round(disk.total/(1024**3), 2), "GB")
print("Free Disk         :", round(disk.free/(1024**3), 2), "GB")
print("Disk Usage        :", disk.percent, "%")

# ---------------- UPTIME ----------------
print("\nSYSTEM UPTIME")
print("-" * 60)
boot = datetime.fromtimestamp(psutil.boot_time())
print("Boot Time         :", boot.strftime("%d-%m-%Y %H:%M:%S"))

# ---------------- PROCESSES ----------------
print("\nPROCESS INFORMATION")
print("-" * 60)
print("Running Processes :", len(psutil.pids()))

# ---------------- NETWORK ----------------
print("\nNETWORK INFORMATION")
print("-" * 60)
net = psutil.net_io_counters()
print("Bytes Sent        :", round(net.bytes_sent/(1024*1024),2), "MB")
print("Bytes Received    :", round(net.bytes_recv/(1024*1024),2), "MB")
print("Packets Sent      :", net.packets_sent)
print("Packets Received  :", net.packets_recv)

# ---------------- TOP PROCESSES ----------------
print("\nTOP RUNNING PROCESSES")
print("-" * 60)

count = 0
for p in psutil.process_iter(['pid', 'name']):
    try:
        print("PID:", p.info['pid'], " Name:", p.info['name'])
        count += 1
        if count == 5:
            break
    except:
        pass

# ---------------- ALERT SYSTEM ----------------
print("\nSYSTEM ALERTS")
print("-" * 60)

if cpu > 80:
    print("⚠️ HIGH CPU USAGE ALERT")

if memory.percent > 80:
    print("⚠️ HIGH MEMORY USAGE ALERT")

if disk.percent > 90:
    print("⚠️ HIGH DISK USAGE ALERT")

if cpu <= 80 and memory.percent <= 80 and disk.percent <= 90:
    print("✅ SYSTEM HEALTHY")

# ---------------- LOGGING ----------------
with open("logs/system.log", "a") as file:
    file.write("\n" + "=" * 70 + "\n")
    file.write(f"Timestamp : {datetime.now()}\n")
    file.write(f"CPU       : {cpu}%\n")
    file.write(f"Memory    : {memory.percent}%\n")
    file.write(f"Disk      : {disk.percent}%\n")
    file.write("=" * 70 + "\n")

print("\nLog saved to logs/system.log")
print("\nSystem Monitoring Completed Successfully")
print("=" * 60)