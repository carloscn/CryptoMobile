# −*− coding: UTF−8 −*−
# python3

def pstr_to_carray(array, name):
    print('______________________________')
    print(array)
    print('covert c_alg: \n')
    print('uint8_t *', end='')
    print(name, end='')
    print(' =\n{\n')
    for i in range(1, len(array)+1):
        if (i == len(array)):
            print('0x%x' %array[i-1])
        else:
            print('0x%x,' %array[i-1] , end='')
        if (i % 8 == 0):
            print("")

    print('};')
    print('input str len: %d bits' % (len(array) * 8))
    print('______________________________')

if __name__ == '__main__':
    key     = b'\xfd\xb9\xcf\xdf(\x93l\xc4\x83\xa3\x18i\xd8\x1b\x8f\xab'
    name_str = "key"
    pstr_to_carray(key, name_str)
    key = b'+\xd6E\x9f\x82\xc5\xb3\x00\x95,I\x10H\x81\xffH'
    pstr_to_carray(key, name_str)
    key = b'\xef\xa8\xb2"\x9er\x0c*|6\xeaU\xe9`V\x95'
    pstr_to_carray(key, name_str)
    key = b'Z\xcb\x1ddL\rQ N\xa5\xf1E\x10\x10\xd8R'
    pstr_to_carray(key, name_str)
    key = b'\xd3\xc5\xd5\x922\x7f\xb1\x1c@5\xc6h\n\xf8\xc6\xd1'
    pstr_to_carray(key, name_str)
    key = b'`\x90\xea\xe0L\x83pn\xec\xbfe+\xe8\xe3ef'
    pstr_to_carray(key, name_str)
    data = b"\x10\x11\x121\xe0`%:C\xfd?W\xe3v\x07\xab('\xb5\x99\xb6\xb1\xbb\xda7\xa8\xab\xccZ\x8cU\r\x1b\xfb/IF$\xfbP6\x7f\xa3l\xe3\xbch\xf1\x1c\xf9;\x15\x107k\x02\x13\x0f\x81*\x9f\xa1i\xd8"
    pstr_to_carray(data, "data")