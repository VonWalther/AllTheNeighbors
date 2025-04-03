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

#
#  Compares submission schema to expected schema
#  Returns True if match, False if not
#  Manual review if not
#
def check_schema(submission, stretch=False):
    submission_keys = list(submission.keys())
    if submission_keys != [ 'allLocations' ]:
        return False
    
    for i, location in enumerate(submission['allLocations']):
        location_keys = sorted(list(location.keys()))
        if not stretch and location_keys != [ 'closestPoint', 'location' ]:
            return False

        if stretch and location_keys != [ 'closestPoint', 'location', 'secondClosestPoint', 'thirdClosestPoint' ]:
            return False
    
    return True


def sort_schema(schema, stretch=False):
    schema['allLocations'].sort(key=lambda location : location['location'][0])
    schema['allLocations'].sort(key=lambda location : location['location'][1])
    schema['allLocations'].sort(key=lambda location : location['closestPoint'][0])
    schema['allLocations'].sort(key=lambda location : location['closestPoint'][1])
    
    if stretch:
        schema['allLocations'].sort(key=lambda location : location['secondClosestPoint'][0])
        schema['allLocations'].sort(key=lambda location : location['secondClosestPoint'][1])
        schema['allLocations'].sort(key=lambda location : location['thirdClosestPoint'][0])
        schema['allLocations'].sort(key=lambda location : location['thirdClosestPoint'][1])

if __name__ == "__main__":
    with open('stretch_response_example.json', 'r') as f_submission:
        submission = json.loads(f_submission.read())
    
    sort_schema(submission, True)
    print(submission)