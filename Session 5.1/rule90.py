from template import AbstractSimulation
import random

class rule90(AbstractSimulation):
    def __init__(self, number_of_steps):
        super().__init__(number_of_steps)
        self.iter = 0
    
    def initialize_sim(self):
        len_arr = random.randint(5, 10)
        print("Initializing 1d array, len {}.".format(len_arr))

        result = [True]*len_arr

        for i in range(len_arr):
            temp = random.random()

            if temp > 0.5:
                result[i] = False
        
        print("Array initialized, step 0: {}.".format(result))
        self.arr = result
    
    def run_one_step(self):
        '''
        Changes all values in array simultaneously using XOR, 2n memory :(
        '''

        temp_copy = self.arr

        for i in range(len(temp_copy)):
            if i == 0:
                self.arr[0] = (False != temp_copy[1])
            elif i == len(temp_copy)-1:
                self.arr[-1] = (temp_copy[-2] != False)
            else:
                self.arr[i] = (temp_copy[i-1] != temp_copy[i+1])
    
        self.iter += 1

    def print_sim_state(self):
        print("On step {}, arr looks like {}.".format(self.iter, self.arr))
        
if __name__ == "__main__":
    lets_see = rule90(10)
    lets_see.run()