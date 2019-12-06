import numpy as np
import pandas as pd
df = pd.read_csv(r"H:\AdventOfCode\input5.txt", header=None, sep=",")
int_input_base = df.values.tolist()[0]
input_value = 5
output_value = np.nan

int_input = int_input_base.copy()
i = 0
instruction_pointer_inc = 0

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
            int_input[int_input[i+1]] = input_value
        elif str_input[-3] == '1':
            int_input[i+1] = input_value
        instruction_pointer_inc = 2

    elif str_input[-2:] == '04':
        if str_input[-3] == '0':
            output_value = int_input[int_input[i+1]]
        elif str_input[-3] == '1':
            output_value = int_input[i+1]
        instruction_pointer_inc = 2
        print(output_value)

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
        break


    i += instruction_pointer_inc
print('Input value: ', input_value)
print('Output value: ', output_value)
print('eoc')