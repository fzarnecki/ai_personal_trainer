## AI Personal Trainer
A simple project that will allow you to design your new workout programme with the help of AI!

Solution designed to showcase the ability to create a contenerised application, communicating with other services through API, with a convenient, easy to use web streamlit demo app to quickly evaluate the results in an interactive way.

Such a design is very convenient in AI model testing and quick, in-house experimentation.

## Showcase
Generating a sample workout plan using the app running in docker container:

<img src="https://github.com/fzarnecki/ai_personal_trainer/blob/main/data/images/showcase.gif">

## Run
You can run the demo app in two ways:
- with docker
- without docker

To run it using docker, run the ```run_docker_compose.sh``` script, inside the ```docker/``` subfolder. New container should start and the demo will be available on the port specified in the above file.

To run it without docker, make sure to install all the dependencies specified in ```requirements.txt```. To launch the app run ```streamlit run main.py``` from the level of the main directory. This will start the application and should open a new browser window. Make sure to adjust the images paths to display graphics on the website.