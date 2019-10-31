#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from glob import glob
import pandas as pd


raw_data_folder = 'data/'

files = glob(raw_data_folder+'*')

games = {0: dict()}
i = 0

for file in files:
    with open(file,'r') as f:
        contents = f.readlines()
        for line in contents:
            line = line.strip()
            if line == "":
                i += 1
                games[i] = dict()
                continue
            if line[0] == "%":
                continue
    
            if line[0] == "[":
                # data field
                field = line[1:-1] # strips square brackets
                field = field.split(" ", maxsplit=1)
                field_name = field[0]
                field_value = field[1][1:-1] # strips quotes
    
                games[i][field_name] = field_value


gamesdf = pd.DataFrame(games).dropna(axis=1,how='all').transpose()


# Sorting out the '#' signs which represent repeated data
for i in gamesdf.index[1:]:
    row = gamesdf.loc[i]
    
    row[row == '#'] = gamesdf.loc[i-1][row == '#']
    
gamesdf.to_csv('data/sorted_data.csv')