# MedAI

this is a MVP. i tried to make a working demo as fast as i could.

**MedAI** is a prototype medical OCR system built in Python. It extracts text from medical documents using **Pytesseract** and provides a backend API for processing via **Flask** and **gRPC**. The frontend is minimal, using raw HTML templates, and is intended for demonstration purposes only.  

---

## Features

- **Backend:** Flask API handling requests and routing  
- **OCR Service:** Python + Pytesseract (to be implemented)  
- **Communication:** gRPC for connecting the OCR service to the backend  
- **Frontend:** Raw HTML templates for basic display of results  
- **Database:** Currently none / TBD  

---

## Architecture (current)
[Frontend - HTML Templates] <---> [Flask Backend] <--gRPC--> [OCR Service - Pytesseract]


- Frontend handles user input and displays results  
- Backend routes requests and orchestrates OCR tasks  
- OCR service (planned) will process images and return text  

---

## Planned Improvements

- Implement the OCR service fully with Pytesseract  
- Improve frontend (maybe React/Vue in the future)  
- Potential backend migration to **Go** for better performance and concurrency  
- Add persistent storage and user management  

---

## Getting Started

### Prerequisites

- Python 3.10+  
- Flask  
- gRPC (`grpcio` and `grpcio-tools`)  
- Pytesseract (once OCR is implemented)  

### Installation

```bash
# Clone repo
git clone https://github.com/yourusername/medai-ocr.git
cd medai-ocr

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Running the Backend
```sh
# Start Flask server
export FLASK_APP=app.py
flask run
```

> The OCR service is not yet implemented. Currently, the backend routes are placeholders.

# Notes
- The project is backend-first, frontend is purely for demonstration

- OCR service is planned but not implemented yet

- Some architecture choices may change (e.g., moving backend to Go)
