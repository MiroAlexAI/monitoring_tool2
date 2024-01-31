

### Программа monitoring_tool разработана для сбора данных CPU, RAM, Disk в OS Windows 10 в log файл и вывод графика на 6 секунд 

разработана c использованием:
- Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
- matplotlib==3.7.4
- pandas==2.0.3
- psutil==5.8.0
- schedule==1.1.0
- WMI==1.5.1

### Запуск

 - Распаковать архив и запустить файл Start.CMD  
или 
 - ввести в CMD:
   
>pip install -r requirements.txt
>
>python main.py
>
![image](https://github.com/MiroAlexAI/monitoring_tool2/assets/126348122/cfb17d15-e5ae-46cd-b3d6-58db02044ddc)


#### Два режима работы:

1. Сбор логов - вывод в консоль - сохранение в файл - вывод/авто закрытие графика (100 последних значений)
2. Сбор логов - вывод в консоль - сохранение в файл

#### Пример файла monitoring_log.txt:

>{'timestamp': '2024-01-30 23:30:18', 'cpu_usage': 3.1, 'memory_free': 66.3, 'disk_free': 736328}
>
>{'timestamp': '2024-01-30 23:30:25', 'cpu_usage': 2.2, 'memory_free': 66.7, 'disk_free': 736329}
>

#### Интерфейс программы
![image](https://github.com/MiroAlexAI/monitoring_tool2/assets/126348122/361ccf6c-a664-4127-97b4-63c61f1142ca)
