'''
mass spec equivalent

Gosub "Common Scripts:ConfigureErrors"
SetCanNumber 7
SetExtractionVolumeFraction "Pipette 2" 1
Message "Starting Air Pipette x1"
Gosub "Local scripts:WaitForMiniboneAccess"
Gosub "Local scripts:PrepareForAirShot"
Gosub "Local scripts:Evac Pipette 2"
Gosub "Common scripts:Fill Pipette 2"
Gosub "Local scripts:PrepareForAirShotExpansion"
'---expand shot 2
Gosub "Common scripts:Expand Pipette 2"
Close "Outer Pipette 2"
Delay 1
Gosub "Local scripts:EquilibrationMinibone"
Gosub "Local scripts:PumpAfterAir"
MeasureGas
Gosub "Common scripts:PumpMassSpec"
Message "Analysis complete"


'''
def main():
    #SetCanNumber 7
    #SetExtractionVolumeFraction "Pipette 2" 1
    info("Air Pipette x1")
    gosub('obama:WaitForMiniboneAccess')
    gosub('obama:PrepareForAirShot')
    gosub('common:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('obama:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')
    close(description='Outer Pipette 2')
    
    
