#!/usr/bin/env python3
import csv


FILENAME='registros.csv'


with open(FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file)
    for i, row in enumerate(csv_reader):
        print(f"{i:3} {row[0]:31}{row[1]:4}{row[2]:40}{row[3]:9}{row[4]:20}{row[5]:6}{row[6]:4}")

print(f"===== {FILENAME} - {i} registros leídos")
