'''
mass spec equivalent
Message "Pumping Microbone"
DeviceRead "Pychron Extr Microcontroller" "GetValveState F" "ValveState"
If "ValveState" = "Close" then
    Open "CO2 Laser to Jan"
else
    Close "CO2 Laser to Jan"
end if
Close "CO2 Laser to Roughing"
Delay 1
Open "Microbone to Turbo"
Open "Microbone to Getter NP-10"
Open "Microbone to Getter D-50"
Open "Microbone to CO2 Laser"
Open "Microbone to Inlet Pipette"
Delay 1
DeviceWrite "Pychron Extr Microcontroller" "Set CO2PumpTimeFlag 30"
DeviceWrite "Pychron Extr microcontroller" "Set JanMiniboneFlag 0"
DeviceWrite "Pychron Extr Microcontroller" "Set JanCO2Flag 0"
'''
def main():
	info('Pump Microbone')
	if is_closed('F'):
		open(description=	'CO2 Laser to Jan')
	else:
		close(description=	'CO2 Laser to Jan')
	sleep(1)
	close(description=	'CO2 Laser to Roughing')
	open(description= 	'Microbone to Turbo')
	open(description= 	'Microbone to Getter NP-10')
	open(description= 	'Microbone to Getter D-50')
	open(description= 	'Microbone to CO2 Laser')
	open(description= 	'Microbone to Inlet Pipette')
	sleep(1)
	set_resource(name='CO2PumpTimeFlag', value=30)
	release('JanMiniboneFlag')	
	release('JanCO2Flag')