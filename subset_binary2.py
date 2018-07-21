def subset(a):
    res=[]
    n=len(a)

    ###### 循环子集个数2^n-1~1，因为是从最大到最小，所以倒序######
    for i in range((1<<n)-1,0,-1):
        temp=[]

        ###### 循环元素，判断该元素对应的二进制数的位置是否为1 ######
        for j in range(n-1,-1,-1):

            ###### i>>j 表示将i转换为二进制数，从右向左取第j+1个数 #####
            ###### & 表示位运算中的"与"，1 & 1 =1   1 & 0 =0  0 & 0 =0 #####
            if (i>>j) & 1:

                ###### 元素压入列表里 #####
                temp.append(a[j])

        ###### 中间结果存储在列表里 #####
        res.append(temp)
    return res

if __name__ == '__main__':
    
    a=[123,456,789]
    a.sort()

    res=subset(a)
    
    print(res)
