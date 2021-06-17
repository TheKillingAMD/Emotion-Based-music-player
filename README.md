Emotion-Based-Music-Player Emoticon
It's music player with any web browser as front-End which has the capablity to detect emotions from the face of user with the help of machine learning algorithm.
Description :

In this project we have used libraries like OpenCV, numpy etc.

OpenCV - For capturing images from webcam as well as for processing purpose. made implemantation of fisherface methodology of opencv for classification.

FisherFace - To train the Model and store it in a model-file(.xml). While using player it uses for prediction for emotion.

We have decided to put 4 emotions into consideration for model.

1. Angry
2. Happy
3. Sad
4. Neutral

Back End : Flask. We use Flask Framework to create a simple application providing a basic HTML - CSS Front End.

The Flow goes like - Run the main.py file it will trigger the flask app to run. The flask app operate at port number 5000. (This step will take some Time)

You can use any browser for opening the webpage, but we prefer Firefox as it more developer friendly browser.

We have used Youtube Embedding for playing songs. Google Chrome and Microsoft Edge will not allow Youtube to play songs in our app due to copyright Issues. Hence Firefox is preffered.

HOW TO RUN ?

Download the project and run **pip install** -r **requirements**.txt in your command line which will install all the dependeces and files required.

Then run python main.py

You can go to any browser and enter the URL : http://localhost:5000/ and the app will run.
