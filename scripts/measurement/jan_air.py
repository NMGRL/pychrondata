'''
    equilibration_time: 15
    outlet_valve: V

    asdfasdf: asdfadsaf
'''
EQ_TIME= 1
INLET= 'R'
OUTLET= 'S'
DELAY= 3.0
TIME_ZERO_OFFSET=0
#asfdasdf
def set_source_params():
    set_ysymmetry(100)
    set_zsymmetry(100)
    set_zfocus(100)
    set_extraction_lens(100)
    
def set_deflections():
    set_deflection('H2',0)
    set_deflection('H1',0)
    set_deflection('AX',125)
    set_deflection('L1',225)
    set_deflection('L2',525)
    set_deflection('CDD',160)
    
def main():
    info('generic measurement script')

    #set_source_params()
    #set_deflections()

    activate_detectors('H1','AX','CDD', peak_center=True)
    #peak_center(detector='H1',isotope='Ar40')

    activate_detectors('H2','H1','AX','L1','L2','CDD')
    #regress('linear')
                    
    #peak_center(detector='H1',isotope='Ar40')
    
    position_magnet('Ar40', detector='H1')

    #h1s=detector['H1'].signal
    #if h1s <10:
#        info('H1 signal is to low {}'.format(h1s))

    equilibrate(eqtime=EQ_TIME, inlet=INLET, outlet=OUTLET)
    set_time_zero()
    #sniff the gas during equilibration
    sniff(EQ_TIME)
    #sleep(12)
    
    multicollect(ncounts=8, integration_time=1)
    #peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)    
    
    baselines(2, mass=40.5, settling_time=0, detector='H1')
    #baselines(counts=5,mass=0.5, detector='CDD')
    activate_detectors('H1','AX','CDD', peak_center=True)
    #peak_center(detector='H1',isotope='Ar40')

    info('finished measure script')