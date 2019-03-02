### Understanding the objective

<p>
The objective of the given module is to aprroximatley predict the real world cordinates of traffic signs across varrious
state roadways. This is one of the core objective of the ongoing reserach projects. The GTSV is a vehicle with multiple
sensors and cameras. Here in this case, we have the vehicle collecting images after a constant distance d which can be put up as a variable while programming</p>

#### Cordinate systsem 
For an image if you take the x-axis along the length and y-axis along the height, we generally assume the bottom left corner as (0,0).
So any pixel (x,y) would indicate that the pixel is x-pixels far from the bottom left corner along the x-axis and y-pixels far from the bottom left corner along the y-axis.
In achieving our objective, we are not intrested in how far our target pixel (center of the sign) is from the bottom left, but we are more 
intrested in finding how far the pixel is from the location of the optical center. So to put in words we are intrested in calculating how wide the pixel
is from the optical axis.

### Understanding the dataset
Before we look into the dataset, let us list out the inputs we have and desired outputs </br>

#### Inputs 
- We have the camera cordinates for every image
  - The cordinates we have are GPS cordinates and UTM N16 cordinates
- We have the location of sign, in each image. 
    -  This input can be recieved from a list of RoI's
    -  This input can also be recieved from the users, allowing them to select their point on intrest
- Distance between consecutive images, please note here incase of the allgather application dataset, there is not specific distnace mentioned 
  between the any two points of image capture, and hence the distance between two consecutive images can be found with the help of
  UTM N16 cordinates. The UTM N16 cordinates assumes the world to be a plane and the distance between any two points is the eucledian 
  distance between them
#### Expected Outputs
  - We are expected to estimate the location of a sign in the real world.
  - There are certain secodary objectives also:
    - Which include estimating the area, height and other physical parameters of objects present in the image. All these can be achieved
      using the conept of contours.

#### Dataset
The entire dataset is divided into two divisons 
- GTSV : This division contains data from images sensing vehicle, threr are three stateways from which data is collected.
        - The camera parameters are mentioned in the config.yaml
        - Apart form that to understand the pixel per mm we can use the camera specifications mentioed 
          at <a>https://www.ptgrey.com/grasshopper-5-0-mp-color-firewire-1394b-sony-icx625-camera</a>
        - From here it is clear that each pixel in the image is 3.45 micro-meter. Simple math establishes the number of pixels which we can formulate further
        - Each of the roadway set, contains the sign_annotations.json file, which indicate the location of sign in the image (if it exists)
        - The sign_annotations.json for every specific image contains, the top_left cordinates followed by the length and width of the image,following that is the class of the image.
        - coords.csv, this file contains the location of the camera, each time an image is taken.
- SmartPhone
        - This dataset is simillar apart from the fact the distance between consecutive images is not a constant like that in the GTSV case.
        - Here the distance is calculated from the eucledian distance between UTM N16 cordinates.

### Procedure in words

- Let the sign be W meters wide from the car and (l+d) meters far from the car initally
- Now the car moves a distance of d meters
- initally let the sign be x1 <b>pixels</b> wide from the optical center
- after moving a distance d meters let the sign be a disatane of x2 <b>pixels</b> wide from the optical center.
- when the car is at a distance of (l+d), let it make an angle of theta-1 beterrn the optical axis and sign.
then 
                          tan(theta-1) = x1(pixels) / f(mm) 
now we need to make sure the, the units are are same in both denominaor and numerator
from the camera config.yaml we know the focal length in pixels so, we have
                          tan(theta-1)=x1(pixels)/f(pixels)  = x1/f 
- Simillarly after the car moves a distance of 'd', we have
                           tan(theta-2)= x2(pixels)/f(pixels) 
-Since we have the numeric values of tan(theta-1) and tan(theta-2)
- we can calculate l and d respectively
l * tan(theta-2) = (l+d)*tan(theta-1)
l * x2/f= (l+d)  * x1/f
-cancelling 'f' in denominator both sides, we have l *x2 = (l+d) * x1
-exapanding l * x2 = l*x1 + d*x1
-taking l*x1 to the L.H.S and taking x1 common we have
- l(x2-x1) = d *x1
- Since d is a known variable in meters we have l = (d*x1)/(x2-x1)
- This gives us the value of l in meters
- from the triangle formed, we have the equality , l*tan(theta-2)= we
- this gives [(d*x1)/(x2-x1)]* tan(theta-2)
we know tan(theta-2)= x2/f
- w = [(d*x1)/(x2-x1)]* x2/f (meters)






