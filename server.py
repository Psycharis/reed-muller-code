from random import randrange

from sage.all import *
from sage.coding.reed_muller_code import BinaryReedMullerCode
from sage.coding.reed_muller_code import ReedMullerVectorEncoder

if __name__ == "__main__":

    while True:

        r = int(raw_input("Give reed-muller's order: "))
        m = int(raw_input("Give reed-muller's code length: "))

        if (m >= r and m >= 0 and r >= 0):
            break
        else:
            print "Your input is invalid!"

    RM = codes.BinaryReedMullerCode(r, m) # initialize reed-muller code
    ENCODER = codes.encoders.ReedMullerVectorEncoder(RM) # initialize vector encoder
    RM_MATRIX = ENCODER.generator_matrix() # generate vector matrix

    print "** minimum distance: " + str(RM.minimum_distance())
    print "** number of variables: " + str(RM.number_of_variables())

    w2s = [] # w2s = words to send
    encoded_w2s = [] # encoded words to send

    # create 20 random words
    for i in range(0, 19):
        pre_vector_array = [] # initialize empty array

        for i in range(0, RM.dimension()):
            pre_vector_array.append(randrange(0,2)) # create random bits in single array

        w2s.append(vector(pre_vector_array)) # append array as vector in w2s

    # encode w2s
    for i in range(0, 19):
        encoded_w2s.append(w2s[i]*RM_MATRIX)

    # show results
    for i in range(0, 19):
        print str(w2s[i]) + " => " + str(encoded_w2s[i])