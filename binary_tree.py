from turtle import *

def tree(h, y, n):
    if n == 0:
        return
    forward(h)
    right(y)
    tree(h // 2, y, n - 1)
    left(2*y)
    tree(h // 2, y, n - 1)
    right(y)
    backward(h)


def main():
    h = int(input())
    y = int(input())
    n = int(input('Глубина рекурсии:'))
    up()
    goto(0, -100)
    left(90)
    down()
    tree(h,y,n)
    mainloop()


if __name__ == '__main__':
    main()