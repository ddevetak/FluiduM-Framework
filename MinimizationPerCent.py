import numpy as np
from scipy.interpolate import RegularGridInterpolator
import ndsplines
from scipy.optimize import basinhopping
from scipy.optimize import differential_evolution
from scipy.optimize import shgo
from iminuit import Minuit

dat1=np.loadtxt("./LHC-276TeV-FILES/PionKaonProton/GRID_10BINS_1020_PionKaonProton.dat")

datlist=[dat1]

for dat in datlist:
    dat.shape=(10,10,10,10,10,6)


p1=dat1[:,0,0,0,0,0]
p2=dat1[0,:,0,0,0,1]
p3=dat1[0,0,:,0,0,2]
p4=dat1[0,0,0,:,0,3]
p5=dat1[0,0,0,0,:,4]

interpfun1 = ndsplines.make_interp_spline((p1,p2,p3,p4,p5), dat1[:,:,:,:,:,-1])
#interpfun2 = ndsplines.make_interp_spline((p1,p2,p3,p4,p5), dat2[:,:,:,:,:,-1])
#interpfun3 = ndsplines.make_interp_spline((p1,p2,p3,p4,p5), dat3[:,:,:,:,:,-1])
#interpfun4 = ndsplines.make_interp_spline((p1,p2,p3,p4,p5), dat4[:,:,:,:,:,-1])
#interpfun5 = ndsplines.make_interp_spline((p1,p2,p3,p4,p5), dat5[:,:,:,:,:,-1])

def single(x):

   return interpfun1(np.array([x[0], x[1], x[2], x[3], x[4] ]))
   #return interpfun1(np.array([x[0], x[1], x[2], x[3], x[4] ]))


#def sumxhi(x):
#    return ( interpfun1(np.array([x[0], x[1], x[2], x[3], x[4] ]))
#            +interpfun2(np.array([x[0], x[1], x[2], x[3], x[4] ]))
#            +interpfun3(np.array([x[0], x[1], x[2], x[3], x[4] ]) )                      
#                       )[0]



print("Begin minimization.....\n\n")

m = Minuit.from_array_func( single, (41, 0.20, 0.03, 0.13690, 0.25), error=(0.01, 0.01, 0.01, 0.01, 0.01), 
                            limit=  ( (30, 60), (0.08, 0.25), (0.005, 0.1), (0.130, 0.155), (0.2, 0.6) ),  
                            errordef=0.5)

m.migrad()  # run optimiser
m.minos()  # run optimiser

print("values=", m.values)  # {'x': 2,'y': 3,'z': 4}
print("values=", m.errors)  # {'x': 2,'y': 3,'z': 4}

temp = m.matrix(correlation=True)
error = m.hesse()
print(temp)
print(error)


#print("\n chi2/NDF = ",single([m.values[0], m.values[1], m.values[2], m.values[3], m.values[4]])[0]/58)   # RHIC
print("\n chi2/NDF = ",single([m.values[0], m.values[1], m.values[2], m.values[3], m.values[4]])[0]/106)





