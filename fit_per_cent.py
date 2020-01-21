import numpy as np
from scipy.interpolate import RegularGridInterpolator
import ndsplines
from scipy.optimize import basinhopping
from scipy.optimize import differential_evolution
from scipy.optimize import shgo
from iminuit import Minuit

dat1=np.loadtxt("./RHIC-200GeV-FILES/Pion/GRID_10BINS_2030_Pion.dat")
dat2=np.loadtxt("./RHIC-200GeV-FILES/Kaon/GRID_10BINS_2030_Kaon.dat")
dat3=np.loadtxt("./RHIC-200GeV-FILES/Proton/GRID_10BINS_2030_Proton.dat")

#dat4=np.loadtxt("./RHIC-200GeV-FILES/GRID_10BINS_1520.dat")
#dat5=np.loadtxt("./RHIC-200GeV-FILES/GRID_10BINS_2030.dat")

#datlist=[dat1,dat2,dat3,dat4,dat5]
datlist=[dat1,dat2,dat3]

for dat in datlist:
    dat.shape=(10,10,10,10,10,6)


p1=dat1[:,0,0,0,0,0]
p2=dat1[0,:,0,0,0,1]
p3=dat1[0,0,:,0,0,2]
p4=dat1[0,0,0,:,0,3]
p5=dat1[0,0,0,0,:,4]

interpfun1 = ndsplines.make_interp_spline((p1,p2,p3,p4,p5), dat1[:,:,:,:,:,-1])
interpfun2 = ndsplines.make_interp_spline((p1,p2,p3,p4,p5), dat2[:,:,:,:,:,-1])
interpfun3 = ndsplines.make_interp_spline((p1,p2,p3,p4,p5), dat3[:,:,:,:,:,-1])

#interpfun4 = ndsplines.make_interp_spline((p1,p2,p3,p4,p5), dat4[:,:,:,:,:,-1])
#interpfun5 = ndsplines.make_interp_spline((p1,p2,p3,p4,p5), dat5[:,:,:,:,:,-1])

def single(x):

   return interpfun1(np.array([x[0], x[1], x[2], x[3], x[4] ]))


def sumxhi(x):
    return ( interpfun1(np.array([x[0], x[1], x[2], x[3], x[4] ]))
            +interpfun2(np.array([x[0], x[1], x[2], x[3], x[4] ]))
            +interpfun3(np.array([x[0], x[1], x[2], x[3], x[4] ]))
 #           +interpfun4(np.array([x[3], x[5], x[6], x[7], x[8] ]))
 #           +interpfun5(np.array([x[4], x[5], x[6], x[7], x[8] ]) )                      
                       )[0]


print("Begin minimization.....\n\n")


OBJECT = Minuit.from_array_func( sumxhi, (20, 0.216, 0.051, 0.13690, 0.267), error=(0.1, 0.1, 0.1, 0.1, 0.1),  
                                 limit=  ( (10, 60), (0.08, 0.25), (0.005, 0.1), (0.130, 0.155), (0.2, 0.6) ),  
                                 errordef=0.5)

#m = Minuit.from_array_func(sumxhi, (50, 45, 45, 40, 41.0, 0.15, 0.03, 0.140, 0.40))

OBJECT.migrad()  # run optimiser
OBJECT.minos()  # run optimiser

#print("values=", OBJECT.values)  # {'x': 2,'y': 3,'z': 4}

matrix = OBJECT.matrix(correlation=True)
error = OBJECT.hesse()

print(matrix)
print(error)

print("\n chi2/NDF = ",sumxhi([OBJECT.values[0], OBJECT.values[1], OBJECT.values[2], OBJECT.values[3], OBJECT.values[4]])/58)
