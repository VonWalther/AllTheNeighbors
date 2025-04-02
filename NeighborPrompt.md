**All the Neighbors**

Required Files: possibleLocationsSmall.json, possibleLocationsMedium.json, possibleLocationsLarge.json, possibleLocationsSmallOutput.json

A local game design company, Really Augmented, is developing an augmented reality game with a database of multiple cartesian coordinate pairs. The developers need help determining the closest point for each pair and outputting this information in a new json file. The final file for the program is expected to have no more than 100,000 coordinates. You have been provided with three different test files having 100 coordinates, 5000 coordinates, and 100,000 coordinates.

Develop a program that will allow the user to select an input file and create an output file formatted like the example provided. Once this process has been completed, Really Augmented would be interested in some additional features. They would like to be able to add new coordinates  (or remove existing ones) and then have the output file updated for that new point without having the run time of running the original file. They would like to have the option to create another output file that has the three closest points for each uploaded point instead of just one. They would also like to see two types of maps: an overall map of the points as well as a localized map for any given point highlighting the two nearest identified neighbors.

**User Stories:**  
As a user, I want to run the program and input the small json file and get the output of the small output file.  
As a user, I want to provide the medium and large files and receive a solution for all points within ninety seconds.

**Stretch Goals:**   
*Stretch Goals will be ignored if User Stories are not complete.*  
As a user, I want to be able to remove points from the uploaded  list and receive an updated output file.  
As a user, I want to be able to add points to the updated list and receive an updated output file.  
As a user, I want an overall visual representation of all the points provided in the file.  
As a user, I want a localized visual representation of a single point on the map as well as the location of its nearest two neighbors.  
As a user, I would like to have an option to create a second output file that provides the nearest three points for all points.  
Contest ID:\_\_\_\_\_\_\_\_\_\_\_\_\_

When you are done with both of the programs, submit your code on the USB flash drive provided to the test proctor. The programs are graded with the following attributes in mind, first using the initial user stories and (if at least 50% of user stories points are satisfied) then using the stretch goals.

* Completeness (90 pts) \- Does the program run an entire use case? Does it generally accomplish the task assigned?  
* Correctness of Output (80 pts) \- Does the program produce the output requested in the format requested?  
* Validation of Input (70 pts) \- Does the program check for input that could crash the program/cause it to provide incorrect or unexpected output?  
* Internal Documentation (50 pts) \- Is commenting provided? Could another developer come along and add functionality to your program with ease?  
* Efficiency of Code (60 pts) \- Does your program waste resources while running? Do you use optimal algorithms over brute force code?  
* Quality of Work (25 pts) \- Is this code professional? Externally, is the output to the user professional? Internally, is the code presented in a professional and organized manner?

*\_\_\_\_\_\_ Resume Provided  (10 pts)          \_\_\_\_\_\_ Professional Dress (10 pts)*



/*************************************************** Every thing past here is Judges Eyes Only ***********************************************************************/
# AI
## Code I
*import json*  
*import numpy as np*  
*from sklearn.neighbors import NearestNeighbors*  
*import matplotlib.pyplot as plt*

*class CoordinateManager:*  
    *def \_\_init\_\_(self, coordinates):*  
        *self.coordinates \= np.array(coordinates)*  
        *self.kd\_tree \= NearestNeighbors(n\_neighbors=3, algorithm='kd\_tree').fit(self.coordinates)*

    *def find\_closest\_points(self):*  
        *\# Find the nearest two neighbors for each point*  
        *distances, indices \= self.kd\_tree.kneighbors(self.coordinates)*  
        *closest\_points \= {}*  
        *for i, (dist, idx) in enumerate(zip(distances, indices)):*  
            *closest\_points\[tuple(self.coordinates\[i\])\] \= \[tuple(self.coordinates\[j\]) for j in idx\[1:3\]\]  \# Exclude the point itself*  
        *return closest\_points*

    *def add\_coordinate(self, coordinate):*  
        *\# Add a new coordinate and update the kd-tree*  
        *self.coordinates \= np.append(self.coordinates, \[coordinate\], axis=0)*  
        *self.kd\_tree \= NearestNeighbors(n\_neighbors=3, algorithm='kd\_tree').fit(self.coordinates)*

    *def remove\_coordinate(self, coordinate):*  
        *\# Remove a coordinate and update the kd-tree*  
        *self.coordinates \= self.coordinates\[np.all(self.coordinates \!= coordinate, axis=1)\]*  
        *self.kd\_tree \= NearestNeighbors(n\_neighbors=3, algorithm='kd\_tree').fit(self.coordinates)*

    *def generate\_map(self):*  
        *\# Plot the coordinates*  
        *plt.scatter(self.coordinates\[:, 0\], self.coordinates\[:, 1\], color='blue')*  
        *plt.title("Overall Map of Coordinates")*  
        *plt.show()*

    *def generate\_localized\_map(self, point):*  
        *\# Plot the selected point and its two nearest neighbors*  
        *distances, indices \= self.kd\_tree.kneighbors(\[point\])*  
        *nearest\_points \= self.coordinates\[indices\[0\]\[1:3\]\]*  
        *plt.scatter(self.coordinates\[:, 0\], self.coordinates\[:, 1\], color='blue', label='All Points')*  
        *plt.scatter(nearest\_points\[:, 0\], nearest\_points\[:, 1\], color='red', label='Nearest Neighbors')*  
        *plt.scatter(point\[0\], point\[1\], color='green', label='Selected Point')*  
        *plt.title(f"Localized Map for {point}")*  
        *plt.legend()*  
        *plt.show()*

