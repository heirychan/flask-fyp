from app import create_app, db, cli
from app.models import User, Post, News, Tech, Anime, Network, Evaluation, Ittime

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'News': News, 'Tech': Tech, 'Anime': Anime, 'Network': Network,
            'Evaluation': Evaluation, 'Ittime':Ittime}
