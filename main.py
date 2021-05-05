import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def favorite_movie(movie_name):
    print(f"My favorite movie is named {movie_name}. ")


def print_country(dict_country):
    print(dict_country)


def make_country(name, capital):
    dict_country = {name: capital}
    print_country(dict_country)


def make_operation(sign, *args):
    if sign in OPERATORS:
        args = list(args)
        while len(args) > 2:
            arg0 = args.pop(0)
            arg1 = args.pop(0)
            args.insert(0, OPERATORS[sign](arg0, arg1))
        return OPERATORS[sign](args[0], args[1])

    return "ERROR"


def print_word_dict(word_for_display, list_ch):
    print("Divine word -> ", end="")
    for ch in word_for_display:
        print(ch if ch.lower() in list_ch else "*", end="")
    print()


def print_ask_and_input():
    return input("Choose a letter: ")


def winner_check(word_for_display, list_ch):
    for ch in word_for_display:
        if ch not in list_ch:
            return False
    return True


if __name__ == '__main__':
    # Task 1
    """
    A simple function.
    
    Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. 
    The function should then print “My favorite movie is named {name}”.
    """

    favorite_movie("Aliens")

    # Task 2
    """
    Creating a dictionary.
    
    Create a function called make_country, which takes in a country’s name and capital as parameters. 
    Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
    Make the function print out the values of the dictionary to make sure that it works as intended.
    """

    make_country("Ukraine", "Kiev")

    # Task 3
    """
    A simple calculator.
    
    Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
    (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) 
    as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. 
    For example:    
    the call make_operation(‘+’, 7, 7, 2) should return 16
    the call make_operation(‘-’, 5, 5, -10, -20) should return 30
    the call make_operation(‘*’, 7, 6) should return 42  
    """

    print(make_operation('+', 7, 7, 2, 4))
    print(make_operation('-', 5, 5, -10, -20))
    print(make_operation('*', 7, 6, 5))

    # Task Виселица
    """
    Пишем игру виселица. Храним десяток слов и рандомно загадываем. 
    Показываем звездочки вместо букв закрытых. Человек дает букву если не угадал "рисуем" ему элемент виселицы.  
    """
    word = "Ambassador"
    list_answers = []
    while not winner_check(word, list_answers):
        print_word_dict(word, list_answers)
        char = print_ask_and_input().lower()
        if char == "stop":
            break
        list_answers.append(char)
    else:
        print("you are winner")
    # Task 21
    """
    Пишем игру в 21. 
    Создать массив "карт" рандомно их перемешать и выдавать "игроку" пока не скажет стоп или не проиграет. 

    карта - словарь. Масть, Название, очки.  Не надо мудрить с "вариантами очков карт" упрощенно. 
    Интересует работа с циклами, словарями, функциями :)
    Помним про единую ответственность. Разбиваем на примитивные действия. 
    С начала пишем каркас с запассенными функциями, а потом заполняем "пропуски". 
    
    пока не стоп или перебор
     предложить карту
     вывести текущие очки.
    если не перебор набирать себе карт 
    """
