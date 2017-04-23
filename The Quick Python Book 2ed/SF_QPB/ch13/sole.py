"""sole module: contains function sole, save, show"""

import cPickle
    
_soleMemCacheD = {}
_soleDiskFileS = "solecache"

# this  initialization code will be executed when this module is first loaded
file = open(_soleDiskFileS, 'r')
_soleMemCacheD = cPickle.load(file)
file.close()

# Public functions
def sole(m, n, t):
    """sole(m,n,t): perform the sole calculation, using the cache if possible."""
    global _soleMemCacheD
    if _soleMemCacheD.has_key((m, n, t)):
        return _soleMemCacheD[(m, n, t)]
    else:
        # . . . do some time-consuming calculations . . .
        _soleMemCacheD[(m, n, t)] = result
        return result

def save():
    """save(): save the cache to disk including the results of this session."""
    global _soleMemCacheD, _soleDiskFileS
    file = open(_soleDiskFileS, 'w')
    cPickle.dump(_soleMemCacheD, file)
    file.close()

def show():
    """show(): print the cache"""
    global _soleMemCacheD
    print _soleMemCacheD
