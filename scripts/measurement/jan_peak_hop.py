#!Measurement
'''
'''
#counts

#baselines
BASELINE_COUNTS= 90
BASELINE_DETECTOR= 'H1'
BASELINE_MASS= 34.2
BASELINE_BEFORE= False
BASELINE_AFTER= True
BASELINE_SETTLING_TIME= 10

#peak center
PEAK_CENTER_BEFORE= False
PEAK_CENTER_AFTER= True
PEAK_CENTER_DETECTOR= 'H1'
PEAK_CENTER_ISOTOPE= 'Ar40'
PEAK_DETECTORS= ('H1','AX','CDD')

#equilibration
EQ_TIME= eqtime
INLET= 'R'
OUTLET= 'O'
EQ_DELAY= 3.0

ACTIVE_DETECTORS=('H2','H1','AX','L1','L2','CDD')
FITS=('Ar41:average_SEM','Ar40:parabolic','Ar39:parabolic','Ar38:linear','Ar37:linear','Ar36:parabolic','Ar35:linear')
BASELINE_FITS=('average_SEM',)
USE_WARM_CDD=False

NCYCLES=12

def main():
    info('unknown measurement script')
    
    activate_detectors(*ACTIVE_DETECTORS)
   
    if PEAK_CENTER_BEFORE:
        peak_center(detector=PEAK_CENTER_DETECTOR,isotope=PEAK_CENTER_ISOTOPE)
    
    position_magnet('Ar40', detector='H1')
    
    hops=load_hops('hops/hops.txt')
    define_hops(hops)
    '''
    Equilibrate is non-blocking so use a sniff or sleep as a placeholder
    e.g sniff(<equilibration_time>) or sleep(<equilibration_time>)
    '''
    equilibrate(eqtime=EQ_TIME, inlet=INLET, outlet=OUTLET, delay=EQ_DELAY)
    set_time_zero(5)
    
    #sniff the gas during equilibration
    sniff(EQ_TIME-1)
    set_fits(*FITS)
    set_baseline_fits(*BASELINE_FITS)

    sleep(0.5)
    
    if BASELINE_BEFORE:
        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, detector=BASELINE_DETECTOR,
                  settling_time=BASELINE_SETTLING_TIME)
                  
    #multicollect on active detectors
    #multicollect(ncounts=MULTICOLLECT_COUNTS, integration_time=1)
   
    peak_hop(ncycles=NCYCLES, hops=hops)
    
    if BASELINE_AFTER:
        #necessary if peak hopping
        define_detectors('Ar40','H1')
        
        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, detector=BASELINE_DETECTOR,
                  settling_time=BASELINE_SETTLING_TIME)
    if PEAK_CENTER_AFTER:
        activate_detectors(*PEAK_DETECTORS, **{'peak_center':True})
        peak_center(detector=PEAK_CENTER_DETECTOR, isotope=PEAK_CENTER_ISOTOPE)
    
    if USE_WARM_CDD:
       gosub('warm_cdd', argv=(OUTLET,))    
       
    info('finished measure script')