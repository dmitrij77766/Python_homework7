import datetime

def search_logger(rezhim, result ):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{rezhim} = {result}. Время запроса: {str(datetime.datetime.now())} \n')
    
