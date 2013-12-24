#!Extraction
def main():
    '''
        start at 0 zoom 
        focus
        
        take picture
        
        increment zoom
        take picture
        
        start at 100 zoom
        focus
        take picture....
        
    '''
    degas(brightness=10)    
        
    start_video_recording(run_identifier)
    
    set_motor('zoom',0)
    #autofocus(set_zoom=False)
    
    for i in range(10):
        set_motor('zoom',(i+1)*10)
        sleep(0.1)
        snapshot()
    
    set_motor('zoom',100)
    #autofocus(set_zoom=False)
    
    for i in range(10):
        set_motor('zoom',100-(i+1)*10)
        sleep(0.1)
        snapshot()
    stop_video_recording()
           
        
    