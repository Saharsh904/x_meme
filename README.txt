X-meme is meme Stream Page where users can post memes by providing their name, a caption for the meme and the URL for the meme image as input. 
The page then retrieve and display the latest 100 posted Memes (names + meme images + caption).The interaction between the backend and the front is purely based 
REST api.
The backend is capable of receiving the posted meme inputs from the frontend and store them in a database.
The backend is capable of fetching the list of memes from the database and send them to the frontend.


The project mainly consist of two parts : Backend and Frontend

BACKEND:
* The backend is developed on the Django framework
* In the backend folder , there is application api, memestream and manage.py.. etc
   -- In backend , there is folder of api which consist of serializers.py, views.py and urls.py
   -- In in main application folder there is models.py which gives the basic database structure of the of the Meme.
   -- views.py is to make the logical management and workflow of the application.
   -- admin.py registers the model to the admin
   -- serializer.py manage the serializtion of incomming and outgoing data of the
   * In memestream folder:
    -- there is setting.py which takes care of main settings of the project
    -- manage.py  is used to run the server of the application


FRONTEND:
* The frontend of the project was made using HTML, CSS, javascript, Bootstrap 
-- html is used to write about the basic structure of the application
-- bootstrap and basic css was used to style the project
-- to make it dynamic Javascripts was used where the logic to acces the database from the api is also written.
-- There are two section of the page on one side there is form which can used to post the meme whereas on the other side there is meme section
   which is used to publish and see all the memes that are being posted on the page .