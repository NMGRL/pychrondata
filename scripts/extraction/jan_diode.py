def main():
    info('Jan unknown laser analysis')
    
    gosub('jan:PrepareForCO2Analysis')
    
    if analysis_type=='blank':
        info('is blank. not heating')
    else:
        info('move to position {}'.format(position))
        move_to_position(position)
        info('ramp_rate {}'.format(ramp_rate))
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
            elapsed=ramp(setpoint=extract_value, rate=ramp_rate)
            
            if not elapsed:
                           exit()
            else:
                           sleep(min(0, duration-elapsed))
            
        else:
            info('set heat to {}'.format(extract_value))
            enable()
            extract()
            sleep(duration)
            disable()
    if not analysis_type=='blank':
        end_extract()
    sleep(cleanup)