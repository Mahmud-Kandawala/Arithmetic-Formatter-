import re  


def arithmetic_arranger(problems, solve=False):

    
    if len(problems) > 5:
        return "Error: Too many problems."

    
    top_line = ""
    bottom_line = ""
    dash_line = ""
    result_line = ""

    
    for problem in problems:
        
        if re.search("[^\s\d.+-]", problem):
            if re.search("[/*]", problem):
                return "Error: Operator must be '+' or '-'."
            else:
                return "Error: Numbers must only contain digits."

        
        first_number = problem.split()[0]
        operator = problem.split()[1]
        second_number = problem.split()[2]

        
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        
        sum = ""
        if operator == "+":
            sum = int(first_number) + int(second_number)
        elif operator == "-":
            sum = int(first_number) - int(second_number)

        
        line_length = max(len(first_number), len(second_number)) + 2
        
        top = str(first_number).rjust(line_length)
        bottom = operator + str(second_number).rjust(line_length - 1)
        result = str(sum).rjust(line_length)
        
        dashes = ""
        for i in range(line_length):
            dashes += "-"

        
        if problem != problems[-1]:
            top_line += top + "    "
            bottom_line += bottom + "    "
            dash_line += dashes + "    "
            result_line += result + "    "
        
        else:
            top_line += top
            bottom_line += bottom
            dash_line += dashes
            result_line += result

   
    if solve is True:
        arranged = top_line + "\n" + bottom_line + "\n" + dash_line + "\n" + result_line
    else:
        arranged = top_line + "\n" + bottom_line + "\n" + dash_line
    
    return arranged
