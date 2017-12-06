# Bugger is printed when the user inputs no Pokemon
Bugger = "\n   You have entered no pokemon."


# pokemon Class
class Pokemon:
    # __init__ called AUTOMATICALLY when an object is created
    # this also assigns argument name and ability to 'self.__name & self.__ability'
    def __init__(self, name, ability):
      self.__name = name
      self.__ability = ability

    def get_name(self):
        return self.__name

    def get_ability(self):
        return self.__ability


# main() function
def main():
    print("This is Program 9")

    print("\nRequirement 1:"
          "\nThis program keeps track of the Pokemon characters, saves data to a file,"
          "\nand displays the data from a file")

    # PokemonFile is created
    PokemonFile = "Pokemon_File"

    print("##########    In main()    ##########")
    pokemon_list = add_pokemon()
    print("\nRequirement 2:")
    save_data(PokemonFile, pokemon_list)

    print("\nRequirement 3 & 4:")
    display_pokemon(pokemon_list)

    print("\nRequirement 5:")
    print("Program 8 was a fairly quick program to finish for me. I've had experience with"
          "\nobject oriented programming beforehand, so I didn't really struggle with this"
          "\none. I appreciate the Pokemon reference, very cool.")


# add_pokemon() function
def add_pokemon():
    print("\n__________    In add_pokemon()    __________")
    # creating a new list to hold pokemon characters
    pokemon_list = []
    # counter used in loop
    pokemon_number = 1
    more_pokemon = input("\n   Do you have a pokemon to enter? (y/n) ").lower()
    while more_pokemon == 'y':
        # user inputs pokemon name
        pokemon_name = input("\n   Enter name for Pokemon #{}: ".format(pokemon_number))
        # user inputs pokemon ability
        pokemon_ability = input("\n   Enter ability for Pokemon #{}: ".format(pokemon_number))
        # creating a new pokemon object with pokemon_name and pokemon_ability
        new_pokemon = Pokemon(pokemon_name, pokemon_ability)
        # adding new_pokemon to list
        pokemon_list.append(new_pokemon)
        # incrementing counter
        pokemon_number += 1
        # user inputs whether he/she wants to enter another pokemon
        more_pokemon = input("\n   Another pokemon to enter? (y/n) ").lower()
    return pokemon_list


def display_pokemon(pokemon_list):
    print("\n__________    In display_pokemon()    _________")
    # if the list has objects, the pokemon are printed, else message appears
    if len(pokemon_list) > 0:
        for pokemon in pokemon_list:
            poke_index = pokemon_list.index(pokemon) + 1
            print("\n   Name of Pokemon #"+str(poke_index)+": "+pokemon.get_name())
            print("\n   Ability of Pokemon #"+str(poke_index)+": "+pokemon.get_ability())
    else:
        print(Bugger)
# you can use display_data() in addition to display_pokemon()


def save_data(file_name, pokemon_list):
    print("\n__________    In save_data()    __________")
    file_output1 = open(file_name, 'w')
    if len(pokemon_list) > 0:
        print("   Saving Pokemon data to Pokemon_File")
        for pokemon in pokemon_list:
            file_output1.write(pokemon.get_name()+"\n"+pokemon.get_ability()+"\n")
        file_output1.close()
    else:
        print(Bugger)


def display_data(file_name, pokemon_list):
    print("\n__________    In display_data()    __________")


if __name__ == '__main__':
    main()

else:
    pass
