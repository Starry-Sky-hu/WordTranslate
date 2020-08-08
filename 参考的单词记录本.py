import json
import os

print("欢迎使用本单词记录软件！")
path = 'C:\\Users\\80656\\Desktop\\dictionary\\WORDS.txt'
while True:
    modea = input("请输入模式：1.查询单词 2.新添单词 3.修改单词 4.删除单词 5.退出:")
    data = {}
    with open(path, "r") as file:
        data = json.load(file)
    if(modea == "1"):
        word = input("请输入单词或单词对应的意思")
        if word in data:
            input(word + "对应" + data[word])
            os.system("cls")
        else:
            input("您还没记录呢！")
            os.system("cls")

    elif(modea == "2"):
        print("@@@@@必须要让单词的意思只有一种，否则查找不到！@@@@@")
        dataa = input("请输入你要记录的单词或单词的意思")
        datab = input("请输入你要记录的单词的意思或单词(与上个相反)")
        if dataa not in data:
            if datab not in data:
                data[dataa] = datab
                data[datab] = dataa
                with open(path, 'w') as file:
                    json.dump(data, file)
                ##下面是多余，但我只是怕程序出错。##
                with open(path, 'r') as file:
                    data = json.load(file)
                input("记录成功！")
                os.system("cls")
            else:
                input("已经记录过了！")
                os.system("cls")
        else:
            input("已经记录过了！")
            os.system("cls")
    elif(modea == "3"):
        print("@@@@@必须要让单词的意思只有一种，否则查找不到！@@@@@")
        dataa = input("请输入你要修改的单词或单词的意思")
        datab = input("请输入你要修改的单词的意思或单词(与上个相反)")
        if dataa in data:
            data[dataa] = datab
            data[datab] = dataa
            with open(path,'w') as file:
                json.dump(data,file)
                ##下面是多余，但我只是怕程序出错。##
            with open(path, "r") as file:
                data = json.load(file)
            input("记录成功！")
            os.system("cls")
        else:
            print("你没有记录哦！")
    elif(modea == "4"):
        dataa = input("请输入你要删除的单词或单词的意思")
        if dataa in data:
            del data[data[dataa]]
            del data[dataa]
            with open(path, 'w') as file:
                json.dump(data,file)
            with open(path, "r") as file:
                data = json.load(file)
            input("删除成功！")
            os.system("cls")
        else:
            input("你还没有记录！")
            os.system("cls")
    elif(modea == "5"):
        break
    else:
        print("输错啦！！")