## Data Diri

**Nama:** Abel Fortino
**NIM:** 123140111
**Tugas:** Individu 3 - Pengembangan Aplikasi Web RA

## Fitur

- Input product review (text)
- Analyze sentiment (positive/negative/neutral) menggunakan Hugging Face
- Extract key points menggunakan Gemini AI
- Display hasil analysis di React frontend
- Save results ke PostgreSQL database
- Error handling dan loading states

## Teknologi

**Backend:** Python, Pyramid, SQLAlchemy, PostgreSQL, Hugging Face Transformers, Google Gemini AI  
**Frontend:** React, Vite, Axios, Bootstrap 5

## Prasyarat

- Python 3.11+
- Node.js 18+
- PostgreSQL 12+

## Setup dan Instalasi

### 1. Clone Repository
```bash
git clone [https://github.com/AbelFortino/Pengembangan-Aplikasi-Web]
cd product-review-analyzer
```

### 2. Setup Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -e .
```

### 3. Setup Database

Buat database PostgreSQL:
```sql
CREATE DATABASE review_db;
```

### 4. Konfigurasi .env

Buat file `.env` di folder `backend/`:
```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/review_db
GEMINI_API_KEY=your_gemini_api_key
```

### 5. Setup Frontend

```bash
cd frontend
npm install
```

## Cara Menjalankan

### Backend
```bash
cd backend
pserve development.ini --reload
```
Backend: http://localhost:6543

### Frontend
```bash
cd frontend
npm run dev
```
Frontend: http://localhost:5173

## API Endpoints

### 1. POST /api/analyze-review
Menganalisis review baru dan menyimpannya ke database.

**Request:**
```json
{
  "review": "Produk ini sangat bagus!"
}
```

**Response:**
```json
{
  "status": "success",
  "id": 1,
  "review": {
    "id": 1,
    "product_review": "Produk ini sangat bagus!",
    "sentiment": "POSITIVE",
    "key_points": "Kualitas produk sangat baik; User sangat puas",
    "analysis_date": "2025-12-13T10:30:00"
  }
}
```

### 2. GET /api/reviews
Mengambil semua review yang tersimpan di database.

**Response:**
```json
[
  {
    "id": 1,
    "product_review": "Produk ini sangat bagus!",
    "sentiment": "POSITIVE",
    "key_points": "Kualitas produk sangat baik; User sangat puas",
    "analysis_date": "2025-12-13T10:30:00"
  }
]
```

## Struktur Project

```
product-review-analyzer/
├── backend/
│   ├── review_analyzer/
│   │   ├── __init__.py          # Konfigurasi Pyramid
│   │   ├── models.py            # Model database
│   │   ├── views.py             # API endpoints
│   │   └── analysis_service.py  # AI analysis service
│   ├── .env                     # Environment variables
│   ├── development.ini          # Konfigurasi server
│   └── setup.py                 # Package setup
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ReviewForm.jsx
│   │   │   └── AnalysisResult.jsx
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   └── package.json
└── README.md
```
