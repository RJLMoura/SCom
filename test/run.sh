#!/usr/bin/bash

# compile
zokrates compile --debug -i fleet.zok -o fleet && zokrates inspect -i fleet
# perform the setup phase
zokrates setup
# execute the program
zokrates compute-witness --verbose -i fleet -a 1 0 0 2 0 0 3 0 0 4 0 0 5 0 0  1 3 
# generate a proof of computation
zokrates generate-proof
# export a solidity verifier
zokrates export-verifier
# or verify natively
zokrates verify
