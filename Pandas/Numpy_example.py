import numpy as np

def myFun(a, b, c):
    print(a+b+c)
    return a+b+c

def myFun1():
    print("Hello world")
    #List
    L = [1, 2.0, 'str', True]
    #print the type of item inside of list
    for i in range(0, len(L)):
        print('value: {}, type: {}'.format(L[i],type(L[i])))

def myFun2():
    ar = np.array([2, 4.0, 5, 8],dtype=np.float)
    ar1 = np.array([2, 4.0, 5, 8],dtype=np.uint8)
    print(ar)
    print(ar1)

def myFun3():
    ar_zeros = np.zeros(10, dtype=float)
    ar_ones = np.ones(10)
    ar_full = np.full((5,5),5.5)

    ar_arange = np.arange(0,10,2,dtype=float)
    ar_linspace = np.linspace(0,10,5,endpoint=True)
    ar_random = np.random.random((3,3))
    ar_normal_random = np.random.normal(0,1,(3,3))
    ar_random_int = np.random.randint(0,20,(3,3))
    ar_eye = np.eye(5)
    ar_empty = np.empty(3)

    print(ar_eye)
    print(ar_empty)

    print(ar_arange)
    print(ar_linspace)
    print(ar_random)
    print(ar_normal_random)
    print(ar_random_int)

#properties of numpy arrays 
def myFun4():
    ''' Types of variables
    uint8 (0,256) or int8 (-128 to 127)
    int16 - -32768 or 32768 uint16 0 - ~65000
    int32
    int64
    float16 5 bits exponent and 10bits mantisa
    float32
    float64
    complex_   4 + 10j, 10 - 5j
    complex64
    complex128
    '''
    x1 = np.random.randint(10,size=6)
    x2 = np.random.randint(10,size=(3,4))
    x3 = np.random.randint(10,size=(3,4,5))

    print(x1)
    print(x1[2])
    print(x1[-1]) #last item in array
    print(x1[-2]) #befor last one

    print("......................")
    print(x2)
    print(x2[2,2])
    print(x2[-1,-1])
    x2[-1,-1] = 100
    print(x2)
    '''
    print('........')
    print(x1)
    print('........')
    print(x2)
    print('........')
    print(x3)

    print("x ndim: {}".format(x2.ndim))
    print("x shape: {}".format(x2.shape))
    print("x size: {}".format(x2.size))
    print("bytes per item: {}".format(x3.itemsize))
    print("bytes per array: {}".format(x3.nbytes))
    print("type of array: {}".format(x3.dtype))
    '''

def myFun5():

    x = np.arange(10)
    print(x)
    print(x[0:5]) #first five elements from 0 to 5 (it gives end with 4)
    print(x[2:7])
    print(x[6:-1])
    print(x[1::3])
    x2 = np.random.randint(10,size=(5,5))
    print(x2)
    print(x2[1:3,2:-1])

    str = 'certain string 2525'
    print(str)
    print(str[:])
    str = 'K'
    print(str)

    #reshaping 
    print(">>>>>>>>>reshape of arrays>>>>>>>>>>>>")
    x = np.array([1, 2, 3])
    print(x)
    y = x.reshape((3,1))
    print(y)
    print(x[np.newaxis,:])

    x1 = np.array([3, 2, 1])

    c = np.concatenate([x,x1])
    print(c)

def myFun6():
    x = np.arange(4)
    print(x)
    print(x + 5)   #np.add
    print(x - 5)   #np.subtract
    print(x * 3)   #np.multiply
    print(x / 2)   #np.divide
    print(x // 2)  #np.floor_divide
    print(-x) #inversion of items np.negative
    print(x ** 2) #power by 2
    print(x % 3) # Modulus or remainder

    print('----------------')
    y = np.negative(x)
    print(y)
    print(np.abs(y)) #np.absolute

    print('------- trigonometric functions -----------')
    theta = np.linspace(0,np.pi,3)
    print(np.sin(theta))
    print(np.cos(theta))
    print(np.tan(theta))

    x = np.array([-1, 0, 1])
    print(np.arcsin(x))
    print(np.arccos(x))
    print(np.arctan(x))

    print('---------logoritmic values-------')
    x = np.array([0, 0.001, 0.01, 0.1, 1])
    print(np.expm1(x))
    print(np.log1p(x))

    print('----------sum min max value---------')
    M = np.random.randint(10,size=(1,5))
    print(M)
    print(np.sum(M))
    print('max value: {} and index: {}'.format(np.max(M),np.argmax(M)))
    print('min value: {} and index: {}'.format(np.min(M),np.argmin(M)))
    print(np.mean(M))
    print(np.std(M))
    print(np.var(M))
    print(np.median(M))




myFun6()
