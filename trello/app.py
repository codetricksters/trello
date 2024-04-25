import typer
from config import Config
from trelloapi import trello

app_config = Config()
app = typer.Typer()
api = trello(app_config.API_KEY, app_config.TOKEN)