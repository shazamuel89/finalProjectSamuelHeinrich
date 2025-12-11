### INF601 - Advanced Programming in Python
### Samuel Heinrich
### Final Project

# Last.fm Music Visualizer

A web application that visualizes a user's personal music listening habits using data from their Last.fm account.

## Description

This project aims go beyond typical music listening charts by presenting the data in an artistic and data-driven way.
The visualizations created represent the user's listening history and preferences through abstract and creative
graphics. The app allows a user to enter their Last.fm username (or any Last.fm username), after which the system
retrieves and processes their listening data. The user can select a number of statistical summaries with filters, and
then they can select from a variety of visualizations with optional customization.

The Last.fm API is essential to this project as it allows access to detailed user listening data such as
top artists, tracks, albums, and scrobbles. This data is freely accessible, and only requires a username to request it.
The framework used is Django, chosen for its simplicity and quick setup process.
For visualizations, the Python library Matplotlib is used to create graphs and visual patterns.
Other visualization libraries may be considered in the future as time allows.

## Getting Started

### Dependencies

* Python 3.13 or higher
* Django 5.0 or higher
* Bootstrap 5 (loaded via CDN)
* OS: Works on Windows, macOS, or Linux
* Required Pip packages (instructions for install below)

### Installing

* Clone the GitHub repository to your local machine:
```
git clone https://github.com/shazamuel89/miniproject4SamuelHeinrich.git
cd finalProjectSamuelHeinrich
```
* Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```
* Install required packages:
```
pip install -r requirements.txt
```
* Verify that Django is installed correctly:
```
python -m django --version
```

### Executing program

* Make database migrations and apply them:
```
cd LastfmMusicVisualizer
python manage.py makemigrations
python manage.py migrate
```
* Create an admin (superuser) account:
```
python manage.py createsuperuser
```
* Run the development server:
```
python manage.py runserver
```
* Open your browser and open the following on 2 separate tabs:
```
http://127.0.0.1:8000/
```
* On the second tab, replace the text after :8000/ with:
```
admin/
```
* Log in with the admin superuser account credentials you just created
* On the first tab, you can now view the main website and use the app

## Authors

Samuel Heinrich

## Version History

* 0.1
    * Initial Release

## Acknowledgments

* [Django Documentation](https://docs.djangoproject.com/en/5.2/)
* [Official Last.fm Api Documentation](https://www.last.fm/api)
* [Unofficial Last.fm API Documentation](https://github.com/lastfm-docs/api-docs)
* [Matplotlib Documentation](https://matplotlib.org/stable/)
* [Plotly Docuentation](https://plotly.com/python/)
* [Graph Gallery: Streamgraph with Python and Matplotlib](https://python-graph-gallery.com/streamchart-basic-matplotlib/)