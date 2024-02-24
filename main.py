from flask import Flask
from hello_world.hello_world import helloword_bp

app = Flask(__name__)
app.register_blueprint(helloword_bp)

if __name__ == '__main__':
    app.run(debug=True)