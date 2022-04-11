import json
from pathlib import Path
import sys


def main():
    if len(sys.argv) < 2:
        print("Missing argument to folder with all translations")
        exit(1)

    path = Path(sys.argv[1])
    if not path.is_dir():
        print(f"Not a directory: {path}")
        exit(1)

    import_i18n(path)
    print("done")


def import_i18n(path: Path, out: Path = None):
    if out is None:
        out = Path(__file__).parents[1] / "cleaner_i18n" / "locale"
    for language in path.iterdir():
        if not language.is_dir() or language.name.startswith("."):
            continue
        data = json.loads((language / "bot.json").read_text())
        lines = ["# flake8: noqa E501"]
        lines.extend(
            f"{key} = {json.dumps(value, ensure_ascii=False)}"
            for key, value in data.items()
        )
        name = language.name.replace("-", "_").lower()
        (out / f"{name}.py").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
