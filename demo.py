import numpy as np
from qecsim import paulitools as pt
from qecsim.models.generic import DepolarizingErrorModel
from qecsim.models.toric import ToricCode, ToricMWPMDecoder

# initialise models
my_code = ToricCode(5, 5)
my_error_model = DepolarizingErrorModel()
my_decoder = ToricMWPMDecoder()
# print models
print(my_code)
print(my_error_model)
print(my_decoder)

# set physical error probability to 10%
error_probability = 0.1
# seed random number generator for repeatability
rng = np.random.default_rng(59)

# error: random error based on error probability
error = my_error_model.generate(my_code, error_probability, rng)
qsu.print_pauli('error:\n{}'.format(my_code.new_pauli(error)))

# syndrome: stabilizers that do not commute with the error
syndrome = pt.bsp(error, my_code.stabilizers.T)
qsu.print_pauli('syndrome:\n{}'.format(my_code.ascii_art(syndrome)))

# recovery: best match recovery operation based on decoder
recovery = my_decoder.decode(my_code, syndrome)
qsu.print_pauli('recovery:\n{}'.format(my_code.new_pauli(recovery)))

# print recovery ^ error (out of curiosity)
qsu.print_pauli('recovery ^ error:\n{}'.format(my_code.new_pauli(recovery ^ error)))