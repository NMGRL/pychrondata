def main():
    info('Evacuate Microbone')
    close(description='Jan Inlet')
    open(description='Jan Ion Pump')
    
    close(description='Minibone to Bone')
    close(description='Microbone to Minibone')
    close(description='Microbone to CO2 Laser')
    
    open(description='Microbone to Turbo')
    open(description='Microbone to Inlet Pipette')
    open(description='Microbone to Getter D-50')
    
    #evacuate apis section
    info('evacuate apis')
    open(description='Microbone to Getter NP-10')
    sleep(15)
    close(description='Microbone to Getter NP-10')