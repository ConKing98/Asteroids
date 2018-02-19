from platform import system

def save(score):
    """
    Used write all highscores to the highscore.txt file which is referenced in load()
    whenever the highscore_label is called in main.py. Only the top ten highscores 
    are saved.

    Inputs
    =================================================================================
    Score       str; the player's score, a property of the Player class.

    Outputs
    =================================================================================
    None
    """
    # Defining all variables that must persist through the for loops
    global old_line, new_lines, old_data, lines_of_note
    old_line = ''
    new_lines = []
    lines_of_note = []
    # Conditions to deal with file path naming conventions
    if system() == 'Windows':
        file_path = "game\\save_data\\highscores.txt"
    elif system() == 'Darwin' or system() == 'Linux':
        file_path = "game/save_data/highscores.txt"
    else:
        raise Exception('Unknown Operating System.')
    # Opening the highscore file in read only and managing the data
    with open(file_path, 'r') as score_file:
        score_file_lines = score_file.readlines()
        old_data = []
        # Used to determine if the player's score is in the top ten
        for file_line in score_file_lines:
            value = float(file_line.rstrip())
            if value >= score:
                pass
            else:
                lines_of_note.append(file_line)
        # Condition to exit save() if the score is not high enough
        if len(lines_of_note) == 0:
            return
        else:
            # Determining where the score will fit in and the resulting cascade
            for line in lines_of_note:
                # Condition for first time through for loop after save() is called
                if old_line == '':
                    old_line = line
                    old_data.append([score, old_line])
                    continue
                else:
                    old_data.append([old_line, line])
                    old_line = line
                    continue
            # Determining index where new score will be located in highscores.txt
            new_score_index = score_file_lines.index(old_data[0][1])
            # Removing any previous highscores if the total number of highscores exceeds 10
            if new_score_index + len(old_data) > 10:
                del(old_data[-1])
            # Looping through all 10 scores that will be included
            for line in range(10):
                # Scores greater than the new highscore
                if line < new_score_index:
                    new_lines.append(score_file_lines[line].rstrip().partition('.')[0]+'\n')
                    continue
                # The new highscore and all lower scores that remained
                else:
                    if line != 9:
                        new_lines.append(str(old_data[line-new_score_index][0]).partition('.')[0]+'\n')
                        continue
                    # Condition to not add new line string tag for lowest score
                    else:
                        new_lines.append(str(old_data[line-new_score_index][0]).partition('.')[0])
                        continue
    # Reopening file to write it over with the new data asved in new_line
    with open(file_path, 'w') as score_file:
        score_file.writelines(new_lines)
        return
            
def load():
    """
    Used to get back all highscores saved in highscores.txt


    Inputs
    ======================================================================
    None

    Outputs
    ======================================================================
    None
    """
    # Conditions to deal with file path naming conventions
    if system() == 'Windows':
        file_path = "game\\save_data\\highscores.txt"
    elif system() == 'Darwin':
        file_path = "game/save_data/highscores.txt"
    else:
        raise Exception('Unknown Operating System.') 
    with open(file_path, 'r') as score_file:
        data = score_file.readlines()
        return(data)
