from src import init_app
from config import config

configuration=config['development']

app = init_app(configuration)
if __name__=='__main__':
    app.run()
    