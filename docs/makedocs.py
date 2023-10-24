import shutil
import zipfile
from os import path, remove, system, listdir
from pathlib import Path
from pyreport import ROOT_DIR, get_info

PACKAGE_NAME = get_info()["name"]
PACKAGE_DIR = path.join(ROOT_DIR, PACKAGE_NAME)
DOCS_DIR = path.dirname(path.abspath(__file__))
TEMPLATE_DIR = path.join(DOCS_DIR, "templates")
BLACKLIST = ["makedocs.py", "images", "templates"]

########################################################################


def clear_files():
    for file in listdir(DOCS_DIR):
        if file not in BLACKLIST:
            if path.isdir(path.join(DOCS_DIR, file)):
                shutil.rmtree(path.join(DOCS_DIR, file))
            else:
                remove(path.join(DOCS_DIR, file))


def compress(file_names, output_directory):
    compression = zipfile.ZIP_DEFLATED

    zf = zipfile.ZipFile(
        path.join(output_directory, "pyreport_documentation.zip"), mode="w"
    )

    try:
        for file_name in file_names:
            zf.write(
                path.join(DOCS_DIR, file_name), file_name, compress_type=compression
            )
    except FileNotFoundError as e:
        message = "An error occured while compressing the documentation."
        raise RuntimeError(message) from e
    finally:
        zf.close()


def modify_docfiles():
    with open(
        path.join(DOCS_DIR, PACKAGE_NAME, "index.html"), "r", encoding="utf8"
    ) as f:
        html = f.read()
        html = html.replace("../", "./")

        with open(path.join(DOCS_DIR, "index.html"), "w", encoding="utf8") as f:
            f.write(html)

    remove(path.join(DOCS_DIR, PACKAGE_NAME, "index.html"))

    with open(path.join(DOCS_DIR, "index.js"), "r", encoding="utf8") as f:
        js = f.read()
        js = js.replace(f"{PACKAGE_NAME}/", "")

        with open(path.join(DOCS_DIR, "index.js"), "w", encoding="utf8") as f:
            f.write(js)

    for file in listdir(path.join(DOCS_DIR, PACKAGE_NAME)):
        old = path.join(DOCS_DIR, PACKAGE_NAME, file)
        new = path.join(DOCS_DIR, file)
        shutil.move(old, new)


########################################################################


def build(output_directory, keep_temporary_files):
    try:
        clear_files()
        system(
            f'pdoc3 --force --html --template-dir "{TEMPLATE_DIR}" \
               --output-dir "{DOCS_DIR}" "{PACKAGE_DIR}"'
        )
        modify_docfiles()
    except RuntimeError:
        print("An error occured while generating the documentation.")
        exit()

    try:
        start_at = len(DOCS_DIR) + 1
        file_names = ["index.js"] + [
            str(file)[start_at:]
            for file in Path(DOCS_DIR).rglob("*")
            if file.name.endswith(".html")
        ]

        if len(file_names) == 0:
            raise RuntimeError("No files were found in the documentation directory.")

        print("All files:\n\t-", "\n\t- ".join(file_names))
        compress(file_names, output_directory)
    except RuntimeError as e:
        print(e)
        exit()
    finally:
        shutil.rmtree(path.join(DOCS_DIR, PACKAGE_NAME))
        if not keep_temporary_files:
            clear_files()
