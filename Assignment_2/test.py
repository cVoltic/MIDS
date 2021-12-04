import numpy as np
np.random.seed(25)

ar = np.random.randn(1000)
ar = ar*100
ar = ar.astype('int8')
ar = ar.reshape((200,5))


# print(ar)
print(ar.min())
print(ar.max())
print(ar.mean())
print(ar[7][1])
print((ar > ar.mean()).sum())
print(((ar > -5) & (ar <= 20)).sum())

print(np.where(ar == ar.max()))
print(ar[199][4])