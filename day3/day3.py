# coding: utf-8
with open("info_day_3",'r', newline='\n') as f:
    claims = [i.replace('\n','') for i in f.readlines()]
    
f.close()

claims_list = []
for i in claims:
    claims_list.append({'id':i.split('@')[0].strip(),
    'left': int(i.split('@')[1].strip().split(',')[0]),
    'top':int(i.split('@')[1].strip().split(',')[1].split(':')[0]),
    'wide': int(
    i.split('@')[1].strip().split(',')[1].split(':')[1].strip().split('x')[0]
    ),
    'tall':int(i.split('@')[1].strip().split(',')[1].split(':')[1].strip().split('x')[1])})
    
import numpy as np

malla = np.zeros((1000,1000),dtype=np.int8)
for i in claims_list:
    for l in range(i['wide']):
        for t in range(i['tall']):
            malla[i['top']+t][i['left']+l]+=1
            

#first result:
print(sum((malla)>1))
np.sum((malla)>1)



#part 2:
malla = np.zeros((1000,1000),dtype=np.int8)

for i in claims_list:
    i['indices'] = []
    for l in range(i['wide']):
        for t in range(i['tall']):
            i['indices'].append((l,t))
            
        
claims_list[0]
claims_list[1]
def are_common(l1,l2):
    return sum([1 for i in l1 if i in l2])
are_common(claims_list[0],claims_list[1])
def are_common(l1,l2):
    return sum([1 for i in l1 if i in l2])>0
are_common(claims_list[0],claims_list[1])
claims_list2 = claims_list[:]
for l1 in claims_list:
    claims_list2.pop(0)
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            pass
        else:
            print(l1)
            
are_common(claims_list[0]['indices'],claims_list[1]['indices'])
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    claims_list2.pop(0)
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            pass
        else:
            print(l1)
    print(k, ' de ', len(claims_list))
    
            
def are_common(l1,l2):
    for i in l1:
        if i in l2:
            return True
        
for k,l1 in enumerate(claims_list):
    claims_list2.pop(0)
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            pass
        else:
            print(l1)
    print(k, ' de ', len(claims_list))
    
            
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    claims_list2.pop(0)
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            pass
        else:
            print(l1)
            
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    claims_list2.pop(0)
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            pass
        else:
            print(l1)
            
            
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            pass
        else:
            print(l1)
            
            
claims_list[0]['indices']
for i in claims_list:
    i['indices'] = []
    for l in range(i['wide']):
        for t in range(i['tall']):
            i['indices'].append((l+i['wide'],t+i['tall']))
            
            
        
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            pass
        else:
            print(l1)
            
            
for k,l1 in enumerate(claims_list):
    commons = 0
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
        else:
            pass
    if commons ==0:
        print(l1['id'])
        
            
            
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
        else:
            pass
    if commons ==0:
        print(l1['id'])
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
        else:
            pass
    if commons ==0:
        print(l1['id'])
        
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
        else:
            pass
    if commons ==0:
        print(l1['id'])
    print(k, ' de ', len(claims_list))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    print(k, ' de ', len(claims_list))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
        
l1['indices']
for i in claims_list:
    i['indices'] = []
    for l in range(i['wide']):
        for t in range(i['tall']):
            i['indices'].append((l+i['wide'],t+i['tall']))
            
            
        
