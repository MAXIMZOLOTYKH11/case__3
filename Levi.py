from turtle import *

def levi(l, n):
    if n == 0:
        down()
        forward(l)
    else:
        a = left(45), levi(l/(2**0.5), n-1), right(90), levi(l/(2**0.5), n-1), left(45)
        return a


def main():
    l = int(input())
    n = int(input('Глубина рекурсии:'))
    levi(l, n)
    speed(100)
    mainloop()


if __name__ == '__main__':
    main()