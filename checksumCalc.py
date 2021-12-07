def checksum_crosscheck(check_string, verbose=False):
    if check_string[0] != "$":
        return None
    else:
        string_to_check = []
        check_str_end = check_string.find("*")
        checksum_input = hex(int('0x' + check_string[check_str_end + 1 :], 16))
        calc_checksum = 0

        for charecter in check_string[1:]:
            if charecter == "*":
                break
            else:
                string_to_check.append(charecter)

    string_to_check[:] = (x for x in string_to_check if x != ',')


    for each in string_to_check:
        calc_checksum ^= ord(each)
    
    calc_checksum = hex(calc_checksum)
    if verbose:
        print(f'Input checksum = {checksum_input}, Calculated checksum = {calc_checksum}')

    if checksum_input == calc_checksum:
        return True
    else:
        return False


if __name__ == '__main__':
    
    check_str = "$GPGGA,121315.00,0128.96496,F,02330.13368,L,1,08,0.94,31.7,M,-94.3,M,,*49"
    print(checksum_crosscheck(check_str, verbose=True))
