#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d_one = {'name': 'Ivan', 'last_name': 'Lysenko'}
d_two = {'name': 'Igor', 'last_name': 'Padalka'}

for (k1, k2), (v1, v2) in zip(d_one.items(), d_two.items()):
    print(k1, ':', k2, v1, ':', v2)
