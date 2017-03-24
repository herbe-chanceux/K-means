'''
Created on 2017-3-15

@author: libing
'''
def fun_dis (x,y,n):  
    return sum (map (lambda v1,v2:pow(abs(v1-v2),n), x,y))  
  
def distance (x,y):  
    #return fun_dis (x,y,2)  
    return fun_dis (x,y,1)  
      
  
def min_dis_center(center, node):  
    min_index = 0  
    min_dista = distance (center[0][1],node)  
    for i in range (1,len(center)):  
        tmp = distance (center[i][1],node)  
        if (tmp < min_dista):  
            min_dista = tmp  
            min_index = i  
    return min_index  
  
  
# input [[x1,y1,z1..],[x2,y2,z2..]..]  
# return   
def k_means (info,k=10):  
    center = [[1,info[i]] for i in range(k)]  
    result = [[i] for i in range(k)]  
    width  = len (info[0])  
    for i in range(k,len(info)):  
        min_center = min_dis_center (center,info[i])  
        for j in range(width):  
            center[min_center][1][j] = (center[min_center][1][j] * center[min_center][0] + info[i][j])/ (1.0+center[min_center][0])  
        center[min_center][0] += 1  
        result[min_center].append (i)  
    return result,center  
  
  
test_data = [[1,100,300,9],  
             [9,200,400,20],  
             [2,102,305,10],  
             [3,103,299,9],  
             [3,105,299,11],  
             [3,105,299,11],  
             [9,200,400,20],  
             [2,102,305,10],  
             [11,220,409,20]]  
  
  
data = k_means (test_data,2)  
print (data[0]) 
print (data[1])  