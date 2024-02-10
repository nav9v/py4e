while True:
    print ('input dalo to print')
    print ('if you put "#" in prefix it wont print and to stop write "done"')
    lol = input('> ')
    if lol[0] == '#' :
        continue
    if lol == 'done':
        break
    print(lol)
print ('loop khatam bhaau!!')    