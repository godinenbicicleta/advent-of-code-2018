# coding: utf-8

#open file to read codes

with open('codes_day_2', 'r', newline='\n') as f:
    codigos = [i.strip() for i in f.readlines()]
    
f.close()


#count words that contain exactly 2 of the same letter at least once
def count2(word):
    original = len(word)
    for letter in set([i for i in word]):
        ocasiones = original - len(word.replace(letter, ''))
        if ocasiones == 2:
            return True
    
    return False



#count words that contain exactly 3 of the same letter at least once
def count3(word):
    original = len(word)
    for letter in set([i for i in word]):
        ocasiones = original - len(word.replace(letter, ''))
        if ocasiones == 3:
            return True
    
    return False


palabras_con_2 = len([i for i in codigos if count2(i)])
palabras_con_3 = len([i for i in codigos if count3(i)])


print(palabras_con_2* palabras_con_3)
