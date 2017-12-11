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

    print("\n**Requirement 1**:"
          "\nThis program keeps track of the Pokemon characters, saves data to a file,"
          "\nand displays the data from a file")

    # PokemonFile is created
    pokemon_file = "Pokemon_File.txt"

    print("\n####################    In main()    ####################")
    pokemon_list = add_pokemon()

    print("\n**Requirement 2**:")
    save_data(pokemon_file, pokemon_list)

    # displays pokemon from pokemon_list
    display_pokemon(pokemon_list)

    # displays pokemon from pokemon_file
    print("\n**Requirement 3**:")
    display_data(pokemon_file)

    print("\n**Requirement 4**:")
    print("Program 9 was kind of tricky to fulfill since we had to incorporate File I/O in the program,"
          "\nbut I've managed to find a compromise between using the old code from program_8 and the newer"
          "\ncode for this program. It was a pretty fun program overall.")


# add_pokemon() function
def add_pokemon():
    print("\n__________    In add_pokemon()<From Program 8>    __________")
    print(" Program8's method of adding Pokemon using pokemon_list")
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
    print("\n__________    In display_pokemon()<From Program 8>    _________")
    # if the list has objects, the pokemon are printed, else message appears
    if len(pokemon_list) > 0:
        print(" Program8's method of displaying Pokemon using pokemon_list")
        for pokemon in pokemon_list:
            poke_index = pokemon_list.index(pokemon) + 1
            print("\n   Name of Pokemon #"+str(poke_index)+": "+pokemon.get_name())
            print("\n   Ability of Pokemon #"+str(poke_index)+": "+pokemon.get_ability())
    else:
        print(Bugger)
# you can use display_data() in addition to display_pokemon()


def save_data(file_name, pokemon_list):
    print("__________    In save_data()    __________")
    file_output1 = open(file_name, 'w')
    if len(pokemon_list) > 0:
        print(" Saving Pokemon data to Pokemon_File")
        for pokemon in pokemon_list:
            file_output1.write(pokemon.get_name()+"\n"+pokemon.get_ability()+"\n")
        file_output1.close()
    else:
        print(Bugger)


def display_data(file_name):
    print("__________    In display_data()    __________")
    len_read = open(file_name, 'r+')
    len_read.seek(0, 2)
    # getting file size in byte form
    f_size = len_read.tell()
    len_read.close()

    file_input1 = open(file_name, 'r')
    if f_size > 0:
        current_byte = 0
        i_count = 1
        poke_index = 1
        while current_byte < f_size:
            if i_count == 1:
                print("")
                # if odd num line, print pokemon name
            if i_count % 2 != 0:
                print("   Name of Pokemon #" + str(poke_index) + ": " + file_input1.readline())
                # if even num line, print ability
            else:
                print("   Ability of Pokemon #" + str(poke_index) + ": " + file_input1.readline())
                # count one poke index up
                poke_index += 1
            current_byte = file_input1.tell()
            i_count += 1
        file_input1.close()
    else:
        print(Bugger)


if __name__ == '__main__':
    main()

else:
    pass
