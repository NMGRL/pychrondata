def main():
    info('Jan uv analysis')
    gosub('jan:PrepareForUVAnalysis')
    info('analysis type {}'.format(analysis_type))
    if analysis_type=='blank':
        info('is blank. not extracting sample gas')
    else:
        info('is unknown')
        info('Enable Laser')
        enable()

        sleep(10, message='Waiting for laser to power on/warm up')
        
    close(description='Microbone to Turbo') 
    
    if analysis_type=='blank':  
        sleep(duration, message='Extracting gas')       
    else:
        info('starting extraction')    
        for po in position:
            do_extract(po)
        # for pi in position:
#             if isinstance(pi, str):
#                 if pi.startswith('d'):
#                     info('drill point: {}'.format(pi))
#                     drill_point(pi) 
#                 elif pi.startswith('l'):
#                     info('tracing path: {}'.format(pi))
#                     trace_path(pi) 
#                 else:
#                     do_extract(pi)
#             else:
#                 do_extract(pi)                
        
        disable()
        info('end extraction')
        
    sleep(cleanup,message="Cleaning gas")
    #=====================================================================================
    # continue to measurement_script
    #=====================================================================================
    
    

#=========================================================================================
# helper functions
#=========================================================================================
def do_extract(po):
    
    info('moving to position {}'.format(po))
    move_to_position(po)
    sleep(1)
    
    info('set extraction value to {} {}'.format(extract_value, extract_units))
    extract(extract_value, po)
    sleep(duration)
    
    if disable_between_positions:
        end_extract()
    info('end extraction for {}'.format(po))
    

#=========================================================================================
# EOF
#=========================================================================================