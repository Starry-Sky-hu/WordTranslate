import json
import os

print('\nWelcome To Wordbook! :)\n')
WordName = input("Please Enter Name of Wordbook:")
path = 'C:\\Users\\80656\\Desktop\\dictionary\\' + WordName
with open(path, 'w') as f:
    f.write(json.dumps({'word': '单词'}, ensure_ascii=False))
with open(path, 'r') as f:
    recorded = json.loads(f.read())
    print(recorded)
while True:
    mode = input('Enter mode:\t0.Print Record\t1.add word\t2.delete word\t3.Clean the Screen\t4.Exit:\n')
    if mode == '0':
        with open(path, 'r') as f:
            recorded = json.loads(f.read())
        for key, value in recorded.items():
            print(key + ':' + value + '\t')
        print('\n')
    elif mode == '1':
        word = input('Please Enter a New Word: ')
        Chinese = input('Please Enter Chinese of the Word: ')
        recorded[word] = Chinese
        with open(path, 'w') as f:
            f.write(json.dumps(recorded, ensure_ascii=False))
        with open(path, 'r') as f:
            recorded = json.loads(f.read())
            print(recorded)
        print('\nSaved Successfully! :)\n')
    elif mode == '2':
        word = input('Please Enter Word that needs to delete: ')
        with open(path, 'r') as f:
            recorded = json.loads(f.read())
        if word in recorded: 
            del recorded[word]
        with open(path, 'w') as f:
            f.write(json.dumps(recorded, ensure_ascii=False))
        with open(path, 'r') as f:
            recorded = json.loads(f.read())
            print(recorded)
        if word not in recorded:
            print('\ndeleted Successfully! :)\n')
        else:
            print('\ndeleted Failedly! :(\n')
    elif mode == '3':
        os.system("cls")
    elif mode == '4':
        break
    else:
        print('\nEnter False\n')
