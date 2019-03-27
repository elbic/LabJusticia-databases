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
    if os.path.exists('databases/' + file_name):
        with open('databases/' + file_name, "r") as read_file:
            data = json.load(read_file)

        for element in data['columns']:
            if column == element['column']:
                element['short'] = short

        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str

        with io.open('databases/' + file_name, 'w', encoding='utf8') as outfile:
            str_ = json.dumps(data,
                              indent=4, sort_keys=False,
                              separators=(',', ': '), ensure_ascii=True)
            outfile.write(to_unicode(str_))
    else:
        print file_name
