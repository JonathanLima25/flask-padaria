import click
from padoza.ext.database import db
from padoza.ext.auth import create_user
from padoza.models import Product

def create_db():
    """Creates database"""
    db.create_all()

def drop_db():
    """Cleans database"""
    db.drop_all()

def populate_db():
    data = [
        Product(
            id=1, name="Ciabatta", price="10", description="Italian Bread"
        ),
        Product(id=2, name="Baguete", price="15", description="French Bread"),
        Product(id=3, name="Pretzel", price="20", description="German Bread"),
    ]

    db.session.bulk_save_objects(data)
    db.session.commit()
    return Product.query.all()

def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_commad(app.cli.command()(command))

    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        return create_user(username, password)