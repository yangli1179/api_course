# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/12

E-mail:1179384105@qq.com

=================================


"""

import random


def random_ip():
    ip = "{}.{}.{}.{}".format(random.randint(0, 255), random.randint(0, 255),
                              random.randint(0, 255), random.randint(0, 255))
    return ip


if __name__ == '__main__':

    ip = random_ip()
    print(ip)


