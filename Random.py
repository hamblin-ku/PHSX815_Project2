# File:     Random.py
# Author:   Kurt Hamblin
# Description:  Random() class that can generate random data

import numpy as np

class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        self.m_u = np.uint64(self.m_u * 2862933555777941757) + np.uint64(7046029254386353087)
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        """ Generate random float on (0,1) """
        return 5.42101086242752217E-20 * self.int64()
    
    # function returns a random floating point number (0 to infinity) from a Rayleigh Distribution
    def Rayleigh(self):
        R = self.rand()

        Z = np.sqrt(-2*np.log(R))
        return Z

        # Peforms a die roll
    def roll_die(self, Nsides = 6, weights = None):
        """ Roll a die with Nsides and optional bias"""
        # Generate a random float from 0->1
        rand_num = self.rand()
        
        # If weights are not provided, we roll a fair die
        if weights is None:
            # Divide 0->1 evenly into slices of width 1/Nsides
            ch = 1 / Nsides
            
            # We iterate through, summing up the current and previous bins until the random float is less than the current sum
            for i in range(Nsides):
                if rand_num < ch*(i+1):
                    # reurn (i+1) because range(Nsides) starts at 0 but the first index 0 corresponds to side 1, and so on
                    return i + 1
                    
        # If weights are provided, we use them
        else:
            # Initilize the total count
            total = 0
            # Now we iterate through as above, and add the current weight to the total until the random float is less than the total
            for i in range(Nsides):
                total += weights[i]
                if rand_num < total:
                    # reurn (i+1) because range(Nsides) starts at 0 but the first index 0 corresponds to side 1, and so on
                    return i + 1
        
