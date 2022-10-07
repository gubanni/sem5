def InputText(text):
    textr = input(f"{text}")
    return textr

def createText():
    with open('textZ3.txt','w', encoding='UTF-8' ) as file:
        file.write(InputText("Введите первоночальный текст: "))
    
     
def readText():
    with open('textZ3.txt','r') as file:
        my_text = file.readline()
        change_text = my_text.split()
        return change_text

createText()
change_text = readText()

del_text = InputText('Введите набор букв, который нужно искать в словах для удаления :  ')

result = ' '.join(filter(lambda x: del_text not in x, change_text))
with open('textZ3.txt','w', encoding='UTF-8') as file:
    file.write(f'{result}')
print(result)