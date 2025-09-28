#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from code_master.crew import Coder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

assignment = (
    "Write a Python program to generate the first 500 prime numbers "
    "using an efficient algorithm (not simple trial division). "
    "Store them in a list, then calculate and print: "
    "1) the sum of all primes, "
    "2) the largest prime, "
    "3) the average of the primes, "
    "and 4) how many of them are twin primes. "
    "Make sure the program runs efficiently."
)

def run():
    """
    Run the crew.
    """
    inputs = {
        'assignment': assignment,
    }
    
    result = Coder().crew().kickoff(inputs=inputs)
    print(result.raw)




