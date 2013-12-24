'''
Message "Fill Pipette 2"
Message "Fill Pipette 1"
Close "Outer Pipette 2"
Close "Outer Pipette 1"
Delay 1
If IsBlank then
    Message "NOT Filling air pipette 2--"
else
    Message "Filling air pipette 2--"
    Open "Inner Pipette 2"
    Open "Inner Pipette 1"
'---Filling  pipettes
end if
BeginInterval 15
CompleteInterval
Close "Inner Pipette 2"
Close "Inner Pipette 1"
Delay 1
'''

def main():
    info('Fill Pipettes 1 and 2')
    close(description='Outer Pipette 1')
    close(description='Outer Pipette 2')
    sleep(1)
    if analysis_type=='blank':
        info('Not filling pipettes')
    else:
        info('filling pipettes')
        open(description='Inner Pipette 1')
        open(description='Inner Pipette 2')
    sleep(15)
    close(description='Inner Pipette 1')
    close(description='Inner Pipette 2')