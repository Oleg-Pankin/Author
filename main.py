with open(
    'oleg.txt','r', encoding = 'utf-8'
    )as file:
    data = file.read(1)
    print(data)
    data = file.read()
    print(data)
author = input('Автор:')
quote = ''
while quote!='нет':
    quote = input('Я жду твою цитвту олвег:')
    b = ('\n')
    author1 = input('Я все еще жду автрроа олвег:')
    a = (quote+b+author1)


with open(
    'oleg.txt','a',encoding = 'utf-8'
    )as file:
    data = file.write('\n')
    data = file.write(author)
    data = file.write('\n')
    data = file.write('\n')
    data = file.write(a)
with open(
    'oleg.txt','r', encoding = 'utf-8'
    )as file:
    data = file.read(1)
    print(data)
    data = file.read()
    print(data)