# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os.path
import simplejson as json
import io
from collections import namedtuple
import pandas

df = pandas.read_csv(open('rename.csv','rb'))

for index, row in df.iterrows():
    file_name = row["file_name"]
    column = row["column"]
    short = row["short"]
    type = row["type"]
    desc = row["desc"]
    dictionary = row["dictionary"]
    filter = row["filter"]

    if os.path.exists('databases/' + file_name):
        with open('databases/' + file_name, "r") as read_file:
            data = json.load(read_file)

        print (data['columns'])
        jsonData = {}
        jsonData['file_name'] = row['file_name']
        jsonData['column'] = row['column']
        jsonData['short'] = row['short']
        jsonData['type'] = row['type']
        jsonData['desc'] = row['desc']
        jsonData['dictionary'] = row['dictionary']
        filter = 0 if row['filter'] else 1
        jsonData['filter'] = filter


    else:
        print file_name
        data = []
        jsonData = {}
        jsonData['file_name'] = row['file_name']
        jsonData['column'] = row['column']
        jsonData['short'] = row['short']
        jsonData['type'] = row['type']
        jsonData['desc'] = row['desc']
        jsonData['dictionary'] = row['dictionary']
        filter = 0 if row['filter'] else 1
        jsonData['filter'] = filter

        data = {"columns": jsonData}

    if data:
        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str

        with io.open('databases/' + file_name, 'w', encoding='utf8') as outfile:
            str_ = json.dumps(data,
                              indent=4, sort_keys=False,
                              separators=(',', ': '), ensure_ascii=True)
            outfile.write(to_unicode(str_))
