from Poison import *

def append() -> None:
    """
        Appeng new item to dictionary of medicals
    """
    global p
    name = input('\nНазвание зелья? ')
    if name in p.medicals.keys():
        print('Такое зелье уже есть')
        return
    subjects = input('Состав зелья? ')
    cost = input('Цена? ') 
    p.medicals[name] = (subjects, cost)

def edit() -> None:
    """
        Edit medical in existing dictionary
    """
    global p
    name = input('\nНазвание зелья? ')
    if name not in p.medicals.keys():
        print('Такого зелья нет')
        return
    subjects = input('Состав зелья? ')
    cost = input('Цена? ') 
    p.medicals[name] = (subjects, cost)

def delete():
    global p
    name = input('\nНазвание зелья? ')
    if name not in p.medicals.keys():
        print('Такого зелья нет')
        return
    else:
        del p.medicals[name]

def show_content():
    global p
    print('\n\n')
    for k, v in p.medicals.items():
        print(k, *v)


p = Poison()

while True:
    show_content()
    i = input('\n1 - Добавить новое зелье\n2 - Редактировать\n3 - Удалить\n4 - Выйти\n')
    if i == '4':
        break
    elif i == '1':
        append()
    elif i == '2':
        edit()
    elif i == '3':
        delete()
