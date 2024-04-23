import numpy as np
import matplotlib.pyplot as plt

# 활성화함수 -> sigmoid 함수화
def actf(x):
    return 1.0/(1.0+np.exp(-x))

# sigmoid 미분한 것
def actf_prime(x):
    return x*(1.0-x)

# x에 대해 이진화(binary)를 수행
# 배열 x의 모든 요소를 순회하면서 0.5 이상인 값을 1로 변경
def actbin(x):
    x[x>=0.5] = 1
    x[x<0.5] = 0
    return x

#-----------------------3layers의 경우-----------------------------
inputs, hiddens, outputs = 2, 2, 1
learning_rate = 0.5

X = np.array([[0,0],[0,1],[1,0],[1,1]]) # input
T = np.array([[0],[1],[1],[0]]) # Truth

# np.random.randn(nxm) -> 표준 정규 분포에서 난수를 (nxm)개 생성 후 -1
# 가중치를 초기화할때 사용 
W1 = 2*np.random.randn(inputs, hiddens) - 1.0
W2 = 2*np.random.randn(hiddens, outputs) - 1.0
b1 = np.zeros(hiddens)
b2 = np.zeros(outputs)

#print(W1, W2, b1, b2)

def predict(X, W1, W2, b1, b2):
    layer0 = X
    z1 = np.dot(layer0, W1) + b1 # z1 = ndarray
    layer1 = actf(z1)
    z2 = np.dot(layer1, W2) + b2
    layer2 = actf(z2)
    return layer0, layer1, layer2

def fit(X, W1, W2, b1, b2 ,T, it_max=6000):
    out = list()
    for it in range(it_max):
        layer0, layer1, layer2 = predict(X, W1, W2, b1, b2)
        layer2_error = layer2 - T

        out.append((layer2_error**2).mean())
        
        # 오류를 은닉층으로 역전파하기 위해, 출력층의 각 뉴런에서 은닉층의 각 뉴런으로 가중치를 적용해야 하지만,
        # 각 출력 뉴런의 오류 기울기를 각 은닉층 뉴런에 적절히 할당하기 위해서는 W2의 구조를 전치해야 합니다. 
        # 즉, 원래 가중치가 은닉층의 뉴런에서 출력층의 뉴런으로 가는 방향이었다면, 이제는 그 반대 방향으로 오류를 전파해야 하므로 전치가 필요합니다.
        layer2_delta = layer2_error * actf_prime(layer2) # layer2_delta는 출력층(최종 계층)에서 계산된 오차의 기울기
        layer1_error = np.dot(layer2_delta, W2.T) # layer2_delta 와 W2 전치를 내적
        layer1_delta = layer1_error * actf_prime(layer1)
        
        #layer1_error 에서 np.dot 함수는 출력층의 오류 기울기(layer2_delta)와 가중치 행렬 W2의 전치를 내적하여, 
        #그 결과로 은닉층에서의 오류를 계산. 
        #이는 은닉층의 각 뉴런에 대한 오류의 기여도를 계산하여, 그 다음 단계에서 은닉층의 가중치를 조정하는 데 사용.

        W2 += -learning_rate * np.dot(layer1.T, layer2_delta)/4.0
        W1 += -learning_rate * np.dot(layer0.T, layer1_delta)/4.0
        b2 += -learning_rate * np.sum(layer2_delta, axis=0)/4.0
        b1 += -learning_rate * np.sum(layer1_delta, axis=0)/4.0

        return W1, W2, b1, b2, out

W1, W2, b1, b2, out = fit(X, W1, W2, b1, b2, T, 10000)
_,_, layer2 = predict(X, W1, W2, b1, b2)

print(actbin(layer2))

npout = np.array(out)
plt.figure(figsize=(6,3))
plt.plot(npout)
plt.show()


#------------------------4lyaer의 경우-----------------------
inputs, hiddens1, hiddens2, outputs = 2, 2, 2, 1
learning_rate = 0.5

X = np.array([[0,0],[0,1],[1,0],[1,1]]) # input
T = np.array([[0],[1],[1],[0]]) # Truth

W1 = 2*np.random.randn(inputs, hiddens1) - 1.0
W2 = 2*np.random.randn(hiddens1, hiddens2) - 1.0
W3 = 2*np.random.randn(hiddens2, outputs) - 1.0
b1 = np.zeros(hiddens1)
b2 = np.zeros(hiddens2)
b3 = np.zeros(outputs)

def predict_4layers(X, W1, W2, W3, b1, b2, b3):
    layer0 = X
    z1 = np.dot(layer0, W1) + b1 # z1 = ndarray
    layer1 = actf(z1)
    z2 = np.dot(layer1, W2) + b2
    layer2 = actf(z2)
    z3 = np.dot(layer2, W3) + b3
    layer3 = actf(z3)
    return layer0, layer1, layer2, layer3

def fit_4layers(X, W1, W2, W3, b1, b2, b3, T, it_max=6000):
    out = list()
    for it in range(it_max):
        layer0, layer1, layer2, layer3 = predict_4layers(X, W1, W2, W3, b1, b2, b3)
        layer3_error = layer3 - T # 출력값 - 신뢰값

        out.append((layer3_error**2).mean())

        # (오류) 해당계층 기울기 = (해당 계층의) 에러폭 * 활성함수 미분값
        # 이전 계층의 에러폭 = (이후 계층 기울기, 이후 계층 가중치) 내적
        layer3_delta = layer3_error * actf_prime(layer3) # layer3_delta는 출력층(최종 계층)에서 계산된 오차의 기울기
        layer2_error = np.dot(layer3_delta, W3.T) # layer3_delta 와 W3 전치를 내적
        layer2_delta = layer2_error * actf_prime(layer2)
        layer1_error = np.dot(layer2_delta, W2.T) # layer2_delta 와 w2 전치를 내적
        layer1_delta = layer1_error * actf_prime(layer1)
        #layer0_error = np.dot(layer1_delta, W1.T)
        
        W3 += -learning_rate * np.dot(layer2.T, layer3_delta)/4.0
        W2 += -learning_rate * np.dot(layer1.T, layer2_delta)/4.0
        W1 += -learning_rate * np.dot(layer0.T, layer1_delta)/4.0
        b3 += -learning_rate * np.sum(layer3_delta, axis=0)/4.0
        b2 += -learning_rate * np.sum(layer2_delta, axis=0)/4.0
        b1 += -learning_rate * np.sum(layer1_delta, axis=0)/4.0

        return W1, W2, W3, b1, b2, b3, out


W1, W2, W3, b1, b2, b3, out = fit_4layers(X, W1, W2, W3, b1, b2, b3, T, 10000)
_,_,_, layer3 = predict_4layers(X, W1, W2, W3, b1, b2, b3)

print(actbin(layer3))

npout = np.array(out)
plt.figure(figsize=(6,3))
plt.plot(npout)
plt.show()