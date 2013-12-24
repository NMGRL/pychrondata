#!Measurement
'''
'''
#counts
MULTICOLLECT_COUNTS= 20

#baselines
BASELINE_COUNTS= 10
BASELINE_DETECTOR= 'H1'
BASELINE_MASS= 39.5
BASELINE_BEFORE= False
BASELINE_AFTER= True

#peak center
PEAK_CENTER_BEFORE= False
PEAK_CENTER_AFTER= False
PEAK_CENTER_DETECTOR= 'H1'
PEAK_CENTER_ISOTOPE= 'Ar40'


#equilibration
EQ_TIME= eqtime

INLET= 'R'
OUTLET= 'S'
DELAY= 3.0
TIME_ZERO_OFFSET=0

#PEAK HOP
ACTIVE_DETECTORS=('H1','AX', 'L1','L2', 'CDD')
FITS=('Ar40:parabolic', 'Ar39:parabolic','Ar38:linear','Ar37:linear','Ar36:parabolic')
BASELINE_FITS=('average_SEM',)
#FITS=[
#      ((0,5),('linear', 'linear', 'linear', 'linear','linear')),
#      ((5,None),('linear', 'parabolic', 'parabolic', 'parabolic', 'parabolic')),
#      ]

ACTIONS= [(False,('age','<',10.6,20,10,'',False)),
         ]

TRUNCATIONS = [(False, ('age','<',10.6,20,10,)),
              ]

TERMINATIONS= [(False, ('age','<',10.6,20,10))
              ]
        

def main():
    #this is a comment
    '''
        this is a multiline 
        comment aka docstring
    '''
    #display information with info(msg)
    info('unknown measurement script')
    
    #set the spectrometer parameters
    #provide a value
    set_source_parameters(YSymmetry=10)
    
    #or leave blank and values are loaded from a config file (setupfiles/spectrometer/config.cfg)
    set_source_optics()
    
    #set the cdd operating voltage
    set_cdd_operating_voltage(100)
    
    if PEAK_CENTER_BEFORE:
        peak_center(detector=PEAK_CENTER_DETECTOR,isotope=PEAK_CENTER_ISOTOPE)
        
    #open a plot panel for this detectors
    activate_detectors(*ACTIVE_DETECTORS)
        
    #set default regression
    #regress(*FITS)

    #position mass spectrometer 
    position_magnet('Ar40', detector='H1')

    #gas is staged behind inlet
    
    #post equilibration script triggered after eqtime elapsed
    #equilibrate is non blocking    
    #so use either a sniff of sleep as a placeholder until eq finished
    equilibrate(eqtime=EQ_TIME, inlet=INLET, outlet=OUTLET)
    
    for use,args in ACTIONS:
        if use:
            add_action(*args)
            
    for use,args in TRUNCATIONS:
        if use:
            add_truncation(*args)
            
    for use, args in TERMINATIONS:
        if use:
            add_termination(*args)
            
    #equilibrate returns immediately after the inlet opens
    set_time_zero(offset=TIME_ZERO_OFFSET)
    
    sniff(EQ_TIME)
    
    set_fits(*FITS)
    set_baseline_fits(*BASELINE_FITS)
    
    if BASELINE_BEFORE:
        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, detector=BASELINE_DETECTOR)

    #multicollect on active detectors
    multicollect(ncounts=MULTICOLLECT_COUNTS, integration_time=1)
    
    clear_conditions()
    
    if BASELINE_AFTER:
        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, detector=BASELINE_DETECTOR)
    if PEAK_CENTER_AFTER:
        peak_center(detector=PEAK_CENTER_DETECTOR,isotope=PEAK_CENTER_ISOTOPE)
    
    
    #WARM CDD
    warm_cdd()
    
    info('finished measure script')
   
def warm_cdd():
    '''
        1. blank beam
        2. move to desired position
        3. unblank beam
    '''
    if not is_last_run():
        set_deflection('CDD',2000)
        
        position_magnet(28.04, detector='H1')
        #or 
        #position_magnet(5.00, dac=True)
        
        #return to config.cfg deflection value
        set_deflection('CDD')
        
         
#========================EOF==============================================================
    #peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)    
    #baselines(counts=50,mass=0.5, detector='CDD')s
    
#isolate sniffer volume
    # close('S')
#     sleep(1)
#     
#     #open to mass spec
#     open('R')
#     
#     set_time_zero()
#     #display pressure wave
#     sniff(5)
#     
#     #define sniff/split threshold
#     sniff_threshold=100
#     
#     #test condition
#     #if get_intensity('H1')>sniff_threshold:
#     if True:
#         gosub('splits:jan_split', klass='ExtractionLinePyScript')
#     