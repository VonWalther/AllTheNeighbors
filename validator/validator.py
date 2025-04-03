######################################################################
#                                                                    #
#  AllTheNeighbors Validator                                         #
#                                                                    #
#  1  Sorts both submission and answer key by                        #
#     a  location x -> y                                             #
#     b  closestPoint x -> y                                         #
#     c  secondClosestPoint x -> y (stretch only)                    #
#     d  thirdClosestPoint x -> y (stretch only)                     #
#                                                                    #
#  2  Runs a diff on the two                                         #
#                                                                    #
#  3  Scores based on % output correct                               #
#     a  Incorrect schema -> 0 + flag                                #
#     b  % of incorrect array comparisons / total array comparisons  #
#     c  Score of (b) out of 80                                      #
#                                                                    #
######################################################################

import json

with open('stretch_response_example.json', 'r') as f_submission:
    submission = json.loads(f_submission.read())

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
