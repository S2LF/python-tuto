from pathlib import Path

dirs = {
    '.mp3': "Musique",
    '.wav': "Musique",
    '.flac': "Musique",
    '.mp4': "Vidéos",
    '.avi': "Vidéos",
    '.gif': "Vidéos",
    '.png': "Images",
    '.bmp': "Images",
    '.gif': "Images",
    '.txt': "Documents",
    '.pptx': "Documents",
    '.csv': "Documents",
    '.xls': "Documents",
    '.odp': "Documents",
    '.pages': "Documents",
}

tri_dir = Path("C:\\laragon\\www\\python\\Part2\\Fichiers\\data")

files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)