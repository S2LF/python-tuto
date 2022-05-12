from optparse import Option
import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()

def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher."),
         delete: bool = typer.Option(False, help="Supprimer les fichiers trouvés.")
        ):
    """Affiche les fichiers trouvés avec l'extension donnée."""

    print(extension, directory, delete)
    if not directory:
        cwd = Path.cwd()
        # directory = cwd.joinpath("Fichiers", "data", "test")
        directory = cwd.joinpath("Fichiers", "data")
        print(directory)
    else:
        directory = cwd.joinpath("Fichiers", "data")

    if not directory.exists():
        typer.secho(f"Le dossier '{ directory }' n'existe pas.", fg=typer.colors.RED)
if __name__ == "__main__":
    typer.run(main)