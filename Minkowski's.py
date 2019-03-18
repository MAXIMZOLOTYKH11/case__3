from turtle import *

def g(l, n):
    if n == 0:
        down()
        forward(l)
    else:
        a = g(l/4, n-1), left(90), g(l/4, n-1), right(90),\
            g(l/4, n-1), right(90), g(l/4, n-1),\
            g(l/4, n-1), left(90), g(l/4, n-1), left(90),\
            g(l/4, n-1), right(90), g(l/4, n-1)
        return a


def main():
    l = int(input())
    n = int(input('Глубина рекурсии:'))
    g(l, n)
    mainloop()


if __name__ == '__main__':
    main()