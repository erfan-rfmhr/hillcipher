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


