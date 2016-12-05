def rescaleTime(dialogs):
    
    time_scaled_dialogs = {}
    
    for character in dialogs.keys():
        abs_lines, speeches = zip(*dialogs[character])
        first_line = min(abs_lines)
        last_line = max(abs_lines)
        scaled_lines = map(lambda x: (x - float(first_line))/(last_line - first_line), abs_lines)  
        time_scaled_dialogs[character] = zip(scaled_lines, speeches)
    
    return time_scaled_dialogs