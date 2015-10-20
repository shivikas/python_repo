#!/usr/bin/python

f = open(r'/Users/user/Downloads/coho.txt', 'r')

list_tape = list((f.readline()).strip())
print list_tape

starting_offset_head = (f.readline()).strip()
print starting_offset_head

start_state_index = (f.readline()).strip()
print start_state_index
print repr(start_state_index)

halt_state_index = (f.readline()).strip()
print halt_state_index



def ReadActionTable(f):
    d1 = {}
    for line in f:
        splitLine = line.split()
        (a,b,c,d,e) = splitLine
        d1[(a,b)] = (c,d,e)
        return d1

def RunTuringMachine(actiontable, tape, head_pos, startindex):
    print 'inside RunTuringMachine' 
    run = True
    move = 0
    while run:
        (actiontable, tape, head_pos, startindex) = TuringMachine(actiontable, tape, head_pos, startindex)
        move += 1
        if (startindex == int(halt_state_index)):
            run = False
    
        
        

def TuringMachine(actiontable, tape, head_pos, startindex):
    print 'inside TuringMachine' 
    state_index = str(startindex)
    pos = int(head_pos)
    read = tape[pos]
    try:
        (write, dir, new_state_index) = actiontable[(state_index, read)]
        tape[pos] = write
        pos = pos + int(dir)
        return (actiontable, tape,pos,int(new_state_index))
    except:
        for tuple in actiontable:
            if tuple[1] == '*':
                (write, dir, new_state_index) = actiontable[tuple]
                tape[pos] = '-'
                pos = pos + int(dir)
                return (actiontable, tape, pos, int(new_state_index))
                
            
    
   
dict = ReadActionTable(f)
RunTuringMachine(dict, list_tape, starting_offset_head, int(start_state_index))
print list_tape
         

            
         
    
        

    