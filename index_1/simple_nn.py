# 3x2 NN (populated random values)

inputs = [1.2, 5.1, 2.0] # (m1, m2, m3)
w1 = [0.2, 1.2, 1.6] # weights for n1 (from m1, m2, m3) → (w11, w21, w31)
w2 = [3.7, 1.0, 0.6] # weights for n2 (from m1, m2, m3) → (w12, w22, w32)
b1 = 1.2 # bias for n1
b2 = 0.3 # bias for n2

n1 = inputs[0] * w1[0] + inputs[1] * w1[1] + inputs[2] * w1[2] + b1
n2 = inputs[0] * w2[0] + inputs[1] * w2[1] + inputs[2] * w2[2] + b2

outputs = [n1, n2]

print(outputs) # calculated values for layer 2 (n1 & n2)
# [10.76, 11.04]