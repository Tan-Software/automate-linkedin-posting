import sys
import termcolor

sys.tracebacklimit = 0

def prompt_questions():
    termcolor.cprint("Veuillez entrer le numéro correspondant :", 'green')

    data_prompt = {
        1: 'Programmer un nouveau post sur LinkedIn.',
        2: 'Lancer en tâche de fond les posts programmés.',
        3: 'Lancer un test de connexion.'
    }
    
    for i in data_prompt:
        print(f"- {i} : {data_prompt[i]}")

    while True:
        try:
            answer = int(input("\nVotre choix : "))
            if 1 <= answer <= len(data_prompt):
                return answer
            else:
                raise ValueError
        except ValueError:
            termcolor.cprint("Le chiffre doit être compris entre 1 et", 'red', end='')
            termcolor.cprint(f" {len(data_prompt)}", 'red')


def presentation():
    border = "*" * 40
    print(termcolor.colored(border, 'blue'))
    print(termcolor.colored("www.tansoftware.com", 'blue'))
    print(termcolor.colored("automate linkedin posting", 'blue'))
    print(termcolor.colored("version 0.0.1", 'blue'))
    print(termcolor.colored(border, 'blue'))

def questions():
    return prompt_questions()
