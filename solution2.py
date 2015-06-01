from math import ceil


def add(n, k):
    while n < 0:
        n += k
    return n


def decode(message):
    length = ceil(len(message) / 2)
    message = message[length:] + message[:length]
    msg = message.split('~')
    alphabet_length = int(msg[0])
    alphabet = msg[1][:alphabet_length]
    key_length = int(msg[2])
    key = msg[1][-key_length:]
    encripted = msg[1][alphabet_length:-key_length]
    encripted_indexes = [alphabet.index(c) for c in encripted]
    l = len(encripted_indexes)
    key = (key * (l // key_length + 1))[:l]
    key_indexes = [alphabet.index(c) for c in key]
    result_indexes = [add(x - y, alphabet_length) for x, y in
                      zip(encripted_indexes, key_indexes)]
    message = [alphabet[index] for index in result_indexes]
    print (''.join(message))
    return ''.join(message)
