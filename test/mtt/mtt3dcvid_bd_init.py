import numpy as np
from pymrt.tracking.utils import GaussianComponent

# Dimensionality
n = 3

# 12 targets, 2D Constant Velocity Model
n_targets = 12
x_init = np.zeros((n_targets, 7))
x_init[ 0, :] = [   0,    0,    0,    0, -10, -10, 0]
x_init[ 1, :] = [ 400, -600,  300,  -10,   5,  -5, 1]
x_init[ 2, :] = [-800, -200, -300,   20,  -5,   5, 2]
x_init[ 3, :] = [ 400, -600,  300,   -7,  -4,   4, 3]
x_init[ 4, :] = [ 400, -600,  300, -2.5,  10,   7, 4]
x_init[ 5, :] = [   0,    0,    0,  7.5,  -5, 6.3, 5]
x_init[ 6, :] = [-800, -200, -300,   12,   7,  10, 6]
x_init[ 7, :] = [-200,  800,  200,   15, -10,   2, 7]
x_init[ 8, :] = [-800, -200, -300,    3,  15,  15, 8]
x_init[ 9, :] = [-200,  800,  200,   -3, -15,  -8, 9]
x_init[10, :] = [   0,    0,    0,  -20, -15,  -9, 10]
x_init[11, :] = [-200,  800,  200,   15,  -5, 2.3, 11]

# Total 100 steps
n_steps = 100
birth = np.zeros((n_targets, 1), np.int)
# #target      0  1  2   3   4   5   6   7   8   9  10  11
birth[:, 0] = [1, 1, 1, 20, 20, 20, 40, 40, 60, 60, 80, 80]

death = np.zeros((n_targets, 1), np.int)
death[:, :] = n_steps
death[0, 0] = 70
death[2, 0] = 70

# STD of CV disturbance on state updates
w_cov_std = 1
# STD of CV disturbance on measurements
r_cov_std = 5
# Lambda parameter of clutter process - on average, 10 false-alarms per
# observation
poisson_lambda = 10

# Birth probability
model_birth = [
    GaussianComponent(n=7,
                      mean=np.array([0., 0., 0., 0., 0., 0., 0.]).T,
                      cov=np.eye(7)*100,
                      weight=0.03),
    GaussianComponent(n=7,
                      mean=np.array([400., -600., 300., 0., 0., 0., 0.]).T,
                      cov=np.eye(7) * 100,
                      weight=0.03),
    GaussianComponent(n=7,
                      mean=np.array([-800., -200., -300., 0., 0., 0., 0.]).T,
                      cov=np.eye(7) * 100,
                      weight=0.03),
    GaussianComponent(n=7,
                      mean=np.array([-200., 800., 200., 0., 0., 0., 0.]).T,
                      cov=np.eye(7) * 100,
                      weight=0.03),
]
