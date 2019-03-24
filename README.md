# Submission2.0

Hello Professor , Anirban, Nicolas and Niranjan,

The submission is as follows, To make sure the development environments are same, I have attached a Conda Environment named environment.yml. Assuming you have anaconda installed, in your anaconda prompt (on windows) or terminal (on macOS or Linux), please run the following command, to set up the testing environment.
```
conda create env --name <<<NAME OF THE ENV YOU WANT TO GIVE>>> --file <<<Directory of the environment.yml>>>
```
The above will take a couple of minutes and sets up opencv,matplotlib,numpy,pandas and a bunch of other dependencies required for the set up and running of the submission.

Once you have the environment set up and you have cloned the repository, I have removed the dataset and added a few test images you can test the applications on. The easiest way to understand how all the applications function and see the running, I would <b>highly recommend watching the video</b>, which also explains the code in detail. (If not please do look further to know the commands to run the applications).
[![IMAGE ALT TEXT](http://i.imgur.com/Ot5DWAW.png)](http://www.youtube.com/watch?v=JL9k1E3dxbc&t=14s "A Dive into the submission")


Note: All applications work on python3
To run the application whose task is as follows :<b> "Develop a GUI where the user can select two images, which are at a specific distance and calculate the location of the sign, provided we know the image cordinates of it stored in the sign annotations file"</b>

```
python gui_input_image_get_position.py -r <<<expressway code>>>
```
| Expressway    | Code          |
| ------------- |:-------------:|
| GTSV i75      | i75           |
| GTSV i20      | i285          |
| GTSV StateRoute| i             |
| Smartphone 0 | 0|
|Smartphone 1 | 1| 

This command will prompt the user to select two images, and the rest algorithm outputs the performed calculations.

To run the application whose task is as follows :<b> "Develop a GUI application, where the user can select two images and then use his mouse to select to cordinates, after which the algorithm gets the required distances"</b>
```
python give_two_consecutive_images_and_user_points.py -im1  <<<test_image_1>>> -im2 <<<test_image_2>>> -r <<<expressway code>>>
```
The arguments provided in the terminal will be test_images, To make it easier I have already placed a few images and their corresponding datasets in the repository, itself so any path kind of path issues, will be resolved. This application gives rise to two different GUI's where you can select the points on the image. Once you have finished selecting the points make sure you press 'ESC', to move out of the selection. The algorithm tracks your mouse cordinates and outputs the required cordinates.


To run the application whose task is: <b>"Develop an interface where user can select an image which has a pothole, pavement marking etc and then the output corresponds to the area of the pothole"</b>
``` python gui_input_image_get_pothole.py ``` 
This will prompt 2 guis where you can move your cursor around to get the required cordinates, and then another where you can enter the GUI. Please do look into the video to better understand how this application works (quite intresting).

The above are some of the core applications, apart from that we have the following algorithms not in application stage, but definently worth a look.

``` python mark_base_on_road.py``` 
this program allows you to drag the base of the sign, onto the road. It draws a reactangle (shown in the video). The new image is stored and once the image is stored, run the following application
``` python road_length_using_brid_view.py``` 
This gives us the approximate bird eye view of the edited image, from this we can see how it might be possible with a little more work to get the approximate distacnce of a sign using a single image itself from the top view of the whole scene. Using this we can also roughly calculate the distance surrounding cars are from the camrea and also the relative velocity of other cars next to the GTSV.

``` python height_application.py ```
This is a very generaic application where the user can select two points in the image and after pressing 'ESC' we will output the height distnace/height between the pixels, which can be multiplied by a factor depending on the camera and obtain the horizontal and vertical distances. 


The error analysis are found in the error log file, but all applications output the predicted value and can be compared to ground truth values. More comprehensive discussion on each aspect is mentioned in the report which is in the repository. 
