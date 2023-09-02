# nmea-checksum-calculator-python
Calculates checksum of NMEA GPS data and outputs True or False, True if the calculated checksum matches checksum extracted from the NMEA Sentence.
The checksum is obtained simply by bytewise XOR of the charecters of the NMEA sentence excluding '$' and '*'.