*def load\_coordinates(file\_path):*  
    *with open(file\_path, 'r') as f:*  
        *data \= json.load(f)*  
    *return data\['coordinates'\]*

*def save\_output(file\_path, closest\_points):*  
    *with open(file\_path, 'w') as f:*  
        *json.dump(closest\_points, f, indent=4)*

*def main():*  
    *\# 1\. Load the input coordinates*  
    *file\_path \= input("Enter the path to the input JSON file: ")*  
    *coordinates \= load\_coordinates(file\_path)*  
      
    *\# 2\. Process the coordinates*  
    *manager \= CoordinateManager(coordinates)*  
    *closest\_points \= manager.find\_closest\_points()*

    *\# 3\. Save the output to a new file*  
    *output\_file \= input("Enter the path to save the output JSON file: ")*  
    *save\_output(output\_file, closest\_points)*

    *\# 4\. Display options for visualization*  
    *if input("Do you want to see the overall map? (y/n): ").lower() \== 'y':*  
        *manager.generate\_map()*

    *if input("Do you want to see a localized map for a point? (y/n): ").lower() \== 'y':*  
        *x \= float(input("Enter the x-coordinate of the point: "))*  
        *y \= float(input("Enter the y-coordinate of the point: "))*  
        *manager.generate\_localized\_map(\[x, y\])*

*if \_\_name\_\_ \== "\_\_main\_\_":*  
    *main()*

## Code II

*import json*  
*import math*

*def euclidean\_distance(point1, point2):*  
    *"""Compute the Euclidean distance between two points (x1, y1) and (x2, y2)."""*  
    *return math.sqrt((point2\[0\] \- point1\[0\]) \*\* 2 \+ (point2\[1\] \- point1\[1\]) \*\* 2\)*

*class CoordinateManager:*  
    *def \_\_init\_\_(self, coordinates):*  
        *self.coordinates \= coordinates*

    *def find\_closest\_points(self):*  
        *"""Find the two closest points for each coordinate."""*  
        *closest\_points \= {}*  
        *for i, point1 in enumerate(self.coordinates):*  
            *min\_distances \= \[(float('inf'), None), (float('inf'), None)\]  \# To store (distance, index)*  
            *for j, point2 in enumerate(self.coordinates):*  
                *if i \!= j:*  
                    *dist \= euclidean\_distance(point1, point2)*  
                    *if dist \< min\_distances\[1\]\[0\]:*  
                        *if dist \< min\_distances\[0\]\[0\]:*  
                            *min\_distances\[1\] \= min\_distances\[0\]*  
                            *min\_distances\[0\] \= (dist, j)*  
                        *else:*  
                            *min\_distances\[1\] \= (dist, j)*  
            *closest\_points\[tuple(point1)\] \= \[tuple(self.coordinates\[min\_distances\[0\]\[1\]\]),*  
                                             *tuple(self.coordinates\[min\_distances\[1\]\[1\]\])\]*  
        *return closest\_points*

    *def add\_coordinate(self, coordinate):*  
        *"""Add a new coordinate to the list and recompute closest points."""*  
        *self.coordinates.append(coordinate)*

    *def remove\_coordinate(self, coordinate):*  
        *"""Remove a coordinate and recompute closest points."""*  
        *if coordinate in self.coordinates:*  
            *self.coordinates.remove(coordinate)*  
        *else:*  
            *print(f"Coordinate {coordinate} not found.")*

*def load\_coordinates(file\_path):*  
    *"""Load the coordinates from a JSON file."""*  
    *with open(file\_path, 'r') as file:*  
        *data \= json.load(file)*  
    *return data\['coordinates'\]*

*def save\_output(file\_path, closest\_points):*  
    *"""Save the closest points information to a JSON file."""*  
    *with open(file\_path, 'w') as file:*  
        *json.dump(closest\_points, file, indent=4)*

*def main():*  
    *\# 1\. Load the input coordinates*  
    *file\_path \= input("Enter the path to the input JSON file: ")*  
    *coordinates \= load\_coordinates(file\_path)*  
      
    *\# 2\. Process the coordinates to find closest points*  
    *manager \= CoordinateManager(coordinates)*  
    *closest\_points \= manager.find\_closest\_points()*

    *\# 3\. Save the output to a new file*  
    *output\_file \= input("Enter the path to save the output JSON file: ")*  
    *save\_output(output\_file, closest\_points)*

    *\# 4\. Update options for adding/removing coordinates*  
    *while True:*  
        *update\_action \= input("Do you want to add or remove a coordinate? (add/remove/none): ").strip().lower()*  
        *if update\_action \== "add":*  
            *x \= float(input("Enter x-coordinate to add: "))*  
            *y \= float(input("Enter y-coordinate to add: "))*  
            *manager.add\_coordinate(\[x, y\])*  
            *closest\_points \= manager.find\_closest\_points()*  
            *save\_output(output\_file, closest\_points)*  
        *elif update\_action \== "remove":*  
            *x \= float(input("Enter x-coordinate to remove: "))*  
            *y \= float(input("Enter y-coordinate to remove: "))*  
            *manager.remove\_coordinate(\[x, y\])*  
            *closest\_points \= manager.find\_closest\_points()*  
            *save\_output(output\_file, closest\_points)*  
        *elif update\_action \== "none":*  
            *break*  
        *else:*  
            *print("Invalid option. Please choose 'add', 'remove', or 'none'.")*

    *print("Process complete.")*

*if \_\_name\_\_ \== "\_\_main\_\_":*  
    *main()*

