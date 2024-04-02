# Julia's Plot Gen

## Usage

```bash
python src/makeplots.py [COMMAND] --[OPTIONS]
```

# To process all folders with default base path `data`

```bash
python src/makeplots.py
```

# To process all folders with a different path

```bash
python src/makeplots.py --base-path /your/custom/path

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
