#!Measurement
'''
'''

#===============================================================================
# parameter definitions
#===============================================================================
#multicollect
MULTICOLLECT_COUNTS      = 5
MULTICOLLECT_ISOTOPE     = 'Ar40'
MULTICOLLECT_DETECTOR    = 'H1'

#baselines
BASELINE_COUNTS          = 30
BASELINE_DETECTOR        = 'H1'
BASELINE_MASS            = 39.5
BASELINE_BEFORE          = False
BASELINE_AFTER           = True

#peak center
PEAK_CENTER_BEFORE       = False
PEAK_CENTER_AFTER        = False
PEAK_CENTER_DETECTOR     = 'H1'
PEAK_CENTER_ISOTOPE      = 'Ar40'

#equilibration
EQ_TIME                  = 5.0
EQ_INLET                 = 'S'
EQ_OUTLET                = 'O'
EQ_DELAY                 = 2.0

#PEAK HOP
USE_PEAK_HOP             = True
NCYCLES                  = 2

           
"""
    HOPS definition
    
    HOPS is a list of peak hops.
    a peak hop is a list of iso:detector pairs plus the number of counts to measure 
    for this hop. The first iso:detector pair is used for positioning.
    
    added rev 1665
        specify a deflection for the iso:det pair
        Ar40:H1:30
        if no value is specified and the deflection value had been changed by a previous cycle
        then set the deflection to the config. value
        
    
    ('Ar40:H1,     Ar39:AX,     Ar36:CDD',      10) 
    ('Ar40:L2,     Ar39:CDD',                   20),
    means position Ar40 on detector H1 and
    record 10 H1,AX,and CDD measurements. After 10 measurements 
    position Ar40 on detector L2, record 20 measurements.
    
    repeat this sequence NCYCLES times 
    
"""

HOPS=[('Ar40:H1:10, Ar38:L1, Ar37:L2, Ar36:CDD',      3, 1),
       #('bs:39.5:H1', 3, 1),
      #('Ar40:L2,     Ar39:CDD',                   5, 1),
      #('Ar38:CDD',                                5, 1),
      ('Ar39:CDD',                                3, 1),
      #('Ar38:CDD',                                3, 1),
     # ('Ar37:CDD',                                3, 5),
      ]
               
#Detectors
ACTIVE_DETECTORS         = ('H2','H1','AX','L1','L2','CDD')
#FITS                     = ('average','parabolic','parabolic','linear','linear','parabolic')
FITS=('Ar41:(,10,average), (10,,cubic)',
      'Ar40:parabolic', 
      'Ar39AX:parabolic', 
      'Ar39CDD:parabolic',
      'Ar39:parabolic',
      'Ar38:linear', 
      'Ar37:linear', 
      'Ar36:parabolic')
BASELINE_FITS=('average_SEM',)
#===============================================================================
# 
#===============================================================================


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
    #set_source_parameters(YSymmetry=10)
    
    #or leave blank and values are loaded from a config file (setupfiles/spectrometer/config.cfg)
    #set_source_optics()
    
    #set the cdd operating voltage
    #set_cdd_operating_voltage(100)
    
    if PEAK_CENTER_BEFORE:
        peak_center(detector=PEAK_CENTER_DETECTOR,isotope=PEAK_CENTER_ISOTOPE)
    
    activate_detectors(*ACTIVE_DETECTORS)
    
    
    #position mass spectrometer even though this is a peak hop so an accurate sniff/eq is measured
    position_magnet(MULTICOLLECT_ISOTOPE, detector=MULTICOLLECT_DETECTOR)

    #gas is staged behind inlet
    
    #post equilibration script triggered after eqtime elapsed
    #equilibrate is non blocking    
    #so use either a sniff of sleep as a placeholder until eq finished
    equilibrate(eqtime=EQ_TIME, inlet=EQ_INLET, outlet=EQ_OUTLET)
    
    #equilibrate returns immediately after the inlet opens
    set_time_zero()
    
    sniff(EQ_TIME)
    
    if USE_PEAK_HOP:
        define_hops(HOPS)
    #set default regression
    set_fits(*FITS)
    set_baseline_fits(*BASELINE_FITS)
    
    if BASELINE_BEFORE:
        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, detector=BASELINE_DETECTOR)
        
    if USE_PEAK_HOP:
        #hops=load_hops('hops/hop.txt')
        #info(hops)
        
        peak_hop(ncycles=NCYCLES, hops=HOPS)
    else:
        #multicollect on active detectors
        multicollect(ncounts=MULTICOLLECT_COUNTS, integration_time=1)
    
    if BASELINE_AFTER:
        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, 
                      detector=BASELINE_DETECTOR, settling_time=1)
    if PEAK_CENTER_AFTER:
        peak_center(detector=PEAK_CENTER_DETECTOR,isotope=PEAK_CENTER_ISOTOPE)
    
    info('finished measure script')
    
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