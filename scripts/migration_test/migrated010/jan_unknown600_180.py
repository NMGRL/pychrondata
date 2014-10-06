'''
default_fits: nominal_fits
'''
#counts
MULTICOLLECT_COUNTS= 600

#baselines
BASELINE_COUNTS= 180
BASELINE_DETECTOR= 'H1'
BASELINE_MASS= 39.5
BASELINE_BEFORE= False
BASELINE_AFTER= True
BASELINE_SETTLING_TIME= 15

#peak center
PEAK_CENTER_BEFORE= False
PEAK_CENTER_AFTER= True
PEAK_CENTER_DETECTOR= 'H1'
PEAK_CENTER_ISOTOPE= 'Ar40'
PEAK_DETECTORS= ('H1','AX','CDD')

#equilibration
EQ_TIME= 8.0
INLET= 'R'
OUTLET= 'O'
EQ_DELAY= 3.0

ACTIVE_DETECTORS=('H2','H1','AX','L1','L2','CDD')
USE_WARM_CDD=True

def main():
    info('unknown measurement script')
    
    activate_detectors(*ACTIVE_DETECTORS)
   
    
    if PEAK_CENTER_BEFORE:
        peak_center(detector=PEAK_CENTER_DETECTOR,isotope=PEAK_CENTER_ISOTOPE)
    
    if BASELINE_BEFORE:
        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, detector=BASELINE_DETECTOR,
                  settling_time=BASELINE_SETTLING_TIME)
    
    position_magnet('Ar40', detector='H1')

    '''
    Equilibrate is non-blocking so use a sniff or sleep as a placeholder
    e.g sniff(<equilibration_time>) or sleep(<equilibration_time>)
    '''
    equilibrate(eqtime=EQ_TIME, inlet=INLET, outlet=OUTLET, delay=EQ_DELAY)
    set_time_zero()
    
    #sniff the gas during equilibration
    sniff(EQ_TIME)    
    #set_fits(*FITS)
    set_fits()
    #set_baseline_fits(*BASELINE_FITS)
    set_baseline_fits()
    sleep(1)
    
    #multicollect on active detectors
    multicollect(ncounts=MULTICOLLECT_COUNTS, integration_time=1)
    
    if BASELINE_AFTER:
        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, detector=BASELINE_DETECTOR, 
                  settling_time=BASELINE_SETTLING_TIME)
    if PEAK_CENTER_AFTER:
        activate_detectors(*PEAK_DETECTORS, **{'peak_center':True})
        peak_center(detector=PEAK_CENTER_DETECTOR,isotope=PEAK_CENTER_ISOTOPE)
    
    if USE_WARM_CDD:
       gosub('warm_cdd', argv=(OUTLET,))    
       
    info('finished measure script')