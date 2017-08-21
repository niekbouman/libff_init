import math

def find_st(p):
    t = p-1
    s = 0
    while t%2 == 0:
        t >>= 1
        s += 1
        
    return s,t

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def compute_init_vals(p, limb_bitsize=64):
    iv = dict()
    iv['modulus'] = p
    iv['s'],iv['t'] = find_st(p)
    iv['t_minus_1_over_2'] = (iv['t']-1)//2
    iv['euler'] = (p-1)//2
    iv['num_bits'] = math.ceil(math.log2(p))
    iv['inv'] = 2**limb_bitsize - modinv(p,2**limb_bitsize)
    iv['Rsquared'] = (2**limb_bitsize)**(2 * math.ceil(math.log2(p)/limb_bitsize)) % p
    iv['Rcubed'] = (2**limb_bitsize)**(3 * math.ceil(math.log2(p)/limb_bitsize)) % p
    return iv 

def pprint(iv,prefix,limb_bitsize=64):
    numlimbs = math.ceil(iv['num_bits']/limb_bitsize)
    print ('auto modulus = bigint<static_cast<mp_size_t>(%d)>("%s");'%(numlimbs,iv['modulus']))

    for k in ['euler','t','t_minus_1_over_2','Rsquared','Rcubed',]:
            print('%s::%s = bigint<static_cast<mp_size_t>(%d)>("%s");' % (prefix,k,numlimbs,iv[k]))

    print('%s::%s = %s;' % (prefix,'s',iv['s']))            
    print('%s::%s = %s;' % (prefix,'num_bits',iv['num_bits']))
    
    print('%s::%s = %sUL;' % (prefix,'inv',iv['inv']))
    