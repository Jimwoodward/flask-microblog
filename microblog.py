from app import app

# This is needed so that we can expose our flask app to external traffic
# Without this, when the app runs, it only listens to traffic on coming from the localhost
# With this in place we also start the app with `python microblog.py` instead of `flask run` (if you want to use the `flask` command to run the app, use the --host flag)
if __name__ == '__main__':
  app.run(host='0.0.0.0')