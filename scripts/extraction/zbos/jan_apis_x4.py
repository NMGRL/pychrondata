'''
sensitivity_multiplier: 0.5
modifier: 4
'''
def main():
    info('Jan Air Script')
    #gosub('jan:WaitForMiniboneAccess')
    #gosub('jan:PrepareForAirShot')
    #gosub('jan:EvacPipette2')
    #gosub('common:FillPipette2')

    extract_pipette('Air1')
    
    gosub('jan:PrepareForAirShotExpansion')
    #gosub('common:ExpandPipette2')
    #close(description='Outer Pipette 2')