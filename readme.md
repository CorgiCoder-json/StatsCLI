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

| command | alias | sub commands | arguments | what it does |
| Make Directory | makedir, mkdir, mk | None | name of the new directory | Creates a directory in the file system |
| Change Directory | changedir, cd | None | name of the directory to change to | Changes the current directory to the specified one |
| List Directory | listdir, ls | None | None | Lists all of the possible items in the current directory | 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

A system for possible unit tests need to be added, and hopefully will be added at somepoint.

## License

Under the MIT License, see LICENSE