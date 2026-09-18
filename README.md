# BUP GridWise LLM

BUP GridWise LLM is a smart energy optimization system that analyzes building energy information and provides simple energy-saving recommendations.

## Features

* Natural language energy query processing
* Energy data extraction
* Energy data validation using guardrails
* Solar power analysis
* Battery level analysis
* Energy optimization recommendations
* Missing data detection
* Remaining load calculation
* REST API using FastAPI
* Automated testing using Pytest

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Pytest
* Regular Expressions (Regex)
* OpenAI API (planned for future integration)

## Project Structure

```text
BUP_GridWise_LLM/
│
├── guardrails/
│   └── validator.py
│
├── llm/
│   └── interpreter.py
│
├── models/
│   └── schemas.py
│
├── optimizer/
│   └── energy_optimizer.py
│
├── tests/
│   └── test_api.py
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## How to Run

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Server

```bash
uvicorn app:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Endpoints

### Health Check

```text
GET /health
```

Checks whether the API is running.

### Energy Optimization

```text
POST /optimize
```

Analyzes energy information and provides an optimization recommendation.

### Natural Language Interpretation

```text
POST /interpret
```

Extracts energy information from a natural-language query.

### Smart Energy Assistant

```text
POST /ask
```

Processes a natural-language energy query, validates the data, and provides an energy optimization recommendation.

## Example Query

```text
My building has 100 kW load, 40 kW solar generation and 70% battery
```

## Example Response

```json
{
    "question": "My building has 100 kW load, 40 kW solar generation and 70% battery",
    "current_load": 100,
    "solar_generation": 40,
    "battery_level": 70,
    "recommended_action": "Use battery backup",
    "estimated_saving": 40,
    "remaining_load": 60,
    "message": "Use available solar power first, then battery backup."
}
```

## Validation and Guardrails

The system validates energy-related input before performing optimization.

Examples of invalid inputs include:

* Negative current load
* Negative solar generation
* Battery level below 0%
* Battery level above 100%
* Missing required energy information

For example:

```text
My battery is 70%
```

The system responds:

```text
Please provide
```# BUP GridWise LLM

BUP GridWise LLM is a smart energy optimization system that analyzes building energy information and provides simple energy-saving recommendations.

## Features

* Natural language energy query processing
* Energy data extraction
* Energy data validation using guardrails
* Solar power analysis
* Battery level analysis
* Energy optimization recommendations
* Missing data detection
* Remaining load calculation
* REST API using FastAPI
* Automated testing using Pytest

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Pytest
* Regular Expressions (Regex)
* OpenAI API (planned for future integration)

## Project Structure

```text
BUP_GridWise_LLM/
│
├── guardrails/
│   └── validator.py
│
├── llm/
│   └── interpreter.py
│
├── models/
│   └── schemas.py
│
├── optimizer/
│   └── energy_optimizer.py
│
├── tests/
│   └── test_api.py
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## How to Run

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Server

```bash
uvicorn app:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Endpoints

### Health Check

```text
GET /health
```

Checks whether the API is running.

### Energy Optimization

```text
POST /optimize
```

Analyzes energy information and provides an optimization recommendation.

### Natural Language Interpretation

```text
POST /interpret
```

Extracts energy information from a natural-language query.

### Smart Energy Assistant

```text
POST /ask
```

Processes a natural-language energy query, validates the data, and provides an energy optimization recommendation.

## Example Query

```text
My building has 100 kW load, 40 kW solar generation and 70% battery
```

## Example Response

```json
{
    "question": "My building has 100 kW load, 40 kW solar generation and 70% battery",
    "current_load": 100,
    "solar_generation": 40,
    "battery_level": 70,
    "recommended_action": "Use battery backup",
    "estimated_saving": 40,
    "remaining_load": 60,
    "message": "Use available solar power first, then battery backup."
}
```

## Validation and Guardrails

The system validates energy-related input before performing optimization.

Examples of invalid inputs include:

* Negative current load
* Negative solar generation
* Battery level below 0%
* Battery level above 100%
* Missing required energy information

For example:

```text
My battery is 70%
```

The system responds:

```text
Please provide
```
