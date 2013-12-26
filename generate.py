#!/usr/bin/env python

import os

def generateSketelon():
    path = os.getcwd()

    try:
        os.mkdir(path + '/static')
        os.mkdir(path + '/static/scripts')
        os.mkdir(path + '/static/css')
        os.mkdir(path + '/static/img')
        os.mkdir(path + '/templates')
    except Exception,e:
        print(e)

    with open(path + '/' + 'README.md', 'w') as readme:
        readme.write('This is a flask project \n')

    with open(path + '/' + 'templates/' + 'index.html', 'w') as index:
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

    with open(path + '/' + 'routes.py', 'w') as routes:
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
    generateSketelon()
