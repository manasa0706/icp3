import numpy as np

# Create a random vector of size 20 with float values between 1 and 20
array_1 = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
array_1 = array_1.reshape(4, 5)

# Replace the max value in each row with 0 (axis=1)
array_1[np.arange(4), array_1.argmax(axis=1)] = 0

print(array_1)
