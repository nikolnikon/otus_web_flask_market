import glob
import click
import os
from flask import current_app
from flask.cli import AppGroup
from flask_fixtures.loaders import YAMLLoader
from flask_fixtures import load_fixtures

from flask_market.products.models import db

user_cli = AppGroup('fixtures')


@user_cli.command('load')
def load_fixtures_():
    for fixture_dir in current_app.config.get('FIXTURES_DIRS', [os.path.join(current_app.root_path, 'fixtures')]):
        for fixture_file in sorted(glob.glob(fixture_dir + '/*.yml')):
            fixtures = YAMLLoader().load(fixture_file)
            load_fixtures(db, fixtures)

    # click.echo(f'Fixtures were done')

