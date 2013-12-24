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
    info("Cocktail Pipette x1")
    #gosub('obama:WaitForMiniboneAccess')
    #gosub('obama:PrepareForCocktailShot')
    #gosub('common:EvacPipette1')
    #gosub('common:FillPipette1')
    #gosub('obama:PrepareForCocktailShotExpansion')
    #gosub('common:ExpandPipette1')
    #close(description='Outer Pipette 1')
    
    
