# Bangladeshi Taka Note Detection

## Description

A FastAPI application that uses a YOLO model to detect Bangladeshi Taka notes from uploaded images.


## Current Features

- ✅ Project structure created
- ✅ Virtual environment configured
- ✅ Project dependencies installed
- ✅ FastAPI application initialized
- ✅ Root endpoint (`/`) implemented
- ✅ Interactive API documentation (Swagger UI & ReDoc)
- ⏳ Health check endpoint (`/health`) - In Progress
- ⏳ Prediction API - Planned



## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ShaifulPalash/bangladeshi-taka-note-detection.git
cd bangladeshi-taka-note-detection
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (CMD):**

```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```


## Run the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

Once the server is running, open your browser and visit:

- API Base URL: http://127.0.0.1:8000
- Root Endpoint: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

> **Note:** The root endpoint (`/`) is available and returns basic information about the API. Additional endpoints will be implemented in the following development steps.


## Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns basic information about the API. | 