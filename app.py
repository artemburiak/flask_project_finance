from flask import Flask
from routes import login_page, dashboard, export


app = Flask(__name__)
app.register_blueprint(dashboard.page, url_prefix='/dashboard')
app.register_blueprint(export.page, url_prefix='/export')

app.register_blueprint(login_page.page)

app.secret_key = "123"



if __name__ == '__main__':
    app.run(debug=True)
