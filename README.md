# Django social network (instagram)


    
  <p align="center">
    <i>
A Instagram clone written in django :)
    </i>
  </p>
  
  <hr>
</p>

<p>


    A Django social clone created with Django, Postgres, Redis, and Html/Css
 <br>

<h3>
⭐️ Project features 
</h3>

<ul>
  <li>
registering and logging to user account  </li>
  <li>
posting photo  </li>
  <li>
commenting and liking photos  </li>
  <li>
following system  </li>
  <li>
   all CRUD operations on posts, comments, follows and likes with relevant permissions
  </li>
  <li>
    use Redis for count views of post
  </li>
  <li>
    use Postgres for backend databse
  </li>
  <li>
    gmail login
  </li>
  <li>
    save photos in Arvan cloud storage (like AWS)
  </li>
  <li>
    Restful Api
  </li>
</ul>

<hr>

<h3>
⚙️ Config the project
</h3>

<p>
First you should make venv for this project.
So in the main root of project you should type this command in your Terminal or Console: 
</p>
<pre>
python -m venv venv
</pre>
<p>
Now you should activate your venv.
So in the main root of project you should type this command in your Terminal or Console: 
</p>
<b>
In Linux/macOS:
</b>
<pre>
source venv/bin/activate
</pre>
<b>
In Windows:
</b>
<pre>
venv/Scripts/activate
</pre>

<p>
After activating venv you should install the <b>requirements.txt</b> packages. So type this command in your Terminal or Console: 
</p>
<pre>
pip install -r requirements.txt
</pre>

<p>
Create .env file in project root and put this :
</p>
<pre>
SECRET_KEY = 'Your SECRET_KEY'
AWS_ACCESS_KEY_ID = 'Your AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'Your AWS_SECRET_ACCESS_KEY'
AWS_S3_ENDPOINT_URL = 'AWS_S3_ENDPOINT_URL'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'Your SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Your SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'
</pre>

<h5>
Configuration of project almost done.
</h5>

<hr>

<h3>
🏁 Run the project
</h3>
<p>
First of all, please enter the following command in the Terminal or Console to make sure the project is configured correctly:
</p>
<pre>
python manage.py check
</pre>
<p>
You should see This message:
  <strong>
    <i>
      "System check identified no issues (0 silenced)."
    </i>
  </strong>
  <br>
  If you see this message you should create your project database. So type this commands in Terminal or Console:
</p>

<pre>
python manage.py makemigrations
</pre>
<pre>
python manage.py migrate
</pre>

<p>
After creating the project database, you should run project. So type this command in Terminal or Console:
</p>
<pre>
python manage.py runserver
</pre>

<h4>
Congratulations, you ran the project correctly ✅
</h4>

<p>
Now copy/paste this address in your browser URL bar:
</p>
<pre>
http://127.0.0.1:8000
</pre>

<hr>

<h4>
⭐️ Now you can use all the features of Django social.
</h4>

<hr>

### Thanks to..
* [Django](https://djangoproject.com)

### Fork
Fork and develop are free for everyone. Be sure I'll check your push requests out.

###### Made with :heart:

