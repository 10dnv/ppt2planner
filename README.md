
# PPT2PLANNER

This tool will convert ppt/pptx files to Presenter by WorshipTools file format.


## Installation

Install ppt2planner dependencies with pip

```bash
  pip install requirements.txt
```
    
## Usage/Examples
The tool will look for all ppt/pptx files inside the provided ```<input_dir>``` and will dump processed files inside ```<output_dir> ```
The output file will be a .txt file containing slide text together with Planner specific tags (like song title, verse number etc.).

```bash
python ppt2planner.py -in <input_dir> -o <output_dir>
```

The output files can be imported into Planner.
## Features

- PPTX file support
- Auto title + verse tags
- Filter unwanted words
- Song title prefix (for easier filtering in Presenter)


## Roadmap

- ~~PPTX file format~~

- PPT file format

