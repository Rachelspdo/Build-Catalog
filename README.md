# Build-Catalog
This project is a RESTful web application utilizing the Flask framework which accesses a SQL database that populates categories and their items. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

# In This Repo
This project has one main Python module `application.py` which runs the Flask application. A SQL database is created using the `database_setup.py` module. The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application. CSS/JS/Images are stored in the static directory.

# How To Install
1. Install Vagrant & VirtualBox
2. Download or clone Udacity Vagrant file (https://github.com/udacity/fullstack-nanodegree-vm)
3. Download this repository
3. Go to **catalog** inside Vagrant directory and place unzip file from step 3 here
4. Open Terminal
5. Go to Vagrant `/cd vagrant` directory, run `vagrant up`
6. Log into Vagrant VM by run `vagrant ssh`
7. Run `cd /vagrant/catalog`
8. Setup application database python by running `python database_setup.py`
9. Run application `python application.py`
10. **Access the application locally using http://localhost:5000**

# Google Login
1. Go to Google Dev Console (https://console.developers.google.com/)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'Restaurant Menu Application'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/login'
9. Select Create
10. Copy the Client ID and paste it into the data-clientid in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in the catalog directory
14. Run application `python application.py`

# JSON Endpoints

1. Restaurant JSON: /restaurant/JSON - Displays all restaurants.

2. Menu JSON: /restaurant/<int:restaurant_id>/menu/JSON - Displays all items in menu

3. Items JSON: /restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON/ - Displays specific item in the menu
