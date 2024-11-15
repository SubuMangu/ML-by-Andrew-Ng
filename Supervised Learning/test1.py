import numpy as np

x_train = np.array([[1,3],[5,8]])
y_train = np.array([300.0, 500.0])

def linear_regressor(x:np.ndarray, y:np.ndarray):
    m=np.shape(x)[0]
    if not isinstance(x[0],np.ndarray):
        A=np.dot(x,x)
        B=np.sum(x)
        C=np.dot(x,y)
        D=np.sum(y)
        
        b=(D-(B*C/A))/(m-(B**2/A))
        w=(C-B*b)/A
        return w,b
    else:
        n=np.shape(x)[1]
        A=np.empty((n+1,n+1))
        B=np.empty((n+1,))
        for i in range(0,n):
            for j in range(0,n):
                A[i][j]=np.dot(x[:,i],x[:,j])
            A[i][n]=np.sum(x[:,i])
        for i in range(0,n):
            A[n][i]=np.sum(x[:,i])
        A[n][n]=m
        for i in range(0,n):
            B[i]=np.dot(y,x[:,i])
        B[n]=np.sum(y)
        w=np.dot(np.linalg.inv(A),B)
        return w
                
linear_regressor(x_train,y_train)