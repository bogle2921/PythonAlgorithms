import random as rand
file = open('values.txt', 'w+')
values = []

#creates a file with random digits
for i in range(20):
    i = rand.randint(0,50)
    file.write(str(i) + '\n')
file.close()

file = open('values.txt', 'r')
lines = file.readlines()
for line in lines:
    values.append(int(line))

file.close()

def merge(a,b):
    c = []
    ai = 0
    bi = 0
    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            c.append(a[ai])
            ai += 1
        else:
            c.append(b[bi])
            bi += 1
    if ai == len(a):
        c.extend(b[bi:])
    else:
        c.extend(a[ai:])
    return c

def mergeSort(a):
    if len(a) <= 1:
        return a
    mid = int(len(a)/2)
    l = mergeSort(a[:mid])
    r = mergeSort(a[mid:])

    return merge(l,r)

def quickSort(a):
    if len(a) <= 1:
        return a
    pivot = a.pop()
    g = []
    l = []

    for item in a:
        if item > pivot:
            g.append(item)
        else:
            l.append(item)
    return quickSort(l) + [pivot] + quickSort(g)

print(values)
print(quickSort(values))

file = open('list.txt', 'w+')
numbers = []
for i in range(30):
    file.write(str(i * 2) + '\n')

file.close()

file = open('list.txt', 'r')
lines = file.readlines()
for line in lines:
    numbers.append(int(line))
file.close()

def binarySearch(a, i):
    b = 0
    e = len(a) - 1

    while b <= e:
        m = b + (e - b) // 2
        mv = a[m]
        if mv == i:
            return m
        elif i < mv:
            e = m - 1
        else:
            b = m + 1
    return None

print(binarySearch(numbers, 12))