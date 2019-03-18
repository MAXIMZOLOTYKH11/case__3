from turtle import *

def k(d,n):
    if n == 0:
        mainloop()
        return
    up()
    right(20)
    forward(d // 4)
    down()
    for _ in range(4):
        forward(d)
        right(90)
    return k(d*0.9,n-1)


def main():
    d = int(input('Длина стороны:'))
    n = int(input('Глубина рекурсии:'))
    k(d,n)


if __name__ == "__main__":
    main()