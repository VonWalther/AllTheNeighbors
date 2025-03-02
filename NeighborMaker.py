# This program creates data files for NeighborPrompt for Skills USA Texas 2025.
# Written by Carl Walther carl.waltehr@sbcglobal.net
# Started on 2/10/2025
# Last Touched....
from random import randint
import json
from datetime import datetime


# Need to create object to place in to Json here...
class NeighborhoodDataFile:
# Might come back to the naming of the data fields, given that class member namse shows up in the dictanary pairs in the json.
    def __init__(self, number_of_pairs, data_set_name="Neighborhood", x_limit=1000, y_limit=1000):
        data_set_name = data_set_name + "_" + str(number_of_pairs) + ":" + str(x_limit) + "x" + str(y_limit)
        self.name = data_set_name
        self.dateCreated = str(datetime.now())
        self.count = number_of_pairs
        self.xLimit = x_limit
        self.yLimit = y_limit
        plist = self.create_list()
        self.pairList = plist

    def create_pair(self):
        x = randint(0, self.xLimit)
        y = randint(0, self.yLimit)
        pair = [x, y]
        return pair

    def create_list(self):
        plist = []
        for i in range(self.count):
            new_pair = self.create_pair()
            plist.append(new_pair)
        return plist


def main():

    data = NeighborhoodDataFile(25)
    jdata = json.dumps(data.__dict__, indent=2)
    file_name = data.name + ".json"
    output = open(file_name, "w")
    output.write(jdata)
    output.close()


if __name__ == "__main__":
    main()
