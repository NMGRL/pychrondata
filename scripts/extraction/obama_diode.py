def main():
    info('Obama unknown laser analysis')
    
    gosub('obama:PrepareForCO2Analysis')
    
    if analysis_type=='blank':
        info('is blank. not heating')
    else:
        info('move to position {}'.format(position))
        move_to_position(position)
        info('set heat to {}'.format(extract_value))
        extract(extract_value)
    
        info('executing pattern {}'.format(pattern))
    
    
        ''' 
            the concept is 
                1. to thermal shock the crystals by varying intensity
                2. couple with different intra and extra crystal features
                
                options
                1. pulse laser
                    a. vary request power
                    b. use spinning mask
                    
                    square wave
                    
                2. vary focal point
                    sweep z down and up.
                    
                    sine wave                     
                    
        
        set_z(focus_value)
        
        for i in range(nsweeps):
            #defocus down
            set_z(defocus_value,
                  velocity=0.25)
            set_z(focus_value,
                  velocity=0.25)
        '''
        
        #style 1.
        #begin_interval(duration)
        #execute_pattern(pattern)
        #complete_interval()
        
        #style 2.
        #elapsed=execute_pattern(pattern, block=True)
        #sleep(min(0,duration-elapsed))
    
        end_extract()
    
    
    sleep(cleanup)