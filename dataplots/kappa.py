
import numpy as np
from scipy.interpolate import interp1d

# Define a function to get the compressibility
def deriv( x, f ):
    dx = 0.001
    return (f(x+dx) - f(x-dx))/(2.*dx)

def compressibility( mudat, ndat):
    ''' 
    Returns the normalized comprsesibility, \kappa_{T} / \kappa_{T}^{0}
    where \kappa_{T}_{0} is the zero T compressibility of a free Fermi gas
    (note: up to some numerical factors, which are defined in the writeup)
    '''
    # I want to evaluate a derivative of n^{2/3} to obtain the compressibility.
    # The evaluation should be at the points where we have data
    # 
    # PLEASE BE AWARE THAT THIS MUST BE MULTIPLIED BY A NUMERICAL FACTOR
    # THAT DEPENDS ON THE SPIN DEGENERACY gspin:
    #  
    # numfactor = (6.* np.pi**2.)**(2./3.) / np.pi**2  / gspin**(2./3.)
    # 
    n23 = ndat**(2./3.)
    mupad = 0.2 
    mupadded  = np.concatenate(([mudat[0]-mupad], mudat, [mudat[-1]+mupad]))
    n23padded = np.concatenate(([n23[0]], n23, [n23[-1]]))
    n23f = interp1d( mupadded , n23padded)
    cdat = deriv( mudat, n23f)
    return cdat
 
def compressibility_bare( mudat, ndat):
    ''' 
    Returns the unnormalized (bare) compressibility, \kappa_{T} , which is 
    defined as:
    \kappa_{T} = (1/n**2) dn/dmu  \equiv  - d(n**-1)/dmu 
    '''
    # I want to evaluate a derivative of n^{-1} to obtain the unnormalized 
    # compressibility.
    # The evaluation should be at the points where we have data

    # The inverse density can't handle zeros, so make them a very small number
    ndat[ np.where( ndat < 1e-10 )  ]  = 1e-10
    nm1 = -1./ndat
    mupad = 0.2 
    mupadded  = np.concatenate(([mudat[0]-mupad], mudat, [mudat[-1]+mupad]))
    nm1padded = np.concatenate(([nm1[0]], nm1, [nm1[-1]]))
    nm1f = interp1d( mupadded , nm1padded)
    cdat = deriv( mudat, nm1f)
    return cdat

def kappa0( dens, gspin):
    """
    Define function to
    plot the compressibility of a non-interacting g-spin component 
    Fermi gas,  in units of a^3 / E_r 
    """
    numfactor = 3.*gspin**(2./3.) / (6.*np.pi**2.)**(2./3.)  * (np.pi**2./2.)
    return dens**(-5./3.) * numfactor

 
