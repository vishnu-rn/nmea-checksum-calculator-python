from time import perf_counter_ns


def validator(nmea_sentence: str | None = None):
    if not len(row) or row[0] != '$':
        return False

    chksum = 0x0
    splitRow = row.split('*')
    for c in splitRow[0]:
        if c == ',' or c == '$':
            continue
        else:
            # print(f'{bin(chksum)} ^ {bin(ord(c))} = {bin(chksum^ord(c))}')
            chksum ^= ord(c)
    if hex(chksum)[2:].upper() == splitRow[1]:
        return True
    # print(chksum)
    return False

if __name__ == '__main__':

    check_str = "$GPGGA,121315.00,0128.96496,F,02330.13368,L,1,08,0.94,31.7,M,-94.3,M,,*49"

    start = perf_counter_ns()
    result = validator(check_str)
    print(f'Validation returned {result.__str__().lower()} and the operation took {(perf_counter_ns() - start)/10e3} µs')
