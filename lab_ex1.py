import numpy as np

a,b = 2,3
my_arr = np.zeros(shape=(a,b))
 
print (my_arr)

for(i,j), x in np.ndenumerate (my_arr):
    my_arr[i,j] = float(input(f'Input [{i}],{[j]}:'))
    print (i,j,x,sep=';')

print(my_arr)



my_arrr = np.zeros(shape=(a,b))
 
print (my_arrr)

for(o,p), x in np.ndenumerate (my_arrr):
    my_arrr[o,p] = float(input(f'Input [{o}],{[p]}:'))
    print (o,p,x,sep=';')

print(my_arrr)




my_arrr1 = np.zeros(shape=(a,b))
 
print (my_arrr1)

for(o,p), x in np.ndenumerate (my_arrr1):
    my_arrr1[o,p] = np.maximum(my_arr[o,p], my_arrr[o,p])
    print (o,p,x,sep=';')

print(my_arrr1)





