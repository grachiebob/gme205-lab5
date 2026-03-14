# GmE 205: Laboratory 5 
## Polymorphism in Spatial Object Systems

### *Description*
This project aims to introduce polymorphism, which eliminates the excessive use of conditional logic by using the same method name while allowing objects to have their own way of implementing it.

### *Dependencies*
* Python 3.14
* Visual Studio Code
* shapely

### *Reflection*
1. The idea of polymorphism is that different objects can all understand the same method, but each object responds in its own way or differently. In this exercise, polymorphism is present in `spatial.py` through the `effective_area()` method implemented in the `SpatialObject` base class. The subclasses `Parcel`, `Building`, and `Road` implement this method differently: <br>
- `Parcel` calculates its area.<br>
- `Building` multiplies the polygon area by the number of floors.<br>
- `Road` uses a buffer to calculate the surface area.  <br> 
As shown in `run_lab5.py`, the subclasses are all called through `f.effective_area()`. Depending on what `f` represents, the method runs without the need for conditional logic.<br>
2. In the running script `run_lab5.py`, we do not need to repeat conditional logic such as `if type(feature) == Building: area = feature.geometry.area * feature.floors` We also do not need to write separate instructions for each subclass, which could lead to `God Functions` with a lot of `if/else` logic.  With polymorphism, the system does not need to know the type of object it deals with. Instead, we simply implement the same method name, `effective_area()`, and the subclasses will implement it in their own way. In `run_lab5.py`, this approach is applied through `f.effective_area()`. The method runs automatically depending on what `f` represents, which removes the need for conditional logic. 
3. Polymorphism and inheritance make it possible for multiple spatial classes to share a method name. In `spatial.py`, we defined the method `effective_area()` in the `SpatialObject` base class, and this structure is inherited or shared by the subclasses `Parcel`, `Building`, and `Road`. Due to inheritance, these subclasses now have access to the same method name, but they execute it in a different way because of polymorphism.  <br>
4. It is better for each object to compute its own area because we are trying to avoid the risk of creating `God Functions`. If we try to write separate instructions for computing the area per object, we would end up having more conditional statements (`if/else`), where the code will look messy, cluttered and complicated. On the contrary, if the subclasses `Parcel`, `Building`, and `Road` implement their own `effective_area()`, the responsibility is now designated to each object, in which they can simply compute for the area without the need for conditional logic. This approach makes the code easier to understand, easier to debug or know the errors, and flexible to extend when new subclasses are added.<br>
5. Using inheritance and polymorphism makes it flexible to extend `spatial.py`. Thus, adding a new class `River` will not give a major change in the existing logic of `spatial.py` and `run_lab5.py`. We can simply add it as a subclass `River` in our base class `SpatialObject`, in which the new subclass will be able to inherit the polymorphic method `effective_area()`. Similar to the case of subclass `Road`, `River` can implement its own way of calculating its area, for instance, by using buffer or the length and width. As a result, the only change needed in `spatial.py` is adding the new subclass `River`, and defining its own `effective_area()` implementation.<br>

## Author
Maria Graciella L. Roque  
Discord:[@grachiebob]

## Acknowledgements
* GmE 205 Laboratory Exercise 5 Manual
* [MarkDown](https://www.markdownguide.org/cheat-sheet/)

Edited on VS Code