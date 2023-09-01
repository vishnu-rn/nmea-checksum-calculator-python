from time import perf_counter_ns


def validator(nmea_sentence: str | None = None):
    if nmea_sentence is not None:
        # Split the sentence and provided checksum value
        chk_str, chk_hex = nmea_sentence.split("*")
        # Convert the provided checksum into hex notation
        chk_hex = '0x' + chk_hex
        # Initialize a variable for byte-wise XOR of sentence characters
        chk_str_hex = 0
        # Remove the '$' at the beginning of each sentence
        for char in chk_str[1:]:
            chk_str_hex ^= ord(char)
        chk_str_hex = hex(chk_str_hex)

        if chk_str_hex == chk_hex:
            return True

    return False


if __name__ == '__main__':
    check_str = "$GPGGA,121315.00,0128.96496,F,02330.13368,L,1,08,0.94,31.7,M,-94.3,M,,*49"

    start = perf_counter_ns()
    result = validator(check_str)
    print(f'Validation returned {result.__str__().lower()} and the operation took {(perf_counter_ns() - start)/10e3} µs')
