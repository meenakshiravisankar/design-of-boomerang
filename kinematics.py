import numpy as np
from numpy.linalg import inv

tan = np.tan
cos = np.cos
sin = np.sin
pi = np.pi
taninv = np.arctan2 # first arg/ second arg 's inverse'
transpose = np.transpose

# change in euler angles of body frame
def doEulerRatesBody(p,q,r,phi, theta, psi) :
    psi_d = q*sin(phi)/cos(theta)+r*cos(phi)/cos(theta)
    theta_d = q*cos(phi) - r*sin(phi)
    phi_d = p+ q*sin(phi)*tan(theta)+r*cos(phi)*tan(theta)
    return phi_d, theta_d, psi_d


# f6 - Relative air velocity of blade in blade frame
def doRelativeAirVelBlade(v_j_vec, Tj) :
    w_vec = []
    for i in v_j_vec :
        w_vec.append(np.matmul(-Tj,i))
    return np.array(w_vec)

# f5 - Velocity of blade in body frame
def doVelBlade(u_vec, omega_vec, r_j_ac) :
    v_vec = []
    for i in r_j_ac :
        v_vec.append(u_vec + np.cross(omega_vec,i))
    return np.array(v_vec)

# f7 - Calculation of alpha
def doAlpha(w_vec) :
    return [taninv(i[2],i[0]) for i in w_vec ]
