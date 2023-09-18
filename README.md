
# PPT2PLANNER

This tool will convert ppt/pptx files to Presenter by WorshipTools file format.


## Features

- PPTX file support
- Auto title + verse tags
- Filter unwanted words
- Song title prefix (for easier filtering in Presenter)
- Sentence length filering (for blocks of text like slide number '1/3')
- Song author tag(for easier filtering in Presenter)


## Installation

Install ppt2planner dependencies with pip

```bash
  pip install requirements.txt
```
    
## Settings

Tool configuration can be done inside ```tools.py```
Available configuration:
- ```SONG_PREFIX``` (the prefix will be appended to song title for easier filtering inside Presenter tool)
- ```MIN_SENTENCE_LEN``` minimum sentece length (to filer out unwanted text), default 3
- ```ignored_keywords``` a dictionary containing words/phrases to be filtered out
- ```AUTHOR``` used to add song author, for better filtering

## Usage/Examples
The tool will look for all ppt/pptx files inside the provided ```<input_dir>``` and will dump processed files inside ```<output_dir> ```
The output file will be a .txt file containing slide text together with Planner specific tags (like song title, verse number etc.).

```bash
python ppt2planner.py -in <input_dir> -o <output_dir>
```

The output files can be imported into Planner.
## Roadmap

- ~~Support PPTX file format~~

- ~~Support PPT file format~~

