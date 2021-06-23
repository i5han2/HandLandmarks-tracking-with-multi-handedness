# HandLandmarks-tracking-with-multi-handedness
This Script is used to differentiate the right and left hand of a human being and also find the coordinates of the 21 landmarks of each hand using the mediapipe library.

## Demo

https://user-images.githubusercontent.com/57738183/123156802-5bc14b80-d487-11eb-9292-852348e3fd8a.mp4


## How to run this script

* Clone this repo
```
git clone <url>
```
* Install virtual environment
```
pip install virtualenv
```
* Create a virtual environment
```
virtualenv venv
```
* Activate virtual environment
```
venv\Scripts\activate
```
* Install all the dependencies
```
pip install -r requirements.txt
```
* Run the script
```
python main.py
```

After running the script, you will see the landmark coordinates and handedness list in the console. And a live video stream with hand landmark detection

Use this script for your specific use case <br />
Happy coding!!
