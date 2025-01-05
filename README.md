# Invoice Generator

A Streamlit application for generating professional invoices from HTML template.

## Prerequisites

- Python 3.11+
- Poetry
- Docker (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/huatzhi/invoice-generator.git
cd invoice-generator
```

2. Install dependencies using Poetry:
```bash
poetry install
```

## Running the Application

### Method 1: Using Poetry shell
1. Activate the Poetry shell:
```bash
poetry shell
```

2. Run the Streamlit app:
```bash
streamlit run invoice.py
```

### Method 2: Direct Poetry run
```bash
poetry run streamlit run invoice.py
```

### Method 3: Using Docker
1. Build the Docker image:
```bash
docker build -t invoice-generator .
```

2. Run the container:
```bash
docker run -p 8501:8501 invoice-generator
```

The application will be available at `http://localhost:8501`

## Project Structure

```
invoice-generator/
├── invoice.py          # Main Streamlit application
├── template.html       # Invoice HTML template
├── pyproject.toml      # Poetry dependency configuration
├── poetry.lock         # Poetry lock file
├── README.md           # Project documentation
├── Dockerfile          # Docker configuration
└── .gitignore          # Git ignore rules
```

## Usage

1. Fill in the invoice details in the sidebar:
   - Invoice number
   - Date
   - Billing information
   - Item details

2. The HTML invoice will be generated automatically based on your inputs