def main():
	info('Pump Bone')
	if is_closed('A'):
		open(description='CO2 Laser to Obama')
	else:
		close(description='CO2 Laser to Obama')
	sleep(1)
	close(description='CO2 Laser to Roughing')
	open(description='Bone to Turbo')
	open(description='Bone to Getter GP-50')
	open(description='Bone to Diode Laser')
	open(description='Bone to CO2 Laser')
	sleep(1)
	set_resource(name='CO2PumpTimeFlag', value=30)
	release('ObamaCO2Flag')