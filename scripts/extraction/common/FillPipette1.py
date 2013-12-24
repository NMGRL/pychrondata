'''
mass spec equivalent

Message "Fill Pipette 1"
Close "Outer Pipette 1"
Delay 1
If IsBlank then
    Message "NOT Filling air pipette 1--"
else
    Message "Filling air pipette 1--"
    Open "Inner Pipette 1"
    '---Filling air pipette
end if
BeginInterval 15
CompleteInterval
Close "Inner Pipette 1"    
Delay 1
'''
def main():
	info('Fill Pipette 1')
	close(description='Outer Pipette 1')
	sleep(1)
	info('analysis type {}'.format(analysis_type))
	if analysis_type=='blank':
		info('not filling air pipette')
	else:
		info('filling air pipette')
		open(description='Inner Pipette 1')
		
	sleep(15)
	close(description='Inner Pipette 1')
	sleep(1)