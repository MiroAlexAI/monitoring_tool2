# monitor_log.py
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def read_log_file(log_file_path):
    """Чтение данных из лог-файла."""
    try:
        # Прочитаем строки из файла
        with open(log_file_path, 'r') as file:
            # Преобразуем каждую строку в формат JSON
            lines = [eval(line) for line in file if line.strip()]

        # Создадим DataFrame из списка словарей
        df = pd.DataFrame(lines)
        return df
    except (ValueError, FileNotFoundError) as e:
        print(f"Ошибка при чтении файла лога: {e}")
        return None

def plot_metrics(data):
    """Построение графиков для метрик.
    data_window - задаёт количество выводимых записей для графика 

    """

    data_window = 100

    data = data.tail(data_window)
    plt.figure(figsize=(5, 5))
    # Расположение в нижнем правом углу

    
    # Проверка наличия нужных столбцов
    if set(['timestamp', 'cpu_usage', 'memory_free', 'disk_free']).issubset(data.columns):
        # График для CPU Usage
        plt.subplot(3, 1, 1)
        plt.plot( data['cpu_usage'], label='CPU Usage,% '+ str(data['cpu_usage'][-1:].values), marker='o', color='red')
        #plt.title('CPU Usage, %')
        plt.grid(True)
        plt.legend()
        
        # График для Memory Usage
        plt.subplot(3, 1, 2)
        plt.plot(data['memory_free'], label='Memory Free,% '+ str(data['memory_free'][-1:].values), marker='o', color='green')
        #plt.title('Memory Usage, %')
        plt.grid(True)
        plt.legend()

        # График для Disk Free
        plt.subplot(3, 1, 3)
        # plt.plot(data['timestamp'], data['disk_free'], label='Disk Free, Gb', marker='o', color='blue')
        plt.plot(data['disk_free'], label='Disk Free '+str(data['disk_free'][-1:].values), marker='o', color='blue')
        #plt.title('Disk Free, Mb')
        plt.grid(True)
        plt.legend()
        # Вертикальные подписи даты
        plt.xticks(rotation=45)
        
        # Отображение текущего времени и даты
        plt.suptitle(datetime.now())
        plt.subplots_adjust(right=1, bottom=0, left=0, top=1)
        

        plt.tight_layout()
        plt.show(block=False)  # Не блокирует выполнение кода до закрытия графика
        plt.pause(6)  # Оставить окно открытым на секунд
        plt.close()
    else:
        print("Отсутствуют необходимые столбцы для построения графиков.")


#log_file_path = ".\log\monitoring_log.txt"

# log_data = read_log_file(log_file_path)   
# plot_metrics(log_data)

# if __name__ == "__main__":
#     log_file_path = "\monitoring_tool\log\monitoring_log.txt"
    
#     update_interval = 40
#     while True:
#         try:
#             log_data = read_log_file(log_file_path)
#             if log_data is not None:
#                 plot_metrics(log_data)
#         except Exception as e:
#             print(f"Ошибка при обновлении графика: {e}")
        
#         # Обратный отсчет таймера
#         for i in range(update_interval, 0, -1):
#             print(f"Обновление графика через {i} сек.")
#             time.sleep(1)

#         print("Обновление графика...")