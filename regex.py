import re


str = 'google runoob taobao\RUnoob\taobao'

def regexp(str):
    pattern = r'\\'
    match = re.findall(pattern, str)
    print(match)


regexp(str)