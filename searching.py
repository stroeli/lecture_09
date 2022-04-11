import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field in set(data.keys()):
        return data[field]

def linear_search(unordered_numbers, hledane_cislo):
    positions = []
    count = 0
    for position, number in enumerate(unordered_numbers):
        if number == hledane_cislo:
            positions.append(position)
            count += 1

    output = dict()
    output["positions"] = positions
    output["count"] = count
    # output = {"positions" : positions, "count" : count}
    return output

def pattern_search(dna_sequence, hledany_vzor):
    positions = set()
    for i in range(0, len(dna_sequence) - len(hledany_vzor) + 1):
        subsequence = dna_sequence[i:(i+len(hledany_vzor))]
        same = True
        for letter_subsequence, letter_hledany_vzor in zip(subsequence, hledany_vzor):
            if letter_subsequence != letter_hledany_vzor:
                same = False
                break
        if same:
            positions.add(i)

    return positions

def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)
    output_dict = linear_search(unordered_numbers, 5)
    print(output_dict)
    dna_sequence = read_data("sequential.json", "dna_sequence")
    print(dna_sequence)
    pozice = pattern_search(dna_sequence, "ATA")
    print(pozice)



if __name__ == '__main__':
    main()