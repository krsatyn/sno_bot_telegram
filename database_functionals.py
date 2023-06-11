import sqlite3
from settings import db_name
#Функционал базы данных

"""подключение базы данных"""
db_connect = sqlite3.connect(db_name, check_same_thread=False)
db_cursor = db_connect.cursor()
    
def get_gamedev_raspis():
    key_word = "Собрание GameDev"
    status = db_cursor.execute('SELECT calendarEventDateNORMAL FROM dataKeeper_calendar WHERE calendarEventTitle ==? ', (f'{key_word}',)).fetchall()
    status = status[0][-1].split(" ")
    answer = f"Ближайшее собрание по GameDev\nВремя: {status[1]}\nЧисло: {status[0]}\nПРОСЬБА НЕ ОПАЗДЫВАТЬ!"
    return answer

def get_web_raspis():
    key_word = "Собрание Web"
    status = db_cursor.execute('SELECT calendarEventDateNORMAL FROM dataKeeper_calendar WHERE calendarEventTitle ==? ', (f'{key_word}',)).fetchall()
    
    status = status[0][-1].split(" ")
    answer = f"Ближайшее собрание по Web\nВремя: {status[1]}\nЧисло: {status[0]}\nПРОСЬБА НЕ ОПАЗДЫВАТЬ!"
    return answer
