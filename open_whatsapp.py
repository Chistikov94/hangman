import webbrowser
import time

with open('numbers.txt') as f:
    numbers_list = ['7' + i.replace(' ', '')[1:] for i in f.read().split('\n')]
    print(f'В списке {len(numbers_list)} '
            f'номеров\n')
    for i in numbers_list:
        number_format = '7' + i.strip().replace(' ', '')[1:]
        link = (f'https://api.whatsapp.com/send/?phone=%2B{number_format}'
                f'&text&app_absent=0')
        webbrowser.open(link)

        while True:
            asnwer = input(f'{number_format}: ')

            if asnwer == 'n':
                break
            elif asnwer == 'e':
                with open('error_numbers.txt', 'a', encoding='utf-8') as f:
                    f.write(f'+{number_format}\n')
                print('Нет аккаунта!')
                time.sleep(1)
                break
            else:
                continue

with open('error_numbers.txt') as f:
    print('\nНомера без аккаунта в WA:')
    print(f.read())