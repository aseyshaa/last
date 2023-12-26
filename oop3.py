from random import randint


def run_claim_without_pattern():
    # Новая заявка
    claim = {'state': 'start'}
    # выполняем процесс, пока не будет конца
    while claim['state'] is not None:
        if claim['state'] == 'start':
            print('Некоторый запрос создан.')
            claim['state'] = 'analyze'
        elif claim['state'] == 'analyze':
            print('Анализ запроса...')
            if randint(0, 1) == 1:
                print('Запрос принят в обработку.')
                claim['state'] = 'processing'
            else:
                print('Запрос не принят в обработку. Требуется дополнительная информация.')
                claim['state'] = 'clarify'
        elif claim['state'] == 'processing':
            print('Запрос выполнен.')
            claim['state'] = 'close'
        elif claim['state'] == 'clarify':
            if randint(0, 5) == 5:
                print('Пользователь отозвал запрос.')
                claim['state'] = 'close'
            else:
                print('Дополнительная информация получена.')
                claim['state'] = 'analyze'
        elif claim['state'] == 'close':
            print('')
            claim['state'] = None


if __name__ == "__main__":
    run_claim_without_pattern()
