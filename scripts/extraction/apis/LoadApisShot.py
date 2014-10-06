def main(shot_name):
     # load air shot behind Microbone to Getter NP-10
    info('extracting {}'.format(shot_name)
    #for testing just sleep a few seconds
    sleep(5)
    # this action blocks until completed
    #extract_pipette(shot_name)
    
    #isolate microbone
    close(description='Microbone to Turbo')

    #delay to ensure valve is closed and air shot not factionated
    sleep(2)
    
    #expand air shot to microbone
    open(description='Microbone to Getter NP-10')
    sleep(15)
    
    #isolate microbone ?
    close(description='Microbone to Getter NP-10')
    
    