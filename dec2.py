

def calculate_score_one(path: str) -> int:
    #Score bonus for using each 
    shape_scores: dict[str, int] = {"X": 1, "Y": 2, "Z": 3}
    
    # Key beats value "Rock beats scissors", etc
    win_conditions: dict[str, str] = {'C': 'X', 'A': 'Y', 'B': 'Z'}
    draw_conditions: dict[str, str] = {'A': 'X', 'B': 'Y', 'C': 'Z'}

    win_bonus: int = 6
    draw_bonus: int = 3

    tournament_score: int = 0
    with open(path, 'r') as f:
        for line in f.readlines():
            played_shape: str = line.removesuffix('\n')[-1]
            print(played_shape)
            line_score: int = 0
            if win_conditions[line[0]] == played_shape:
                line_score += win_bonus + shape_scores[played_shape]
            elif draw_conditions[line[0]] == played_shape:
                line_score += draw_bonus + shape_scores[played_shape]
            else:
                line_score += shape_scores[played_shape]
            tournament_score += line_score
    
    return tournament_score

def calculate_score_two(path: str) -> int:
    shape_scores: dict[str, int] = {'r': 1, 'p': 2, 's': 3}
    
    opponent_rock_cases: dict[str, str] = {'X': 's', 'Y': 'r', 'Z': 'p'}
    opponent_scissor_cases: dict[str, str] = {'X': 'p', 'Y': 's', 'Z': 'r'}
    opponent_paper_cases: dict[str, str] = {'X': 'r', 'Y': 'p', 'Z': 's'}


    
    win_bonus: int = 6
    draw_bonus: int = 3

    tournament_score: int = 0
    with open(path, 'r') as f:
        for line in f.readlines():
            opponent_shape = line[0]
            outcome = line.removesuffix('\n')[-1]
            if opponent_shape == 'A':
                played_shape = opponent_rock_cases[outcome]
            elif opponent_shape == 'B':
                played_shape = opponent_paper_cases[outcome]
            elif opponent_shape == 'C':
                played_shape = opponent_scissor_cases[outcome]
            else:
                raise Exception("Invalid Input")
            
            
            tournament_score += shape_scores[played_shape] 
            tournament_score += win_bonus if outcome == 'Z' else 0
            tournament_score += draw_bonus if outcome == 'Y' else 0
    return tournament_score
            



def main():
    print(calculate_score_two("dec2/input.txt"))

if __name__ == "__main__":
    main()