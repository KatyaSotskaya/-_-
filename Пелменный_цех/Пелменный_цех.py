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