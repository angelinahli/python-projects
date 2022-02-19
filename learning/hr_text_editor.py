"""
Date: 2022.02.19
Name: Angelina Li
Desc: Passing Python3 solution to 
      https://www.hackerrank.com/challenges/simple-text-editor/problem

Operations:
- 1 W: append 'W' to end of S
- 2 k: Delete last K-th chars of S
- 3 k: Print K-th char of S
- 4: Undo last operation of type 1 or 2, reverting S back to prev state

Assumptions:
- Operations as given are possible.
"""

import sys

def run():
    ## state stack: last elt of state is always current state of S
    state = [""]
    cur = state[-1]
    
    num_ops = int(input())
    for _ in range(num_ops):
        input_line = input()
        op = input_line[0]
        ## silently returns '' for op 4
        param = input_line[2:]
        
        ## process the operation
        if op == "1":
            new_state = cur + param
            state.append(new_state)
            cur = new_state
        elif op == "2":
            new_str_len = len(cur) - int(param)
            new_state = cur[:new_str_len]
            state.append(new_state)
            cur = new_state
        elif op == "3":
            ## this operation doesn't change the state at all
            index = int(param) - 1
            sys.stdout.write(cur[index] + "\n")
        elif op == "4":
            ## get rid of the last operation
            state.pop()
            cur = state[-1]
        
if __name__ == "__main__":
    run()
