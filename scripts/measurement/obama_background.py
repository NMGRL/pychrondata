'''
'''
def func():
    info('action performed')
    
def main():
    
    info('background measurement script')
        
    activate_detectors('H1','AX','L1','L2','CDD')
    regress('parabolic')
    
    position_magnet('Ar40', detector='H1')

    '''
    Equilibrate is non-blocking so use a sniff or sleep as a placeholder
    e.g sniff(<equilibration_time>) or sleep(<equilibration_time>)
    '''
    equilibrate(eqtime=1, outlet='V')
    set_time_zero()
    
    #sniff the gas during equilibration
    #sniff(5)
    sleep(1)
    
    #set conditions
    '''
        order added defines condition precedence.
        conditions after the first true condition are NOT evaluated
        
    '''
    #add_termination('age','<',10000, start_count=5, frequency=2)
    #add_truncation('age','>',10.6, start_count=20, frequency=10)
    #add_action('age','>',10.6, start_count=20, frequency=10, 
    #            action='sleep(10)')
    #add_action('age','<',10000, start_count=5, frequency=2,
    #              action=func)
    #add_action('age','<',10000, start_count=5, frequency=2,
    #              action='sleep(7)',
    #              resume=True
    #              )
    #add_action('age','<',10000, start_count=5, frequency=2,
    #              action='gosub("snippet")')
                  
    multicollect(ncounts=10, integration_time=1)
    
    #multicollect baselines
    baselines(ncounts=3,settling_time=0.5,mass=39.5)

    info('finished measure script')
#=============================EOF=======================================================
#peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)    
    
#peak hop baselines
#baselines(counts=50,mass=0.5, detector='CDD')

'''
outlet_valve: V
    
def main():
    info('air measurement script')
    
    set_time_zero()
    
    set_source_parameters()
    set_source_optics()
    set_cdd_operating_voltage()

    activate_detectors('H1','AX','CDD')
    regress('parabolic')
    
    position('Ar40', detector='H1')

    #sniff the gas during equilibration
    #sniff(5)
    #sleep(1)
    
    multicollect(ncounts=80, integration_time=1)
    #peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)    
    
    #peak hop baselines
    #baselines(counts=50,mass=0.5, detector='CDD')

    #multicollect baselines
    baselines(counts=5,mass=40.5)

    info('finished measure script')
'''
