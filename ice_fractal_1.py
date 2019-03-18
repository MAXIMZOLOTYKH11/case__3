from turtle import *

def frag(d, n):
    if n == 1:
        forward(d)
    else:
        frag(d / 2, n - 1)
        left(90)
        frag(d / 5, n - 1)
        right(180)
        frag(d / 5, n - 1)
        left(90)
        frag(d / 2, n - 1)


def main():
    up()
    goto(-300, 0)
    down()
    d = int(input('Длина стороны:'))
    n = int(input('Глубина рекурсии:'))
    frag(d, n)
    mainloop()


if __name__ == '__main__':
    main()