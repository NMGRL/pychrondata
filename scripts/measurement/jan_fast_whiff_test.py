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
  eqtime: 20
  use_extraction_eqtime: True
whiff:
  eqtime: 10
  counts: 10
  abbreviated_count_ratio: 0.25
  conditionals:
    - action: run
      attr: age
      teststr: age>50
      start: 9
    - action: run_remainder
      teststr: age<0.1
      attr: age
      start: 9
'''

ACTIVE_DETECTORS=('H2','H1','AX','L1','L2', 'CDD')
#FITS=('Ar41:linear','Ar40:linear', 'Ar39:parabolic','Ar38:parabolic','Ar37:parabolic','Ar36:parabolic')

def main():
    if mx.peakcenter.before:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)

    #open a plot panel for this detectors
    activate_detectors(*ACTIVE_DETECTORS)

    if mx.baseline.before:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector)

    #position mass spectrometer
    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)

    #gas is staged behind inlet
    meqtime = mx.whiff.eqtime
    #post equilibration script triggered after eqtime elapsed
    #equilibrate is non blocking
    #so use either a sniff of sleep as a placeholder until eq finished
    equilibrate(eqtime=meqtime, do_post_equilibration=False,
                inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet)

    #equilibrate returns immediately after the inlet opens
    set_time_zero(0)

    #fast whiff starts whiff measurement before equilibration is finished
    offset = 5
    sniff(meqtime-offset)
    #set default regression
    set_fits()
    set_baseline_fits()
    
    result = whiff(ncounts=mx.whiff.counts, conditionals=mx.whiff.conditionals)
    wab=1.0
    if result=='run':
       post_equilibration()
       wab = mx.whiff.abbreviated_count_ratio
    elif result=='run_remainder':
       reset_measurement(ACTIVE_DETECTORS)
       open(mx.equilibration.outlet)
       sleep(15)
       meqtime = eqtime if mx.equlibration.use_extraction_eqtime else mx.equilibration.eqtime
       equilibrate(eqtime=meqtime, do_post_equilibration=True,
                inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet)
       set_time_zero(0)
       sniff(meqtime)
       
    multicollect(ncounts=mx.multicollect.counts*wab, integration_time=1)
    if mx.baseline.after:
        baselines(ncounts=mx.baseline.counts*wab, mass=mx.baseline.mass, detector=mx.baseline.detector)

    if mx.peakcenter.after:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)
    info('finished measure script')

#========================EOF==============================================================
