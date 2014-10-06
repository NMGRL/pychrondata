'''
'''
OUTLET='V'
EQ_DELAY=1

def main():
    info('generic measurement script')
    
    set_time_zero()
    
    #set_source_params()
    #set_deflections()

    activate_detectors('H1','AX','CDD')
    position_magnet('Ar40', detector='H1')
    set_fits('Ar40:linear','Ar39:linear', 'Ar36:parabolic')

    #h1s=detector['H1'].signal
    #if h1s <10:
#       info('H1 signal is to low {}'.format(h1s))

    #sniff the gas during equilibration
    close(OUTLET)
    sleep(EQ_DELAY)
    
    multicollect(ncounts=5, integration_time=1)
    #peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)    
    baselines(ncounts=2,mass=40.5, detector='H1')
    #baselines(counts=50,mass=0.5, detector='CDD')
    
    info('finished measure script')