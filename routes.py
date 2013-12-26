
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
    