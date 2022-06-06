import yaml
import os
import glob
from pathlib import Path


# Fix for getting indentation in lists
# https://web.archive.org/web/20170903201521/https://pyyaml.org/ticket/64#comment:5
class IncreasedIndentationDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IncreasedIndentationDumper, self).increase_indent(flow, False)

def main():
    
    print("Generating TOC")
    
    with open("mkdocs.yaml") as f:
        mkdocs = yaml.safe_load(f)

    toc = [
        "index.md"
    ]
    
    # Add files from the eda and publish directories
    for notebook in glob.glob("eda/*.ipynb"):
        print("Adding ", notebook)
        toc.append(notebook)
    
    for notebook in glob.glob("publish/*.ipynb"):
        print("Adding ", notebook)
        #toc[os.path.basename(notebook).split('.')[0]] = notebook
        toc.append(notebook)
    
     
    mkdocs["nav"] = toc

    with open("mkdocs.yaml", "w") as f:
        yaml.dump(mkdocs, f, Dumper=IncreasedIndentationDumper, default_flow_style=False, sort_keys=False)
    
    print("Done")
    

if __name__ == "__main__":
    main()
