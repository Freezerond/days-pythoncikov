import hashlib
arraychik = open('input1.txt', 'r'). read()
file = open('output2.txt', 'w+')
for i in range (10000000000000000000000) :
    tonik = arraychik + str(i)
    answerik = hashlib.md5(tonik.encode('utf-8')).hexdigest()
    if answerik.startswith ('000000') :
        break
file.write(str(i))
file.close ()
