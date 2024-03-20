#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def main():
    shozai = pd.read_csv('../dimension.csv')
    age = pd.read_csv('../Age.csv')
    density = pd.read_csv('../Density.csv')

    age = age.iloc[:,1:].add_prefix('Age')
    density = density.iloc[:,1:].add_prefix('Density')
    shozai.rename(columns={'shohan':'SHOZAI'},inplace=True)

    df = pd.concat([shozai,age,density],axis=1)
    df.to_csv('./unity.csv',encoding='shift-jis')

if __name__ == '__main__':
    main()