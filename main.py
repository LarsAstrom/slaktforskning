import person
import sys

def add_person(people):
    assert False, 'Not implemented'

def change_person(people):
    assert False, 'Not implemented'

def pair_person(people):
    assert False, 'Not implemented'

def print_person(people):
    regex = input('Skriv in sökord\n').lower()
    matched_people = [p for p in people if p.find_regex(regex)]
    
    assert False, 'Not implemented'

def read_log():
    pass

def log(people):
    assert False, 'Not implemented'

def main(tree):
    people = read_log()
    while True:
        choice = int(input('\n'.join([
        '1. Lägg till person',
        '2. Ändra person',
        '3. Koppla ihop personer',
        '4. Skriv ut info om person',
        '9. Avsluta programmet',
        ''
        ])))
        if choice == 1:
            people = add_person(people)
        elif choice == 2:
            people = change_person(people)
        elif choice == 3:
            people = pair_person(people)
        elif choice == 4:
            people = print_person(people)
        elif choice == 9:
            break
        else:
            print('Ogiltigt val, försök igen.')


if __name__=='__main__':
    tree = sys.argv[1] if len(sys.argv) > 1 else input('Vilket träd?')
    assert tree in ['erica','lars']
    main(tree)
