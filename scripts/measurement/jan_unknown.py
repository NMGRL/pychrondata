#!Measurement
'''
baseline:
  after: true
  before: false
  counts: 30
  detector: H1
  mass: 39.59
default_fits: nominal
multicollect:
  counts: 200
  detector: H1
  isotope: Ar40
peakcenter:
  after: false
  before: false
  detector: H1
  isotope: Ar40
equilibration:
  inlet: R
  outlet: S
  inlet_delay: 3
'''

#equilibration
EQ_TIME= 20.0

#PEAK HOP
USE_PEAK_HOP= False
#PEAK_HOPS=[((('Ar40','H1'),  'CDD'),  10),
#           ((('Ar39','CDD')),         10),
#           ((('Ar38', 'CDD')),        10),
#           ((('Ar37', 'CDD')),        10),
#           ((('Ar36', 'CDD')),        10),
 #          ]


ACTIVE_DETECTORS=('H2','H1','AX','L1','L2', 'CDD')
#FITS=('Ar41:linear','Ar40:linear', 'Ar39:parabolic','Ar38:parabolic','Ar37:parabolic','Ar36:parabolic')

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

    if mx.peakcenter.before:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)

    #open a plot panel for this detectors
    activate_detectors(*ACTIVE_DETECTORS)

    if mx.baseline.before:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector)


    #position mass spectrometer
    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)

    #gas is staged behind inlet

    #post equilibration script triggered after eqtime elapsed
    #equilibrate is non blocking
    #so use either a sniff of sleep as a placeholder until eq finished
    equilibrate(eqtime=EQ_TIME, inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet)

    #equilibrate returns immediately after the inlet opens
    set_time_zero(7)

    sniff(EQ_TIME)
    #set default regression
    set_fits()
    set_baseline_fits()
    if USE_PEAK_HOP:
        '''

            hop = (Isotope, DetA)[,DetB,DetC...], counts

            ex.
            hops=[((('Ar40','H1'),'CDD'),  10),
                  ((('Ar39','CDD')),       30),

        '''
        peak_hop(hops=PEAK_HOPS)
    else:
        #multicollect on active detectors
        multicollect(ncounts=mx.multicollect.counts, integration_time=1)

    if mx.baseline.after:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector)

    if mx.peakcenter.after:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)
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
