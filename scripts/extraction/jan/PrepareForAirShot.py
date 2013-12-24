def main():
    info('Prepare for Air Shot')
    close(description='Jan Inlet')
    open(description='Jan Ion Pump')
    close(description='Minibone to Bone')
    close(description='Quad Inlet')
    open(description='Microbone to Turbo')
    close(description='Microbone to Minibone')
    open(description='Microbone to Inlet Pipette')
    open(description='Microbone to Getter D-50')
    open(description='Microbone to Getter NP-10')
    close(description='Microbone to CO2 Laser')

    open(name="G", description="CO2 Laser to Roughing")