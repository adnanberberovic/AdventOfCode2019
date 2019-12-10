import numpy as np
import pandas as pd
import itertools as it
df = pd.read_csv(r"H:\AdventOfCode\AdventOfCode2019\input9.txt", header=None, sep=",")
int_input_base = df.values.tolist()[0]

def modify_program_memory(int_input, index):
    for n in range(len(int_input), index+1):
        int_input.append(0)
    return(int_input)

def determine_index(int_input, i, mode, relative_base, di_counter):
    if mode == '0':
        index = int_input[i + di_counter]
    elif mode == '1':
        index = i + di_counter
    elif mode == '2':
        index = int_input[i + di_counter] + relative_base
    return index

def intcodecomputer(input_value, int_input, i = 0, input_value_counter = 0, save_state = False, relative_base = 0):
    instruction_pointer_inc = 0
    output_value = np.nan
    continue_loop = True
    do_output = False
    end_adress = len(int_input)
    while i <= end_adress:

        str_input = str(int_input[i])
        str_input = str_input.zfill(5)
        if str_input[-2:] == '01':
            first_pos = 0
            second_pos = 0

            if str_input[-3] == '0':
                index = int_input[i+1]
            elif str_input[-3] == '1':
                index = i+1
            elif str_input[-3] == '2':
                index = int_input[i+1] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            first_pos = int_input[index]

            if str_input[-4] == '0':
                index = int_input[i+2]
            elif str_input[-4] == '1':
                index = i+2
            elif str_input[-4] == '2':
                index = int_input[i+2] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            second_pos = int_input[index]

            if str_input[-5] == '0':
                index = int_input[i+3]
            elif str_input[-5] == '1':
                index = i+3
            elif str_input[-5] == '2':
                index = int_input[i+3] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            int_input[index] = first_pos + second_pos
            instruction_pointer_inc = 4

        elif str_input[-2:] == '02':
            first_pos = 0
            second_pos = 0

            if str_input[-3] == '0':
                index = int_input[i+1]
            elif str_input[-3] == '1':
                index = i+1
            elif str_input[-3] == '2':
                index = int_input[i+1] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            first_pos = int_input[index]

            if str_input[-4] == '0':
                index = int_input[i+2]
            elif str_input[-4] == '1':
                index = i+2
            elif str_input[-4] == '2':
                index = int_input[i+2] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            second_pos = int_input[index]

            if str_input[-5] == '0':
                index = int_input[i+3]
            elif str_input[-5] == '1':
                index = i+3
            elif str_input[-5] == '2':
                index = int_input[i+3] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            int_input[index] = first_pos * second_pos

            instruction_pointer_inc = 4

        elif str_input[-2:] == '03':
            if str_input[-3] == '0':
                index = int_input[i+1]
            elif str_input[-3] == '1':
                index = i+1
            elif str_input[-3] == '2':
                index = int_input[i+1] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            int_input[index] = input_value[input_value_counter]
                    
            instruction_pointer_inc = 2
            input_value_counter += 1
            if input_value_counter == len(int_input):
                input_value_counter = 0

        elif str_input[-2:] == '04':
            if str_input[-3] == '0':
                index = int_input[i+1]
            elif str_input[-3] == '1':
                index = i+1
            elif str_input[-3] == '2':
                index = int_input[i+1] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            output_value = int_input[index]
            instruction_pointer_inc = 2
            if save_state:
                do_output = True

        elif str_input[-2:] == '05':
            z_flag = False

            if str_input[-3] == '0':
                index = int_input[i+1]
            elif str_input[-3] == '1':
                index = i+1
            elif str_input[-3] == '2':
                index = int_input[i+1] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            z_flag = not int_input[index] != 0

            if str_input[-4] == '0':
                index = int_input[i+2]
            elif str_input[-4] == '1':
                index = i+2
            elif str_input[-4] == '2':
                index = int_input[i+2] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            if not z_flag:
                i = int_input[index]
                instruction_pointer_inc = 0
            else:
                instruction_pointer_inc = 3
            
        elif str_input[-2:] == '06':
            z_flag = False

            if str_input[-3] == '0':
                index = int_input[i+1]
            elif str_input[-3] == '1':
                index = i+1
            elif str_input[-3] == '2':
                index = int_input[i+1] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            z_flag = not int_input[index] != 0

            if str_input[-4] == '0':
                index = int_input[i+2]
            elif str_input[-4] == '1':
                index = i+2
            elif str_input[-4] == '2':
                index = int_input[i+2] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)
                
            if z_flag:
                i = int_input[index]
                instruction_pointer_inc = 0
            else:
                instruction_pointer_inc = 3

        elif str_input[-2:] == '07':
            first_param = 0
            second_param = 0
            z_flag = False

            if str_input[-3] == '0':
                index = int_input[i+1]
            elif str_input[-3] == '1':
                index = i+1
            elif str_input[-3] == '2':
                index = int_input[i+1] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            first_param = int_input[index]

            if str_input[-4] == '0':
                index = int_input[i+2]
            elif str_input[-4] == '1':
                index = i+2
            elif str_input[-4] == '2':
                index = int_input[i+2] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            second_param = int_input[index]

            z_flag = first_param < second_param
            
            if str_input[-5] == '0':
                index = int_input[i+3]
            elif str_input[-5] == '1':
                index = i+3
            elif str_input[-5] == '2':
                index = int_input[i+3] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            if z_flag:
                int_input[index] = 1
            else:
                int_input[index] = 0

            instruction_pointer_inc = 4

        elif str_input[-2:] == '08':        
            first_param = 0
            second_param = 0
            z_flag = False

            if str_input[-3] == '0':
                index = int_input[i+1]
            elif str_input[-3] == '1':
                index = i+1
            elif str_input[-3] == '2':
                index = int_input[i+1] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            first_param = int_input[index]

            if str_input[-4] == '0':
                index = int_input[i+2]
            elif str_input[-4] == '1':
                index = i+2
            elif str_input[-4] == '2':
                index = int_input[i+2] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            second_param = int_input[index]

            z_flag = first_param == second_param
            
            if str_input[-5] == '0':
                index = int_input[i+3]
            elif str_input[-5] == '1':
                index = i+3
            elif str_input[-5] == '2':
                index = int_input[i+3] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)
            
            if z_flag:
                int_input[index] = 1
            else:
                int_input[index] = 0

            instruction_pointer_inc = 4
        
        elif str_input[-2:] == '09':
            if str_input[-3] == '0':
                index = int_input[i+1]
            elif str_input[-3] == '1':
                index = i+1
            elif str_input[-3] == '2':
                index = int_input[i+1] + relative_base
            if index >= len(int_input):
                int_input = modify_program_memory(int_input, index)

            relative_base += int_input[index]
                
            instruction_pointer_inc = 2
            
        elif str_input[-2:] == '99':
            continue_loop = False
            break
        
        i += instruction_pointer_inc
        end_adress = len(int_input)
        if do_output:
            break
    return [output_value, continue_loop, i, input_value_counter]

input_value = [1]
int_input = int_input_base.copy()
boost_keycode = intcodecomputer(input_value, int_input)[0]
print('BOOST Keycode: ', boost_keycode)

input_value = [2]
int_input = int_input_base.copy()
coordinates = intcodecomputer(input_value, int_input)[0]
print('Coordinates: ', coordinates)