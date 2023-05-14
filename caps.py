import tkinter

print(
    """
    Вас приветствует программа для перевода обычного текста в CAPS!
    Введите текст, который нужно перевести в верхний регистр и программа сделает это!
    Если оставить поле пустым, программа завершится!
    
    Powered by kwOks!
    """
)
tk = tkinter.Tk()


while 1:
    
    
    text = input('Обычный текст: ')
    new_text = ''
    
    if text == '':
        break
    
    print('CAPS текст: ', end='')
    for i in text:
        new_text += i
    new_text = new_text.upper()
    tk.clipboard_clear()
    tk.clipboard_append(new_text)
    print(new_text)
    print('\n')

