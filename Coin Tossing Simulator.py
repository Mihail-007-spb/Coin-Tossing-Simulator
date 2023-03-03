"""Coin Tossing Simulator"""

"""Симулятор подбрасывания монеты (Орел или Решка)"""

from random import randint


def main():
    print()
    print('******* Программа имитации подбрасывания монетки *******')
    n_or = 0
    n_re = 0
    N = 0
    st = '_'
    s = 'None'
    while s != 'n':
            n = 'None'
            while not n.isdigit():
                n = input('Введите ЧИСЛО РАЗ подбрасывания монеты: ')
                n = n.replace(' ', '')
                if n == '':
                    print()
                    print('Ошибка ввода! Введите значение.')
                elif not n.isdigit():
                    print()
                    print('Ошибка ввода! Введите только цифры.')
               
            while N != int(n):
                g = randint(1, 2)
                if g == 1:
                    n_or += 1
                    N += 1
                else:
                    n_re += 1
                    N += 1
            Orel = n_or / int(n) * 100
            Reska = 100 - Orel
            print()
            print(50*st)
            print(f'Всего было подбрасываний монеты: <{int(n):,}> раз')
            print(f'   <Орел>  выпал  в: {Orel: .1f} % случаев')
            print(f'   <Решка> выпала в: {Reska: .1f} % случаев')
            print(50*st)
            print()
            s = 'None'
            while s != 'y' and s != 'n':
                s = input('Для ПРОДОЛЖЕНИЯ выберите <y>, чтобы ЗАВЕРШИТЬ <n>: ')
                s = s.replace(' ', '')
                if s != 'y' and s != 'n':
                    print()
                    print('Ошибка ввода! Введите только <y> или <n>.')
                else:
                    print()
                    print('Ошибка ввода! Повторите ввод.')
    print()
    print('*** Программа имитации подбрасывания монетки: ЗАВЕРШЕНА! ***')


if __name__ == '__main__':
    main()