claims_list[0]
for i in claims_list:
    i['indices'] = []
    for l in range(i['wide']):
        for t in range(i['tall']):
            i['indices'].append((l+i['left'],t+i['top']))
            
            
            
        
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
        
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    print(k, ' de ', len(claims_list))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
for k,l1 in enumerate(claims_list):
    commons = 0
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
        
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
        
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
for k,l1 in enumerate(claims_list):
    commons = 0
    claims_list2.pop(claims_list2.index(l1))
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    claims_list2.pop(claims_list2.index(l1))
    for l2 in claims_list2:
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    claims_list2.pop(claims_list2.index(l1))
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    claims_list2.pop(0)
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    try:
        claims_list2.pop(claims_list(index(l1)))
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
for k,l1 in enumerate(claims_list):
    commons = 0
    try:
        claims_list2.pop(claims_list(index(l1)))
    
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
for k,l1 in enumerate(claims_list):
    commons = 0
    try:
        claims_list2.pop(claims_list.index(l1))
    
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    try:
        claims_list2.pop(claims_list2.index(l1))
    
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
for k,l1 in enumerate(claims_list):
    commons = 0
    try:
        claims_list2.pop(claims_list2.index(l1))
    except:
        pass
    
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
    if k%100 ==0:
        print(k, ' de ', len(claims_list))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    try:
        claims_list2.pop(claims_list2.index(l1))
    except:
        pass
    
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
        
    print(k, ' de ', len(claims_list), len(claims_list2))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    try:
        claims_list2.pop(claims_list2.index(l1))
    except:
        pass
    
    for ii,l2 in enumerate(claims_list2):
        if are_common(l1['indices'],l2['indices']):
            commons+=1
            claims_list2.pop(ii)
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
        break
        
    print(k, ' de ', len(claims_list), len(claims_list2))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    
    for ii,l2 in enumerate(claims_list2):
        if l1['id']!= l2['id'] and are_common(l1['indices'],l2['indices']):
            commons+=1
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
        break
        
    print(k, ' de ', len(claims_list), len(claims_list2))
    
for i in claims_list:
    i['indices'] = []
    for l in range(i['wide']):
        for t in range(i['tall']):
            i['indices'].append((l+i['left'],t+i['top']))
    i['indices'] = sorted(i['indices'],key = lambda x: x[0])
    
            
            
        
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    
    for ii,l2 in enumerate(claims_list2):
        if l1['id']!= l2['id'] and are_common(l1['indices'],l2['indices']):
            commons+=1
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
        break
        
    print(k, ' de ', len(claims_list), len(claims_list2))
    
claims_list2 = claims_list[:]
for k,l1 in enumerate(claims_list):
    commons = 0
    if l1['id'] in descartados:
        break
    
    for ii,l2 in enumerate(claims_list2):
        if l1['id']!= l2['id'] and are_common(l1['indices'],l2['indices']):
            commons+=1
            descartados.append(l2['id'])
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
        break
        
    print(k, ' de ', len(claims_list), len(claims_list2))
    
descartados = []
for k,l1 in enumerate(claims_list):
    commons = 0
    if l1['id'] in descartados:
        break
    
    for ii,l2 in enumerate(claims_list2):
        if l1['id']!= l2['id'] and are_common(l1['indices'],l2['indices']):
            commons+=1
            descartados.append(l2['id'])
            break
        else:
            pass
    if commons ==0:
        print(l1['id'])
        break
        
    print(k, ' de ', len(claims_list), len(claims_list2))
    
for k,l1 in enumerate(claims_list):
    commons = 0
    if l1['id'] not in descartados:
    
      for ii,l2 in enumerate(claims_list2):
        if l1['id']!= l2['id'] and are_common(l1['indices'],l2['indices']):
            commons+=1
            descartados.append(l2['id'])
            break
        else:
            pass
      if commons ==0:
        print(l1['id'])
        break
        
      print(k, ' de ', len(claims_list), len(claims_list2))
    
claims_list2 = claims_list[:]
descartados = []
for k,l1 in enumerate(claims_list):
    commons = 0
    if l1['id'] not in descartados:
    
      for ii,l2 in enumerate(claims_list2):
        if l1['id']!= l2['id'] and are_common(l1['indices'],l2['indices']):
            commons+=1
            descartados.append(l2['id'])
            break
        else:
            pass
      if commons ==0:
        print(l1['id'])
        break
        
      print(k, ' de ', len(claims_list), len(claims_list2))
    
