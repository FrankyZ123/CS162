class generators:
    def __init__(self):
        self.generators = {'randU' : randU, 
                           'Mersenne' : Mersenne}

from datetime import datetime
seed = int((datetime.utcnow() - datetime.min).total_seconds())

class Mersenne:
    @staticmethod
    def random_int():
        #!/usr/bin/env python2
        # -*- coding: utf-8 -*-
        """
        Based on the pseudocode in https://en.wikipedia.org/wiki/Mersenne_Twister.

        Generates uniformly distributed 32-bit integers in the range [0, 2^32 − 1] with
        the MT19937 algorithm

        Yaşar Arabacı <yasar11732 et gmail nokta com>
        Modified by Philip Sterne <psterne at minervaproject dot com>
        """


        # Global constants that will never change:
        bitmask_1 = (2**32) - 1  # To get last 32 bits
        bitmask_2 = 2**31  # To get 32nd bit
        bitmask_3 = (2**31) - 1  # To get last 31 bits

        import gettext

        def initialize_generator(seed):
            "Initialize the generator from a seed"
            # Create a length 624 list to store the state of the generator
            MT = [0 for i in range(624)]
            index = 0
            MT[0] = seed
            for i in range(1, 624):
                MT[i] = ((1812433253 * MT[i - 1]) ^ (
                    (MT[i - 1] >> 30) + i)) & bitmask_1
            return (MT, index)


        def generate_numbers(MT):
            "Generate an array of 624 untempered numbers"
            for i in range(624):
                y = (MT[i] & bitmask_2) + (MT[(i + 1) % 624] & bitmask_3)
                MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
                if y % 2 != 0:
                    MT[i] ^= 2567483615
            return MT


        def extract_number(MT, index):
            """
            Extract a tempered pseudorandom number based on the index-th value,
            calling generate_numbers() every 624 numbers
            """
            if index == 0:
                MT = generate_numbers(MT)
            y = MT[index]
            y ^= y >> 11
            y ^= (y << 7) & 2636928640
            y ^= (y << 15) & 4022730752
            y ^= y >> 18

            index = (index + 1) % 624
            return (MT, index, y)
        
        (MT, index) = initialize_generator(seed)
        (MT, index, y) = extract_number(MT, index)
        return y

class randU:
    @staticmethod
    def random_int():
        # Modify the code here for abstraction.
        # ------------------------------------------------------
        from datetime import datetime
        # randU initiation
        x = int((datetime.utcnow() - datetime.min).total_seconds())
        # Constants given by the RANDU algorithm:
        # https://en.wikipedia.org/wiki/RANDU
        c = 65539
        m = 2147483648
        # ------------------------------------------------------
        return abs((c * x) % m)