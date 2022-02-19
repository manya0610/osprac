import sys
from functions import getInput
from sjfnp import sjfnp
from sjfp import sjfp
from fcfs import fcfs
from rr import rr
from priority import priority

if __name__ == "__main__":
    while(True):
        choice = int(
            input(
                "Enter\n 1 for FCFS implementation\n 2 for SJF-NP implementation\n  3 for SJF-P implementation\n 4 for roundrobin\n 5 for priority\n 0 for exit\n"
            )
        )
        if choice not in [0,1, 2, 3, 4, 5 ]:
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
        elif choice == 5:
            priority()
        elif choice==0:
            sys.exit(-1)