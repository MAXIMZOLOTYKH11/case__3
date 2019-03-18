from turtle import *

def f(d, n):
    if n == 1:
        forward(d)
    else:
        f(d / 2, n - 1)
        left(120)
        f(d / 5, n - 1)
        right(180)
        f(d / 5, n - 1)
        left(120)
        f(d / 5, n - 1)
        right(180)
        f(d / 5, n - 1)
        left(120)
        f(d / 2, n - 1)


def main():
    d = int(input())
    n = int(input('Глубина рекурсии:'))
    speed(80)
    up()
    goto(-300, 0)
    down()
    f(d, n)
    right(120)
    f(d, n)
    right(120)
    f(d, n)
    right(180)
    f(d, n)
    left(120)
    f(d, n)
    left(120)
    f(d, n)
    mainloop()


if __name__ == '__main__':
    main()