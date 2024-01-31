# utils.py
import psutil
import wmi
from datetime import datetime

def collect_system_data():
    """Сбор данных о системе."""
    #print("Сбор данных о системе")
    cpu_usage = psutil.cpu_percent(interval=0.5)
    
    # Используем WMI для получения данных о памяти и диске
    w = wmi.WMI()
    
    # Используем явное преобразование к числам
    free_physical_memory = int(w.Win32_OperatingSystem()[0].FreePhysicalMemory)
    total_visible_memory = int(w.Win32_OperatingSystem()[0].TotalVisibleMemorySize)

    memory_usage = (free_physical_memory / total_visible_memory) * 100
    disk_free = psutil.disk_usage('C:').free
    

    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_usage": cpu_usage,
        "memory_free": round(memory_usage,1),
        "disk_free": int(disk_free/10240),
    }
    print(data)
    return data

def write_to_log(data, log_file_path ="log/monitoring_log.txt"):
    """Запись данных в лог-файл."""
    #print(f"Запись данных в лог-файл {log_file_path}")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{data}\n")
    #print("завершена успешно")
