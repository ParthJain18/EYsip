import re

def remove_unsupported_chars(text):
    pattern = r'[^\x20-\x7E]' 
    return re.sub(pattern, '', text)

with open("log_parallel_team_1.txt") as file:
    lines = [line for line in file if line.strip() != ""]
    new_lines = []
    for line in lines:
        temp = line.split(',')

        if len(temp) != 2:
            continue
        
        line = remove_unsupported_chars(line)
        print(line)
        new_lines.append(line + '\n')

    with open("seconds_logs.csv", "w") as file2:
        file2.writelines(new_lines)
