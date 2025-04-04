######################################################################
#                                                                    #
#  AllTheNeighbors Validator                                         #
#                                                                    #
#  1  Check for incorrect schema and return early if presented       #
#                                                                    #
#  2  Sorts both submission and answer key by                        #
#     a  location x -> y                                             #
#     b  closestPoint x -> y                                         #
#     c  secondClosestPoint x -> y (stretch only)                    #
#     d  thirdClosestPoint x -> y (stretch only)                     #
#                                                                    #
#  3  Runs a diff on the two                                         #
#                                                                    #
#  4  Scores based on % output correct                               #
#     a  % of incorrect array comparisons / total array comparisons  #
#     b  Score of (a) out of 80                                      #
#                                                                    #
######################################################################

import json
import sys


#
#  Compares submission schema to expected schema
#  Returns True if match, False if not
#  Manual review if not
#
def check_schema(submission, stretch=False):
    submission_keys = list(submission.keys())
    if submission_keys != ['allLocations']:
        return False

    for i, location in enumerate(submission['allLocations']):
        location_keys = sorted(list(location.keys()))
        if not stretch and location_keys != ['closestPoint', 'location']:
            return False

        if stretch and location_keys != ['closestPoint', 'location', 'secondClosestPoint', 'thirdClosestPoint']:
            return False

    return True


#
#  Sorts the schema using a standard formula
#  Allows for direct comparison of two similar schemas
#
def sort_schema(schema, stretch=False):
    if stretch:
        schema['allLocations'].sort(
            key=lambda location: location['thirdClosestPoint'][1])
        schema['allLocations'].sort(
            key=lambda location: location['thirdClosestPoint'][0])
        schema['allLocations'].sort(
            key=lambda location: location['secondClosestPoint'][1])
        schema['allLocations'].sort(
            key=lambda location: location['secondClosestPoint'][0])

    schema['allLocations'].sort(
        key=lambda location: location['closestPoint'][1])
    schema['allLocations'].sort(
        key=lambda location: location['closestPoint'][0])
    schema['allLocations'].sort(key=lambda location: location['location'][1])
    schema['allLocations'].sort(key=lambda location: location['location'][0])


#
#  Compares the results of two schemas
#  Compares by coordinate pair, i.e., length 2 array
#  Returns a whole number of points out of the total available
#  Accounts for unmatched lengths of lists
#
def compare_schemas(submission, answer, stretch=False, points=80):
    incorrect = 0
    total = 0

    submission_locations = submission['allLocations']
    answer_locations = answer['allLocations']

    # Fix length of answer_locations to that of submission_locations
    # Add additional length of answer_locations to total
    if len(submission_locations) < len(answer_locations):
        total_locations = len(answer_locations)
        answer_locations = answer_locations[:len(submission_locations)]
        total += (total_locations - len(answer_locations)) * 2

    # Fix length of submission_locations to that of answer_locations
    # Add additional length of submission_locations to incorrect
    if len(submission_locations) > len(answer_locations):
        total_locations = len(submission_locations)
        submission_locations = submission_locations[:len(answer_locations)]
        incorrect += (total_locations - len(submission_locations)) * 2
        if stretch:
            incorrect *= 2

    for submission_location, answer_location in zip(submission_locations, answer_locations):
        total += 2

        if submission_location['location'] != answer_location['location']:
            incorrect += 1
        if submission_location['closestPoint'] != answer_location['closestPoint']:
            incorrect += 1
        if stretch and submission_location['secondClosestPoint'] != answer_location['secondClosestPoint']:
            incorrect += 1
        if stretch and submission_location['thirdClosestPoint'] != answer_location['thirdClosestPoint']:
            incorrect += 1

    if stretch:
        total *= 2

    return int((points * (total - incorrect)) / float(total))


if __name__ == "__main__":
    submission_file = sys.argv[1]
    answer_file = sys.argv[2]
    stretch = False
    points = 80

    if len(sys.argv) > 3:
        stretch = "True" == sys.argv[3]

    if len(sys.argv) > 4:
        points = int(sys.argv[4])

    with open(submission_file, 'r') as f_submission:
        submission = json.loads(f_submission.read())

    with open(answer_file, 'r') as f_answer:
        answer = json.loads(f_answer.read())

    if not check_schema(submission, stretch):
        print('Schemas do not match - check manually')
        exit

    sort_schema(submission, stretch)
    sort_schema(answer, stretch)

    print(f'Points: {compare_schemas(submission, answer, stretch)}')
