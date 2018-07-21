def subset(a):
    res=[]
    n=len(a)

    ###### 循环子集个数1~2^n ######
    for i in range(0,1<<n):
        temp=[]

        ###### 循环元素，判断该元素对应的二进制数的位置是否为1 ######
        for j in range(0,n):

            ###### i>>j 表示将i转换为二进制数，从右向左取第j+1个数 #####
            ###### & 表示位运算中的"与"，1 & 1 =1   1 & 0 =0  0 & 0 =0 #####
            if (i>>j) & 1:

                ###### 元素压入列表里 #####
                temp.append(a[j])

        ###### 中间结果存储在列表里 #####
        res.append(temp)
    return res

if __name__ == '__main__':
    a=[1,2,3,4]
    res=subset(a)
    print(res)
