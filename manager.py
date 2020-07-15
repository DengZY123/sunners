
from flask_script import Server
import sys

sys.path.append('../')
from application import manager
from application import app
import www

#manager.add_command("runserver",Server(port=app.config['SERVER_PORT'],use_debugger=True,use_reloader=True))
manager.add_command("runserver",Server(port=8000,use_debugger=True ,use_reloader=True))

def main():
    manager.run()

if __name__ == "__main__":
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import tranceback
        tranceback.print_exc()
