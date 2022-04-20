for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i * (10**i - 1)//9)
    # print(sum([i*pow(10,p) for p in range(i)]))
'''    
1/9 = .1111111111
2/9 = .2222222222
3/9 = .3333333333
'''
