
def main():
    info('Jan uv analysis')
    #gosub('jan:PrepareForUVAnalysis')
    info('analysis type {}'.format(analysis_type))
    if analysis_type=='blank':
        info('is blank. not extracting sample gas')
    else:
        
        info('Enable Laser')
        enable()
        
        mask=get_value('mask')
        if mask:
            info('setting mask to {}'.format())
            set_motor('mask', mask)
        
        attenuator=get_value('attenuator')
        if attenuator:
            info('setting attenuator to {}'.format(attenuator))
            set_motor('attenuator', attenuator)
        
        #if not prepare():
        #   exit()
        #sleep(10, message='Waiting for laser to power on/warm up')
    
    	if not prepare():
        	exit()    
    close(description='Microbone to Turbo') 
    
    if analysis_type=='blank':  
        sleep(duration, message='Extracting gas')       
    elif position:
        info('starting extraction')    
        for pi in position:
            if isinstance(pi, str) and pi:
                pi=pi.lower()
                if pi[0] in ('l','r','d'):
                    info('tracing path: {}'.format(pi))
                    trace_path(pi) 
                else:
                    do_extract(pi)
            else:
                do_extract(pi)                
        
        disable()
        info('end extraction')
        
    sleep(cleanup,message="Cleaning gas")
    #=====================================================================================
    # continue to measurement_script
    #=====================================================================================
    
    

#=========================================================================================
# helper functions
#=========================================================================================
def do_extract(pi):
    
    info('moving to position {}'.format(pi))
    move_to_position(pi)
    sleep(1)
    
    info('set extraction value to {} {}'.format(extract_value, extract_units))
    extract(extract_value)
    sleep(duration)
    
    if disable_between_positions:
        end_extract()
    info('end extraction for {}'.format(pi))
#=========================================================================================
# EOF
#=========================================================================================