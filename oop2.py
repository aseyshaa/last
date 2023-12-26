from random import randint


# Определение функций для каждого состояния
# Паттерн: Состояние (State)
def start(claim):
    print('Некоторый запрос создан.')
    claim['state'] = 'analyze'


def analyze(claim):
    print('Анализ запроса...')
    if randint(0, 1) == 1:
        print('Запрос принят в обработку.')
        claim['state'] = 'processing'
    else:
        print('Запрос не принят в обработку. Требуется дополнительная информация.')
        claim['state'] = 'clarify'


def processing(claim):
    print('Запрос выполнен.')
    claim['state'] = 'close'


def clarify(claim):
    if randint(0, 5) == 5:
        print('Пользователь отозвал запрос.')
        claim['state'] = 'close'
    else:
        print('Дополнительная информация получена.')
        claim['state'] = 'analyze'


def close(claim):
    print('')
    claim['state'] = None


# Определение паттерна - машина состояний
state = {'start': start,
         'analyze': analyze,
         'processing': processing,
         'clarify': clarify,
         'close': close}


def run_claim():
    # Новая заявка
    claim = {'state': 'start'}
    # выполняем процесс, пока не будет конца
    while claim['state'] is not None:
        # определяем функцию
        foo = state[claim['state']]
        foo(claim)


if __name__ == "__main__":
    run_claim()
