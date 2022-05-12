import typer

app = typer.Typer()

def main(delete: bool = typer.Option(False, help="Delete found files"), extension: str = typer.Argument("txt", help="File extension")):
    """
    Display files find by extension
    """

    typer.echo(f"Recherche de fichiers avec l'extension { extension }.")
    if delete:
        typer.echo("Suppression des fichiers trouvés.")

@app.command()
def search_py():
    main(delete=False, extension="py")

@app.command()
def delete_py():
    main(delete=True, extension="py")

app()