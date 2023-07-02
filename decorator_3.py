##Доработать функцию flat_generator. Должен получиться генератор,
##который принимает список списков и возвращает их плоское представление.
##Функция test в коде ниже также должна отработать без ошибок.



import types
import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        dt_now = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as f:
            information =[f'Время вызова функции: {dt_now}\n',f'Название функции: {old_function.__name__}\n',
            f'Аргументы: {args}, {kwargs}\n', f'Возвращаемое значение: {result}\n', '\n'*2]
            f.writelines(information)
        return result

    return new_function



##@logger
def flat_generator(list_of_lists):
    for number in list_of_lists:
        for item in number:
            yield item


gen = logger(flat_generator)

##list_of_lists = [
##        ['a', 'b', 'c'],
##        ['d', 'e', 'f', 'h', False],
##        [1, 2, None]
##    ]
##
##print(list(flat_generator(list_of_lists)))


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()