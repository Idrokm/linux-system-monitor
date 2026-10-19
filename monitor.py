import psutil
import time

def check_system_performance():
    print("=== Linux System Monitor ===")
    try:
        while True:
            # CPU ishlatilishi
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Operativ xotira (RAM) ishlatilishi
            memory = psutil.virtual_memory()
            ram_usage = memory.percent
            
            # Disk xotirasi ishlatilishi
            disk = psutil.disk_usage('/')
            disk_usage = disk.percent
            
            print(f"[CPU]: {cpu_usage}% | [RAM]: {ram_usage}% | [Disk]: {disk_usage}%")
            
            # 5 sekund kutish
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nMonitoring to'xtatildi.")

if __name__ == "__main__":
    check_system_performance()import psutil
import time

def check_system_performance():
    print("=== Linux System Monitor ===")
    try:
        while True:
            # CPU ishlatilishi
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Operativ xotira (RAM) ishlatilishi
            memory = psutil.virtual_memory()
            ram_usage = memory.percent
            
            # Disk xotirasi ishlatilishi
            disk = psutil.disk_usage('/')
            disk_usage = disk.percent
            
            print(f"[CPU]: {cpu_usage}% | [RAM]: {ram_usage}% | [Disk]: {disk_usage}%")
            
            # 5 sekund kutish
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nMonitoring to'xtatildi.")

if __name__ == "__main__":
    check_system_performance()
