import numpy as np

arr = np.array(5)
arr.shape -> () # 0d (scalar 5)

arr1 = np,array([1,2,3])
arr1 -> array([1, 2, 3])
arr1.shape -> (3,) # 1d이기 때문

arr2 = np.array([arr1, arr1, arr1, arr1])
arr2 -> array([[1,2,3],
               [1,2,3],
               [1,2,3],
               [1,2,3]])
arr2.shape -> (4, 3)

arr3 = np.array([arr2, arr2])
arr3 -> array([[[1,2,3],
               [1,2,3],
               [1,2,3],
               [1,2,3]],
               
              [[1,2,3],
               [1,2,3],
               [1,2,3],
               [1,2,3]]])
arr3.shape -> (2, 4, 3)

arr = np.array([[1],[1],[1]]) # 2d
arr.shape -> (3,1) 
arr = np.array([[[1]]]) # 3d
arr.shape -> (1, 1, 1)

zeros = np.zeros([3,4])
zeros -> array([[0., 0., 0., 0.],
                [0., 0., 0., 0.],
                [0., 0., 0., 0.]])
zeros.shape -> (3,4)

ones = np.ones([3, 4])
ones -> array([[1., 1., 1., 1.],
               [1., 1., 1., 1.],
               [1., 1., 1., 1.]])
ones.shape -> (3, 4)
onesx5 = ones * 5
onesx5 -> array([[5., 5., 5., 5.],
                 [5., 5., 5., 5.],
                 [5., 5., 5., 5.]])

arr = np.arange(12).reshape(3,4)
arr -> array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])
arr[1][2] -> 6
arr[1,2] -> 6
arr[1:] -> array([[4, 5, 6, 7],
                  [8, 9, 10, 11]])
arr[:,1:] -> array([[1, 2, 3],
                    [5, 6, 7],
                    [9, 10, 11]])
arr[1:3, 2:4] -> array([[6, 7],
                        [10, 11]])

data = np.random.randn(3,4)
data -> 3행 4열 짜리의 난수 생성

data[data <=1.0] = 0.0 # broadcast 이거 중요
data * 3
data + np.array([1,1,1,1]) # 모든 row에 1씩 더해진다.