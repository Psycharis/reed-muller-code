# Echo server program
import socket

import pickle
from sage.all import *
from sage.coding.reed_muller_code import BinaryReedMullerCode
from sage.coding.reed_muller_code import ReedMullerVectorEncoder
from sage.coding.linear_code import LinearCodeSyndromeDecoder

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50017              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Message by', addr

while 1:
    recvd_data = conn.recv(8192)
    if not recvd_data: break

    data = pickle.loads(recvd_data)

    conn.sendall(recvd_data)

r = data[20] # 'r' order value
m = data[21] # 'm' code lenght value


RM = codes.BinaryReedMullerCode(r, m) # initialize reed-muller code
RM2 = codes.decoders.LinearCodeNearestNeighborDecoder(RM)

max_errors = RM2.decoding_radius() # maximal number of errors that can be decode.
print data[0]
try:

    flag = true
    check = 0
    for i in range(0, 20):
        word = RM.syndrome(data[i])
        for y in range(0, len(word)):
            if word[y]:
                check += 1
        if check > max_errors:
            flag = false
            print word
            break
        check = 0

    unencode_w2s = []
    print

    if flag: # if message can be decode
        print "The message is:"
        for i in range(0, 20):
            E2 = RM2.decode_to_message(data[i]) # decode the encoded message
            unencode_w2s.append(E2)
            print str(unencode_w2s[i])
    else:
        print "The code is not understandable due to errors"
except:
    print "The code is not understandable due to errors"


conn.close()
