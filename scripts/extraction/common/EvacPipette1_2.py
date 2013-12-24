'''
mass spec equivalent
Message "Evac Pipette 2"
Open "Minibone to Turbo"
Open "Minibone to bone"
Close "Inner Pipette 2"
Close "Inner Pipette 1"
Delay 1
Open "Outer Pipette 2"
Open "Outer Pipette 1"
'---Evacuating air pipette
Message "Evacuating  pipettes--"
BeginInterval 15
CompleteInterval
'''

def main():
    info('Evacuate Pipettes 1 and 2')
    open(description='Minibone to Turbo')
    open(description='Minibone to Bone')
    close(description='Inner Pipette 1')
    close(description='Inner Pipette 2')
    sleep(1)
    open(description='Outer Pipette 1')
    open(description='Outer Pipette 2')
    sleep(15)