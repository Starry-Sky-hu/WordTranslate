if(False):
    d = {'a': 'aaa', 'b': 'bbb'}
    s = str(d)
    path = 'C:\\Users\\80656\\Desktop\\dictionary\\dict.txt'
    with open(path, 'w') as f:
        f.writelines(s)
    with open(path, 'r') as f:
        s = f.read()
    s = eval(s)
    print(type(s))
    print(s)

    data = {"姓名":"胡勇"}
    data[姓名]
    print(data)

data = {'from': 'en', 'to': 'zh', 'trans_result': [{'src': 'word', 'dst': '单词'}]}
d = data['trans_result'][0]["dst"]
print(d)

