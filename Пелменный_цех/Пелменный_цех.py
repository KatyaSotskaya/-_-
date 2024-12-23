#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from os import read
import re
import math

def import_file_csv():
    Arr = []
    with open("../data.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            Arr.append(row[0])

    return Arr


arr = import_file_csv()

def import_file_csv_name_arr():
    Arr = []
    with open("../data.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            Arr.append(row[1])

    return Arr


name_arr = import_file_csv_name_arr()

def import_file_csv_name_arr():
    Arr = []
    with open("../data.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            Arr.append(row[1])

    return Arr


name_arr = import_file_csv_name_arr()


Qdaily = float(arr[0])  # суточная выработка готовой продукции Qсут
t = float(arr[1])  # продолжительность рабочей смены

# I. Технологическая линия изготовления пельменей
Rpa = float(arr[2])  # производительность пельменного автомата рпа

# II. Технологическая линия подготовки теста.
at = float(arr[3])  # массовая доля теста в готовой продукции   ат %
Rtm = float(arr[4])  # производительность тестомесильной машины   ртм

# III. Технологическая линия подготовки фарша.
Rk = float(arr[5])  # производительность куттера рк

def print_name_arr(arr, name_arr):
    n = len(arr)
    for index in range(n):
        print(arr[index] + "  " + name_arr[index])
    return 1


print_name_arr(arr, name_arr)

# I. Технологическая линия изготовления пельменей
def dumpling_machines(Qdaily, t, Rpa):
    Ptlp = Qdaily / (2 * t)
    N = math.ceil(Ptlp / Rpa)
    return N

# II. Технологическая линия подготовки теста
def dough_kneading_machines(Qdaily, t, at, Rtm):
    Ptlp = Qdaily / (2 * t)
    Ptlt = Ptlp * at / 100
    N = math.ceil(Ptlt / Rtm)
    return N

# III. Технологическая линия подготовки фарша
def cutter_machines(Qdaily, t, at, Rk):
    Ptlp = Qdaily / (2 * t)
    Ptlf = ((100 - at) * Ptlp) / 100
    N = math.ceil(Ptlf / Rk)
    return N