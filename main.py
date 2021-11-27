while True:
    try:
        name = input('Название файла:')
        with open(
            name,'r', encoding = 'utf-8'
            )as file:
            data = file.read(1)
            print(data)
            data = file.read()
            print(data)
        author = input('Автор:')
        quote = ''
        a = ''
        with open(
            name,'a',encoding = 'utf-8'
            )as file:
            file.write('\n')
            file.write('({})'.format(author))
            file.write('\n')
            while quote!='нет':
                file.write(a)
                quote = input('Я жду твою цитвту олвег:')
                b = '\n'
                author1 = input('Я все еще жду автрроа олвег:')
                a = quote+b+'({})'.format(author1)
                file.write('\n')
        with open(
            name,'r', encoding = 'utf-8'
            )as file:
            data = file.read(1)
            print(data)
            data = file.read()
            print(data)
            break
    except:
        print('Файла несувщеcтвует')