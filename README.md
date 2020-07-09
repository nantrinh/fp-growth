# FP-Growth
This is an implementation of the FP-Growth algorithm. I referred mainly to [this resource](https://wimleers.com/sites/wimleers.com/files/FP-Growth%20presentation%20handouts%20%E2%80%94%C2%A0Florian%20Verhein.pdf) for guidance.

Given a file where each row represents a transaction, the algorithm returns all groups of at least `min_length` items that were purchased together at least `min_support` times.

Each row consists of space-separated integers. Each integer represents an SKU.

`main.py` reads in `transactions.dat` and writes out all groups of 3 or more items that were purchased together at least 4 times. 

## How to run 
Run `python main.py`.
Results are written to `output.txt`.

Python version used: 3.8.2
