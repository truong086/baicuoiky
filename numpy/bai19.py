import numpy as np
#import numpy.random

# Cú pháp của hàm
#numpy.random.normal(loc=0.0, scale=1.0, size=None)
# loc = mean, scale = standard deviation

mu, sigma = 0, 0.1 # mean và standard deviation
s = np.random.normal(mu, sigma, size=5)
print(s)