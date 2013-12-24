#!Laser
CX=-14.524
CY=8.811
PADDING=0.5
POWER=20

def main():
    with interval(10):
        info('interval a')
        with interval(5):
            info('interval b')    
            
#    for bi in xrange(1,5):
#        map_beam(bi)
        
def map_beam(bd):
    info('power map beam diameter {}'.format(bd))
    
    power_map(CX, CY, bd*(1+PADDING)*0.5, bd, POWER)    
    