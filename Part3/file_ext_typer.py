import typer

def main(delete: bool = typer.Option(False, help="Delete found files"), extension: str = typer.Argument("txt", help="File extension")):
    """
    Display files find by extension
    """

    print(delete)

    typer.echo(f"Recherche de fichiers avec l'extension { extension }.")

    ext = typer.prompt("Quelle extension souhaitez-vous rechercher ?")
    print(ext)
    if delete:
        do_delete = typer.confirm("Voulez-vous vraiment supprimer les fichiers trouvés ?")
        # do_delete = typer.confirm("Voulez-vous vraiment supprimer les fichiers trouvés ?", abort=True)
        if not do_delete:
            typer.echo("Annulation de l'opération.")
            raise typer.Abort()
        typer.echo("Suppression des fichiers trouvés.")

typer.run(main)