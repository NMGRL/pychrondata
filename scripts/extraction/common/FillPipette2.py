'''
mass spec equivalent

Message "Fill Pipette 2"
Close "Outer Pipette 2"
Delay 1
If IsBlank then
    Message "NOT Filling air pipette 2--"
else
    Message "Filling air pipette 2--"
    Open "Inner Pipette 2"
    '---Filling air pipette
end if
BeginInterval 15
CompleteInterval
Close "Inner Pipette 2"    
Delay 1
'''
def main():
	info('Fill Pipette 2')
	close(description='Outer Pipette 2')
	sleep(1)
	info('analysis type {}'.format(analysis_type))
	if analysis_type=='blank':
		info('not filling air pipette')
	else:
		info('filling air pipette')
		open(description='Inner Pipette 2')
		
	sleep(15)
	close(description='Inner Pipette 2')
	sleep(1)