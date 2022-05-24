#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = int(input('Введите стипендию: '))
    B = int(input('Введите расходы: '))
    s = B

    for i in range(10):
        B = (B*103) / 100
        s += B

    c = s - A*10
    print('Чтобы прожить учебный год, у родителей надо попросить ', c, ' р.')
