# Importing necessary libraries
import numpy as np

# x = np.array([1,2,3,4,5])
# y = np.array([11,12,13,14,15])

# # Mean of x and y

# x_mean = np.mean(x)
# y_mean = np.mean(y)
# xy_mean = np.mean(x*y)

# #Covariance of x and y
# cov_x_y = xy_mean - (x_mean*y_mean)

# #variance of x
# var_x = np.var(x)

# #Calculating m in y=mx+c
# m = cov_x_y/var_x

# #c = y-mx
# c = y_mean - (m * x_mean)

# #value of predicted y
# y_pred = m*x + c

# #calculating mean squared error
# mse = np.mean(np.square(y_pred-y))

# print(f"X_mean = {x_mean}\nY_mean = {y_mean}\nxy_mean = {xy_mean}\nvar(x)={var_x}\nm={m}\nc={c}\ny={y}\nmse={mse}")


#Linear Regression with multiple inputs and singlee output

x = np.array([[1,25,3,50],[1,25,2,60],[1,28,1,80],[1,25,0.5,59]])
y = np.array([660,580,425,320])

x_t = np.transpose(x)

w = np.linalg.inv(x.T.dot(x)).dot(x.T).dot(y)

print(f"weights are {w}")
