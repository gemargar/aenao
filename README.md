# Weight Sensor Integration

The goal is to intercept the analog input of the ORCA's weight sensor from the PLC to the Raspberry Pi. This is done by interposing and external ADC to read the analog voltage and translate it to weight on the Raspberry Pi.

The original code can be found [here.](https://hardsoftlucid.wordpress.com/various-stuff/realtime-plotting/)