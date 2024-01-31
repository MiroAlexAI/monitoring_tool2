# main.py

import os
import psutil
import schedule
import time
import wmi
from monitor_log import read_log_file, plot_metrics
from utils import collect_system_data, write_to_log

print("-*"*25)
print("Программа для сбора данных CPU, RAM, Disk в файл и вывод графика")

print("Для отключения вывода графиков веведите число: 2")
monitor =  input("Отключить вывод графиков ? :")

if monitor=="2" :
    print("Отображение графиков OFF")
    monitor_flag = True
else:
    print("Отображение графиков ON")
    monitor_flag = False
print("-*"*25)

log_file_path = ".\log\monitoring_log.txt"






def main(log_file_path):
    # Настройки
    print("Start Main func data")
    data = collect_system_data()
    write_to_log(data)

    # Проверяем, существует ли файл
    if not os.path.exists(log_file_path):
    # Если файл не существует, создаем его
        with open(log_file_path, 'w') as file:
            print("Инициализация файла")
        # Можно написать что-то в файл, если это необходимо


    



        # Настройка интервала для сбора и записи данных
    interval_minutes = 0.1

    print("interval_minutes =",interval_minutes)

    # Запуск периодического сбора данных и записи в лог-файл
    schedule.every(interval_minutes).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def job():
    # Сбор данных и запись в лог-файл

    # print("Сбор данных и запись в лог-файл...")
    data = collect_system_data()
    write_to_log(data)
    # Чтение файла и вывод графиков через monitor_log  
    if monitor_flag == False:
        #print("Задача завершена. /n Вывод графика на 5 сек")
        data = read_log_file(log_file_path)
        plot_metrics(data)

main(log_file_path)
