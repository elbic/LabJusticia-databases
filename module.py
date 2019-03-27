# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pandas

import io, json

df = pandas.read_csv(open('module.csv','rb'))

data = []
for index, row in df.iterrows():
    jsonData = {}
    years = row['years']
    years = years.split(",")
    jsonData['years'] = years
    jsonData['pack'] = row['pack']
    jsonData['module'] = row['module']
    jsonData['submodule'] = row['submodule']
    jsonData['file'] = row['file']
    jsonData['name'] = row['name']
    jsonData['desc'] = row['desc']
    data.append(jsonData)

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


with io.open('conf/databases.json', 'w', encoding='utf8') as outfile:
    resources = {"resources":data}
    str_ = json.dumps(resources,
                      indent=4, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('conf/databases.json') as data_file:
    data_loaded = json.load(data_file)

print(data == data_loaded)
