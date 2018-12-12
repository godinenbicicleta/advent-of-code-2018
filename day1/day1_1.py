from freqs import freqs
start = 0
f_list = [0]
loop = 0
seguir = True

example1 = [1,-1]
example2 = [3,3,4,-2,-4]
example3 = [7,7,-2,-7,-4]

for ex in [example1, example2, example3, freqs]:
    start = 0
    f_list = [0]
    loop = 0
    seguir = True

    while seguir:
        for n,i in enumerate(ex):
            start += i
            if start not in f_list:
                f_list.append(start)
            else:
                print('first repeated frequency is: ', start, 
                f_list.index(start))
                seguir = False
                break
        loop += 1
        print('loop: ',loop,len(f_list), len(set(f_list)),
        len(f_list)== len(set(f_list)), start )



"""
start = 0
f_list = [0]
loop = 0
seguir = True


while seguir:
    for n,i in enumerate(frequency_changes):
        start += i
        if start not in f_list:
            f_list.append(start)
        else:
            print('first repeated frequency is: ', start, 
            f_list.index(start),f_list)
            seguir = False
    loop += 1
    print('loop: ',loop,len(f_list), len(set(f_list)),
    len(f_list)== len(set(f_list)), start )

"""


"""
example1 = [1,-1]
example2 = [3,3,4,-2,4]
example3 = [7,7,-2,-7,-4]

for ex in [example1, example2, example3]:
    start = 0
    f_list = [0]
    for i in ex:
        start += i
        if start not in f_list:
            f_list.append(start)
        else:
            print('first repeated frequency is: ', start, f_list.index(start))
            break

"""
