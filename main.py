import sys
from functions import getInput
from sjfnp import sjfnp
from sjfp import sjfp
from fcfs import fcfs
from rr import rr

if __name__ == "__main__":
    choice = int(
        input(
            "Enter 1 for FCFS implementation, 2 for SJF-NP implementation, and 3 for SJF-P implementation, 4 for roundrobin\n"
        )
    )
    if choice not in [1, 2, 3,4]:
        print("Invalid choice!!")
        sys.exit(-1)
    if choice == 1:
        impl = "FCFS"
        fcfs()
    elif choice == 2:
        sjfnp()
        
    elif choice == 3:
        sjfp()
    
    elif choice == 4:
        rr()