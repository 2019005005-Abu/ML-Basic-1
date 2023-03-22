###NumPy-1
import numpy as np;
NumPy_array=np.array([[1,2,3],[4,5,6]]);
print(NumPy_array);

##Numpy-2

NP_1=np.array([[1,3],[4,5]]);
NP_2=np.array([[3,4],[5,7]]);
NP_3=np.array([[3],[4]]);

print(NP_1);
print(NP_2);

##Multiple by matrix-way using @

print(NP_1@NP_2);
'''
[1 3]  [4,5] =[18 25]
[3,4] @[5,7] =[37 51]

'''

print(NP_1 * NP_2);

'''
[1 3]  [4,5] =[3 12]
[3,4] *[5,7] =[20 35]
'''

print(np.dot(NP_1,NP_2));
print(np.multiply(NP_1,NP_2));

Sum1=NP_1+NP_2;
print(Sum1);

Sub1=NP_1-NP_2;
print(Sub1);

Sub2=np.subtract(NP_1,NP_2);
print(Sub2);

ElementSubmission=np.sum(NP_1);
print(ElementSubmission);

Broad_Num=NP_1+3;
print(Broad_Num);
print(NP_1+NP_3);

##Divide
Divide=np.divide([12,14,16],5);
print(Divide);
D1=np.floor_divide([12,14,16],5);
print(D1);

sq=np.math.sqrt(10);
print(sq)




