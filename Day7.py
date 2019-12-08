import numpy as np
import pandas as pd
import itertools as it
df = pd.read_csv(r"C:\Users\Adnan\Dropbox\Documents\Projects\AdventOfCode\AdventOfCode2019\input7.txt", header=None, sep=",")
int_input_base = df.values.tolist()[0]

def intcodecomputer(input_value, int_input, i = 0, input_value_counter = 0):
    instruction_pointer_inc = 0
    output_value = np.nan
    continue_loop = True
    do_output = False
    while i <= len(int_input):

        str_input = str(int_input[i])
        str_input = str_input.zfill(5)

        if str_input[-2:] == '01':
            first_pos = 0
            second_pos = 0

            if str_input[-3] == '0':
                first_pos = int_input[int_input[i+1]]
            elif str_input[-3] == '1':
                first_pos = int_input[i+1]
            if str_input[-4] == '0':
                second_pos = int_input[int_input[i+2]]
            elif str_input[-4] == '1':
                second_pos = int_input[i+2]
            int_input[int_input[i+3]] = first_pos + second_pos
            instruction_pointer_inc = 4

        elif str_input[-2:] == '02':
            first_pos = 0
            second_pos = 0

            if str_input[-3] == '0':
                first_pos = int_input[int_input[i+1]]
            elif str_input[-3] == '1':
                first_pos = int_input[i+1]
            if str_input[-4] == '0':
                second_pos = int_input[int_input[i+2]]
            elif str_input[-4] == '1':
                second_pos = int_input[i+2]
            int_input[int_input[i+3]] = first_pos * second_pos
            instruction_pointer_inc = 4

        elif str_input[-2:] == '03':
            if str_input[-3] == '0':
                int_input[int_input[i+1]] = input_value[input_value_counter]
            elif str_input[-3] == '1':
                int_input[i+1] = input_value[input_value_counter]
            instruction_pointer_inc = 2
            input_value_counter += 1          

        elif str_input[-2:] == '04':
            if str_input[-3] == '0':
                output_value = int_input[int_input[i+1]]
            elif str_input[-3] == '1':
                output_value = int_input[i+1]
            instruction_pointer_inc = 2
            do_output = True

        elif str_input[-2:] == '05':
            z_flag = False

            if str_input[-3] == '0':
                z_flag = not int_input[int_input[i+1]] != 0
            elif str_input[-3] == '1':
                z_flag = not int_input[i+1] != 0

            if str_input[-4] == '0':
                if not z_flag:
                    i = int_input[int_input[i+2]]
                    instruction_pointer_inc = 0
                else:
                    instruction_pointer_inc = 3
            elif str_input[-4] == '1':
                if not z_flag:
                    i = int_input[i+2]
                    instruction_pointer_inc = 0
                else:
                    instruction_pointer_inc = 3
            
        elif str_input[-2:] == '06':
            z_flag = False

            if str_input[-3] == '0':
                z_flag = not int_input[int_input[i+1]] != 0
            elif str_input[-3] == '1':
                z_flag = not int_input[i+1] != 0

            if str_input[-4] == '0':
                if z_flag:
                    i = int_input[int_input[i+2]]
                    instruction_pointer_inc = 0
                else:
                    instruction_pointer_inc = 3
            elif str_input[-4] == '1':
                if z_flag:
                    i = int_input[i+2]
                    instruction_pointer_inc = 0
                else:
                    instruction_pointer_inc = 3

        elif str_input[-2:] == '07':
            first_param = 0
            second_param = 0
            z_flag = False
            if str_input[-3] == '0':
                first_param = int_input[int_input[i+1]]
            elif str_input[-3] == '1':
                first_param = int_input[i+1]
            if str_input[-4] == '0':
                second_param = int_input[int_input[i+2]]
            elif str_input[-4] == '1':
                second_param = int_input[i+2]
            z_flag = first_param < second_param
            
            if str_input[-5] == '0':
                if z_flag:
                    int_input[int_input[i+3]] = 1
                else:
                    int_input[int_input[i+3]] = 0
            if str_input[-5] == '1':
                if z_flag:
                    int_input[i+3] = 1
                else:
                    int_input[i+3] = 0
            instruction_pointer_inc = 4

        elif str_input[-2:] == '08':        
            first_param = 0
            second_param = 0
            z_flag = False
            if str_input[-3] == '0':
                first_param = int_input[int_input[i+1]]
            elif str_input[-3] == '1':
                first_param = int_input[i+1]
            if str_input[-4] == '0':
                second_param = int_input[int_input[i+2]]
            elif str_input[-4] == '1':
                second_param = int_input[i+2]
            z_flag = first_param == second_param
            
            if str_input[-5] == '0':
                if z_flag:
                    int_input[int_input[i+3]] = 1
                else:
                    int_input[int_input[i+3]] = 0
            if str_input[-5] == '1':
                if z_flag:
                    int_input[i+3] = 1
                else:
                    int_input[i+3] = 0
            instruction_pointer_inc = 4
            
        elif str_input[-2:] == '99':
            continue_loop = False
            break
            
        i += instruction_pointer_inc
        if do_output:
            break
    return [output_value, continue_loop, i, input_value_counter]

phase_setting_combinations = list(it.permutations(range(5, 10), 5))
maximum_output = 0

for phase_setting in phase_setting_combinations:    
    int_codes = [int_input_base.copy()]*len(phase_setting)
    phase_setting_output = 0
    iters = [0]*len(phase_setting)
    ivc = [0]*len(phase_setting)
    inputs = []
    for phase in phase_setting:
        inputs.append([phase])

    while True:
        output = [0] * len(int_codes)
        for i, amp in enumerate(int_codes):
            inputs[i].append(phase_setting_output)
            output[i] = intcodecomputer(inputs[i], amp, iters[i], ivc[i])
            iters[i] = output[i][2]
            ivc[i] = output[i][3]
            phase_setting_output = output[i][0]

        if not output[len(output)-1][1]:
            phase_setting_output = inputs[0][len(inputs[0])-1]
            break
    if phase_setting_output > maximum_output:
        maximum_output = phase_setting_output

print('Maximum thrust: ', maximum_output)
