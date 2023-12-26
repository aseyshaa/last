from random import randint


class Claim:
    def __init__(self):
        self.state = 'start'
    
    def start(self):
        print('Некоторый запрос создан.')  # Вывод сообщения о создании запроса
        self.state = 'analyze'  # Изменение состояния на 'analyze'
    
    def analyze(self):
        print('Анализ запроса...')  # Вывод сообщения о процессе анализа
        if randint(0, 1) == 1:  # Случайный выбор в диапазоне [0,1]
            print('Запрос принят в обработку.')  # Вывод сообщения о принятии запроса в обработку
            self.state = 'processing'  # Изменение состояния на 'processing'
        else:
            print('Запрос не принят в обработку. Требуется дополнительная информация.')  # Вывод сообщения о требовании дополнительной информации
            self.state = 'clarify'  # Изменение состояния на 'clarify'
    
    def processing(self):
        print('Запрос выполнен.')  # Вывод сообщения о выполнении запроса
        self.state = 'close'  # Изменение состояния на 'close'
    
    def clarify(self):
        if randint(0, 5) == 5:  # Случайный выбор в диапазоне [0,5]
            print('Пользователь отозвал запрос.')  # Вывод сообщения о отзыве запроса
            self.state = 'close'  # Изменение состояния на 'close'
        else:
            print('Дополнительная информация получена.')  # Вывод сообщения о получении дополнительной информации
            self.state = 'analyze'  # Изменение состояния на 'analyze'
    
    def close(self):
        print('')  # Пустой вывод
        self.state = None  # Изменение состояния на None
    
    def run(self):
        while self.state is not None:  # Цикл, пока состояние не равно None
            if self.state == 'start':  # Если состояние равно 'start', вызывается метод start()
                self.start()
            elif self.state == 'analyze':  # Если состояние равно 'analyze', вызывается метод analyze()
                self.analyze()
            elif self.state == 'processing':  # Если состояние равно 'processing', вызывается метод processing()
                self.processing()
            elif self.state == 'clarify':  # Если состояние равно 'clarify', вызывается метод clarify()
                self.clarify()
            elif self.state == 'close':  # Если состояние равно 'close', вызывается метод close()
                self.close()


if __name__ == "__main__":
    claim = Claim()  # Создание объекта класса Claim
    claim.run()  # Запуск работы объекта
