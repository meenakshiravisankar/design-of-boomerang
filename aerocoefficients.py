import numpy as np

def doLoadLDCoefficients() :
    data = np.genfromtxt('Cl.csv', delimiter=',', dtype='float64')
    Cl = data[:,1]
    alpha_Cl = data[:,2]

    data = np.genfromtxt('Cd.csv', delimiter=',', dtype='float64')
    Cd = data[:,1]
    alpha_Cd = data[:,2]

    return Cl, alpha_Cl, Cd, alpha_Cd

def doLoadMomentCoefficients() :
    data = np.genfromtxt('Cm.csv', delimiter=',', dtype='float64')
    Cm = data[:,1]
    alpha_Cm = data[:,2]

    return Cm, alpha_Cm
