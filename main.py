def zadacha1():
    strana={"russia" : "moscow", "japan" : "tokyo", "china" : "peking", "france" : "paris", "sweden" : "stockholm"}
    x = input('Столицу какой страны вы хотите вывести?')
    #a
    print(strana)
    #b
    print(strana[x])
    #c
    print(sorted(strana))

def zadacha2():
    points={ 1 : ['а','в','е','и','н','о','р','с','т'], 2 : ['д','к','л','м','п','у'], 3 : ['б','г','ё','ь','я'], 4 : ['й','ы'], 5 : ['ж','з','х','ц','ч'], 8 : ['ш','э','ю',], 10 : ['ф','щ','ъ',]}
    s=list(input("Введите слово"))
    summa=0
    for i in s:
        for j in points:
            if i in points[j]:
                summa=summa+j
    print(summa)

def zadacha3():
    students={
        'A' : ['eng','rus','spa'],
        'B' : ['eng','rus','chi'],
        'C' : ['rus','eng'],
        'D' : ['chi','rus'],
        'E' : ['rus'],
        'F' : ['eng', 'spa'],
        'J' : ['kaz', 'rus'],
        'H' : ['eng','ita'],
        'I' : ['eng','fra']
    }
    d = []
    c = 0
    k=[]
    for i in students:
        for i in students[i]:
            if i not in d:
                d.append(i)
                c+=1
    for i in students:
        if 'chi' in students[i]:
            k.append(i)
        else:
            continue
    print(d)
    print(c)
    print(sorted(d))
    print(*k)

zadacha1()
