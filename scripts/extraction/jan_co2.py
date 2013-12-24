def main():
    info('Jan unknown laser analysis')
    
    gosub('jan:PrepareForCO2Analysis')

    if analysis_type=='blank':
        info('is blank. not heating')
    else:
        info('move to position {}'.format(position))
        move_to_position(position)
        
        if ramp_rate>0:
            '''
            style 1.
            '''
#           begin_interval(duration)
#           info('ramping to {} at {} {}/s'.format(extract_value, ramp_rate, extract_units)
#           ramp(setpoint=extract_value, rate=ramp_rate)
#           complete_interval()
            '''
            style 2.
            '''
            #elapsed=ramp(setpoint=extract_value, rate=ramp_rate)
            #sleep(min(0, duration-elapsed))
            pass
            
        else:
            info('set heat to {}'.format(extract_value))
            extract(extract_value)
            sleep(duration)

    if not analysis_type=='blank':
        disable()
    sleep(cleanup)