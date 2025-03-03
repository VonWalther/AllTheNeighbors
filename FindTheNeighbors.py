import json
file_name = "Neighborhood_25:1000x1000.json"  #Hardcoded, might be nice to make a file picker or run as comand line tool.
def main():
    print("Hello World")
    with open(file_name, "r") as input:
        json_data = json.load(input)
    pair_list = []
    for pair in json_data["pairList"]:
        pair_list.append(pair)
    dist_between_pairs = []
    for i in range(0, len(pair_list)):
        for j in range(i+1, len(pair_list )):
            print(i + "," + j, end = " ")
        print()



if __name__ == "__main__":
    main()