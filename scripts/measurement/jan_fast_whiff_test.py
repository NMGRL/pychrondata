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
  counts: 60
  detector: H1
  isotope: Ar40
peakcenter:
  after: false
  before: false
  detector: H1
  isotope: Ar40
equilibration:
  inlet: S
  outlet: O
  inlet_delay: 3
  eqtime: 20
  use_extraction_eqtime: True
whiff:
  eqtime: 10
  counts: 5
  offset: 5 #at eqtime-offset start the whiff measurement. make offset+counts=eqtime
  additional_eqtime: 10
  abbreviated_count_ratio: 0.25
  conditionals:
    - action: run
      attr: Ar40
      teststr: Ar40>50
    - action: run_remainder
      teststr: Ar40<10
      attr: Ar40
'''


ACTIVE_DETECTORS = ('H2', 'H1', 'AX', 'L1', 'L2', 'CDD')
# FITS=('Ar41:linear','Ar40:linear', 'Ar39:parabolic','Ar38:parabolic','Ar37:parabolic','Ar36:parabolic')

def main():
    """
        Fast Whiff.

        Make whiff measurement and determine next step during the equilibration.
        set whiff.offset to the number of seconds before the end of equilibration to
        start the whiff measurement. for an all equilibration whiff (sniff whiff)
        make whiff.offset+whiff.counts<=whiff.eqtime

        Actions:
            Run - Run the current gas. abbreviate measurement using whiff.abbreviated_count_ratio
            Run Remainder - append the gas in the analytical section and run as normal

        if offset is 0
            Run Remainder - pump the mass spec then equilibrate with the analytical section

    """
    #display information with info(msg)
    info('unknown measurement script')

    if mx.peakcenter.before:
        peak_center(detector=mx.peakcenter.detector, isotope=mx.peakcenter.isotope)

    #open a plot panel for this detectors
    activate_detectors(*ACTIVE_DETECTORS)

    if mx.baseline.before:
        baselines(ncounts=mx.baseline.counts, mass=mx.baseline.mass, detector=mx.baseline.detector)

    #position mass spectrometer
    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)

    meqtime = mx.whiff.eqtime

    # use offset to start the whiff ``offset`` seconds before the end of equilibration
    equil(meqtime, False, offset=mx.whiff.offset)

    result = whiff(ncounts=mx.whiff.counts, conditionals=mx.whiff.conditionals)
    info('Whiff result={}'.format(result))
    wab = 1.0
    if result == 'run':
        info('Continuing whiff measurment')
        post_equilibration()
        wab = mx.whiff.abbreviated_count_ratio
    elif result == 'run_remainder':
        info('Measuring remainder instead')
        if not offset:
            eqt = eqtime
            reset_measurement(ACTIVE_DETECTORS)

            #pump out spectrometer
            open(mx.equilibration.outlet)
            sleep(15)

            #open the outer spectrometer pipette
            open('S')
        else:
            eqt = mx.whiff.additional_eqtime

        #equilibrate with entire section
        #if offset dont delay between outlet close and inlet open because outlet already closed
        equil(eqt, delay=0 if offset else None)

    multicollect(ncounts=mx.multicollect.counts * wab, integration_time=1)
    if mx.baseline.after:
        baselines(ncounts=mx.baseline.counts * wab, mass=mx.baseline.mass, detector=mx.baseline.detector)

    if mx.peakcenter.after:
        peak_center(detector=mx.peakcenter.detector, isotope=mx.peakcenter.isotope)
    info('finished measure script')


def equil(eqt, do_post=True, offset=0, delay=None):
    """
        gas is staged behind inlet
        post equilibration script triggered after eqtime elapsed
        equilibrate is non blocking
        so use either a sniff of sleep as a placeholder until eq finished

    :param eqt: int equilibration time
    :param do_post: bool do post equilibration
    :param offset: int whiff offset
    :param delay: int delay between outlet close and inlet open
    :return: None
    """
    if delay is None:
        delay = 3

    equilibrate(eqtime=eqt, do_post_equilibration=do_post,
                inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet,
                delay=delay)

    #equilibrate returns immediately after the inlet opens
    set_time_zero(0)

    if offset:
        info('Doing a fast whiff. Checking the equilibration gas')

    sniff(eqt - offset)
    #set default regression
    set_fits()
    set_baseline_fits()

#========================EOF==============================================================
