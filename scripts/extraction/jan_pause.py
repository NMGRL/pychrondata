'''
eqtime: 5
'''


def main():
    
    info('pause script')
    begin_interval(duration)
    sleep(duration/2.0)
    
    complete_interval()
    
    gosub('jan:PrepareForAirShot')
    #gosub('jan:WaitForMiniboneAccess')