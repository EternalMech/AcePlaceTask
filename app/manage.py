import click
import uvicorn
from app.db import connect_to_db, create_test_user
from conf import settings


@click.group()
def cli():
    pass


@cli.group('run-worker')
def run_worker():
    pass


@run_worker.command()
def runapi():
    connect_to_db()
    create_test_user()
    uvicorn.run("workers.api:app", host='0.0.0.0', port=settings.port)


if __name__ == '__main__':
    cli()
