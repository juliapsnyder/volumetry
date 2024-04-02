# Julia's Plot Gen

## Usage

```bash
python makeplots.py [COMMAND] --[OPTIONS]
```

# To process a single file

```bash
python makeplots.py file --file-path data/<file>.txt
```

# To process all folders in a given base path

```bash
python makeplots.py folder --base-path data/
```

## Structure

```bash
volumetric-data-processor/
│
├── src/
│   ├── __init__.py
│   ├── file_info_extractor.py
│   ├── file_processor.py
│   ├── plot_generator.py
│   ├── makeplots.py
│   └── folder_processor.py
│
├── data/
│   ├── folder1/
│   │   └── ... (data files)
│   ├── folder2/
│   │   └── ... (data files)
│   └── ...
│
├── plots/
│   └── ... (generated plots)
│
├── requirements.txt
│
└── README.md
```

## Development

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

```bash
pip install -r requirements.txt
```
