import shutil
import zipfile
import os.path as path
from os import remove, system
from pathlib import Path
from PyReport import ROOT_DIR, get_info

PACKAGE_NAME = get_info()['name']
PACKAGE_DIR = path.join(ROOT_DIR, PACKAGE_NAME)
DOCS_DIR = path.dirname(path.abspath(__file__))
TEMPLATE_DIR = path.join(DOCS_DIR, 'templates')

########################################################################

def compress(file_names, output_directory):
    compression = zipfile.ZIP_DEFLATED

    zf = zipfile.ZipFile(path.join(output_directory, "PyReport_documentation.zip"), mode="w")

    try:
        for file_name in file_names:
            zf.write(path.join(DOCS_DIR, file_name), file_name, compress_type=compression)
    except FileNotFoundError as e:
        raise RuntimeError("An error occured while compressing the documentation.")
    finally:
        zf.close()

def modify_docfiles():
    with open(path.join(DOCS_DIR, PACKAGE_NAME, "index.html"), "r") as f:
        html = f.read()
        html = html.replace("../", "./")

        modules = [module.name for module in Path(DOCS_DIR, PACKAGE_NAME).rglob("*") if module.name != 'index.html']
        for module in modules:
            html = html.replace(f'href="{module}"', f'href="{PACKAGE_NAME}/{module}"')

        with open(path.join(DOCS_DIR, "index.html"), "w") as f:
                    f.write(html)

    remove(path.join(DOCS_DIR, PACKAGE_NAME, "index.html"))

    with open(path.join(DOCS_DIR, "index.js"), "r") as f:
        js = f.read()
        js = js.replace(f"{PACKAGE_NAME}/index.html", "index.html")

        with open(path.join(DOCS_DIR, "index.js"), "w") as f:
            f.write(js)

########################################################################

def build(output_directory, keep_temporary_files):
    try:
        system(f'pdoc3 --force --html --template-dir "{TEMPLATE_DIR}" --output-dir "{DOCS_DIR}" "{PACKAGE_DIR}"')
        modify_docfiles()
    except RuntimeError:
        print("An error occured while generating the documentation.")
        exit()

    try:
        start_at = len(DOCS_DIR) + 1
        file_names = ["doc-search.html", "index.js", "index.html"] + [str(file)[start_at:] for file in Path(DOCS_DIR, PACKAGE_NAME).rglob("*")]

        if len(file_names) == 0:
            raise RuntimeError("No files were found in the documentation directory.")
        
        compress(file_names, output_directory)
    except RuntimeError as e:
        print(e)
        exit()
    finally:
        if not keep_temporary_files:
            shutil.rmtree(path.join(DOCS_DIR, PACKAGE_NAME))
            remove(path.join(DOCS_DIR, "index.js"))
            remove(path.join(DOCS_DIR, "index.html"))
            remove(path.join(DOCS_DIR, "doc-search.html"))
        