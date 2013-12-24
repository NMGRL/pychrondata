'''
mass spec equivalent
Gosub "Common Scripts:ConfigureErrors"
SetCanNumber 5
SetCanNumber 4
SetExtractionVolumeFraction "Pipette 2" 1
SetExtractionVolumeFraction "Pipette 1" 1
Message "Starting Air Pipette x1"
Message "Starting Cocktail Pipette x1"
Gosub "Local scripts:WaitForMiniboneAccess"
Gosub "Local scripts:PrepareForAirShot"
Gosub "Common Scripts:Evac Pipette 2 and 1"
Gosub "Common Scripts:Fill Pipette 2 and 1"
Gosub "Local scripts:PrepareForAirShotExpansion"
'---expand shot 2 and 1
Gosub "Common Scripts:Expand Pipette 2 and 1"
Close "Outer Pipette 2"
Close "Outer Pipette 1"
Delay 1
Gosub "Local scripts:EquilibrationMinibone"
Gosub "Local scripts:PumpAfterAir"
MeasureGas
Gosub "Common scripts:PumpMassSpec"
Message "Analysis complete"
'''
def main():
    info('Starting Mix script')
    gosub('obama:WaitForMiniboneAccess')
    gosub('obama:PrepareForAirShot')
    gosub('common:EvacPipette1_2')
    gosub('common:FillPipette1_2')
    gosub('obama:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette1_2')
    close(description='Outer Pipette 1')
    close(description='Outer Pipette 2')