from flask.ext.script import Manager

from stocker import app


manager = Manager(app)


@manager.command
def run():
    app.run(debug=True)


if __name__ == '__main__':
    manager.run()
