# StatsCLI

StatsCLI is a command line tool meant to help with data cleaning, modeling and analysis. Using a file-system like structure, one can navigate different columns of data, or make columns of their own to hold results of models. 

## Installation

Download this project as a zip file. Then, run the new_structure.py file using either your favorite editor or run one of the following commands inside the StatsCLI directory:
```bash
python new_structure.py
```
or:
```bash
python3 new_structure.py
```

## Usage

For now, it acts like a simple file system, being able to move, create and list directories. The table below should help explain commands until a help module is setup

| Commands    | Alias | Sub commands | arguments | result | 
| :---        |    :----:   |      :---: | :----: | :----: |
| Make Directory | makedir, mkdir, mk | None | new directory name | Creates a new directory in the current directory |
| Change Directory | changedir, cd | None | directory name | changes the current directory to the one specified |
| List Directory | listdir, ls | None | None | lists all of the items inside the current directory 
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

A system for possible unit tests need to be added, and hopefully will be added at somepoint.

## License

Under the MIT License, see LICENSE