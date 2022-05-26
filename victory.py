"""
Используя любые средства написать программу викторина:
Выбрать минимум 5 известных людей и узнать их год рождения.
Программа должна по очереди спрашивать у пользователя год рождения знаменитости.
После того как пользователь ввел все ответы, программа считает и выводит на экран:
- количество правильных ответов
- количество ошибок
- процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ)
- процент неправильных ответов
После вывода информации программа спрашивает пользователя хочет ли он начать игру сначала,
если да - то повторяем все сначала, если ответ нет - выходим из программы
"""
bornyear_churchill = 1874
bornyear_gandhi = 1869
bornyear_michelangelo = 1475
bornyear_pelevin = 1962
bornyear_dud = 1986
bornyear_ivanterrible = 1530
toRepeat = True
while toRepeat:
    correct_answer_num = 0
    answer = input("Введите год рождения У.Черчиля: ")          # 1874
    if answer.isdigit():
        answer = int(answer)
        if answer == bornyear_churchill:
            correct_answer_num += 1
    answer = input("Введите год рождения М.Ганди: ")            # 1869
    if answer.isdigit():
        answer = int(answer)
        if answer == bornyear_gandhi:
            correct_answer_num += 1
    answer = input("Введите год рождения Микельанджело: ")      # 1475
    if answer.isdigit():
        answer = int(answer)
        if answer == bornyear_michelangelo:
            correct_answer_num += 1
    answer = input("Введите год рождения В.Пелевина: ")         # 1962
    if answer.isdigit():
        answer = int(answer)
        if answer == bornyear_pelevin:
            correct_answer_num += 1
    answer = input("Введите год рождения Ю.Дудя: ")             # 1986
    if answer.isdigit():
        answer = int(answer)
        if answer == bornyear_dud:
            correct_answer_num += 1
    answer = input("Введите год рождения Ивана Грозного: ")     # 1530
    if answer.isdigit():
        answer = int(answer)
        if answer == bornyear_ivanterrible:
            correct_answer_num += 1
    correct_answer_proc = correct_answer_num/6
    print('Ваш результат:')
    print('\tПравильных ответов:\t', correct_answer_num)
    print('\tНеправильных ответов:', 6 - correct_answer_num)
    print('\tПроцент правильных ответов {:5.1%}'.format(correct_answer_proc))
    print('\tПроцент неправильных ответов {:5.1%}'.format(1 - correct_answer_proc))
    answer = input("Хотите начать игру заново (да/нет): ")
    if answer != 'да':
        toRepeat = False