import numpy as np
from mathmatrix import Matrix

n = -1
rows = -1

def encrypt(text, key=[[17,17,5],[21,18,21],[2,2,19]]):
  global n, rows
  text = "".join(text.split(" "))
  try:
    key = np.array(key)
    n = len(key)
    rows = len(text) // n
    arr = [ord(i)-65 for i in text]
    matrix = np.array(arr).reshape(rows,n)

    enc = ""
    for i in range(rows):
      enc += ''.join([chr(i+65) for i in np.dot(matrix[i], key)%26])
    return enc
  except:
    raise Exception(f"Either the string must contain {n} multiples alphabets or the key matrix shall be 'MxM' where M is divisor of {n}")

def decrypt(enc, key=[[17,17,5],[21,18,21],[2,2,19]]):
  try:
    det = np.linalg.det(key)%26
    adj = Matrix(n,n,key).adjoint()
    adj = np.array([[adj[i][j] for j in range(n)] for i in range(n)])%26
    inv = 1
    while True:
      if (inv*det)%26 == 1:
        break
      inv += 1
    decKey = (inv*adj)%26
    em = np.array([ord(i)-65 for i in enc]).reshape(rows, n)
    dec = ""
    for i in range(rows):
      dec += ''.join([chr(i+65) for i in np.dot(em[i], decKey)%26])
    return dec
  except:
    return Exception(f"Either the string must contain {n} multiples alphabets or the key matrix shall be 'MxM' where M is divisor of {n}")


