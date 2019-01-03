# coding=utf-8

import json
data = {
    'number': 1,
    'name': 'yueban',
    'url': 'https://yueban.github.io',
}
jsonStr = json.dumps(data)
print('python original object:', repr(data))
print('json data:', jsonStr)

data2 = json.loads(jsonStr)
print(data2)
