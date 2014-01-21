#!/usr/bin/env python

import os, sys
import urllib

PATH = os.getcwd()

def retrieveFramework():
  global PATH

  try:
  	print("Downloading bootstrap...")
  	urllib.urlretrieve('https://github.com/twbs/bootstrap/releases/download/v3.0.3/bootstrap-3.0.3-dist.zip',
                       PATH + '/static/bootstrap3.zip')

  except IOError:
    print("Error to download de file")
    print("Check your internet connection")

  os.chdir('static')
  os.system('unzip bootstrap3.zip ')
  os.system('mv dist/css css/bootstrap-css')
  os.system('mv dist/js scripts/')
  os.system('mv dist/fonts/* fonts/')
  print("Cleaning up...")
  os.system('rm -rf bootstrap3.zip dist')

def generateSketelon(usingBootstrap=False):
  global PATH

  try:
    os.mkdir(PATH + '/static')
    os.mkdir(PATH + '/static/scripts')
    os.mkdir(PATH + '/static/css')
    os.mkdir(PATH + '/static/img')
    os.mkdir(PATH + '/static/fonts')
    os.mkdir(PATH + '/templates')
  except OSError:
    print("the file/dir already exists ")
    print("Replacing some files ...")

  with open(PATH + '/' + 'README.md', 'w') as readme:
    readme.write('This is a flask project \n')


  with open(PATH + '/' + 'templates/' + 'index.html', 'w') as index:
    if not usingBootstrap:
      index.write('''
      <!DOCTYPE html>
        <html>
          <head>
          </head>
          <body>
            <h1> This is your index page </h1>
            <h2> Now let's go and create a amazing thing! </h2>
          </body>
        </html>
      ''')
    else:
      index.write('''
      <!DOCTYPE html>
      <html>
        <head>
          <link href="../static/css/bootstrap-css/bootstrap.css" rel="stylesheet">
          <style type="text/css">
            body {
              padding-top: 50px;
            }
            .starter-template {
              padding: 40px 15px;
              text-align: center;
            }
          </style>
        </head>
        <body>
          <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="container">
              <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                  <span class="sr-only">Toggle navigation</span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Project name</a>
              </div>
              <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav">
                  <li class="active"><a href="#">Home</a></li>
                </ul>
              </div><!--/.nav-collapse -->
            </div>
          </div>
          <div class="container">
            <div class="starter-template">
              <h1>This is your index page</h1>
              <p class="lead">Now let's go and create a amazing thing!</p>
            </div>
          </div><!-- /.container -->

          <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
          <script src="../static/scripts/js/bootstrap.min.js"></script>
        </body>
      </html>
      ''')

  with open(PATH + '/' + 'routes.py', 'w') as routes:
    routes.write('''
from flask import app, request, Flask, render_template, request, url_for
import os
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app = Flask(__name__, template_folder=template_dir)
app.config.from_object(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.debug = True # to debug your application
  app.run()
''')


if __name__ == '__main__':
  if len(sys.argv) == 2 and sys.argv[1].lower() == 'bootstrap':
    generateSketelon(usingBootstrap=True)
    retrieveFramework()
  else:
    generateSketelon()
