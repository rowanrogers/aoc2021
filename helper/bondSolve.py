import scipy.optimize as opt
import numpy as np


def func(y, present_value, redemption, coupon, n_periods):
    discounted_cashflows = coupon * (1 - pow(1 + y, -n_periods)) / y + redemption * pow(1 + y, -n_periods)

    return present_value - discounted_cashflows

def calcYield(present_value, redemption, coupon, n_periods):

    r = opt.root(func, x0=0.01, method='hybr', args=(present_value, redemption, coupon, n_periods))

    return(r.x)

r_gov = calcYield(102.67,100,4,5)
r_corp = calcYield(96.48,100,6,5)
print(r_gov)
print(r_corp)
print(r_corp - r_gov)
