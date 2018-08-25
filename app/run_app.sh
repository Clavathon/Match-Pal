# this starts a gunicorn server with 2 workers on it, binded to localhost on port 8000.
# how gunicorn knows what app to run is via {file}:{variable name}.  In our case, app:app

gunicorn -w 2 -b :8000 app:app --reload
