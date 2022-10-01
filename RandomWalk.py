# Random Walk in 2D
import random
x,  y=0, 0
X, Y=[], []
for i in range(1000):
    dx, dy=random.choice([(1,0),(-1,0),(0,1),(0,-1)])
    X = x + dx
    Y= y + dy
    X.append (x)
    Y.append (y)

import matplotlib.pyplot as plt
plt.plot(X, Y)
plt.show()    