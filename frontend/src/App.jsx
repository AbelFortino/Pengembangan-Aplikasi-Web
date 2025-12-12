import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import ReviewForm from './components/ReviewForm';
import AnalysisResult from './components/AnalysisResult';
import 'bootstrap/dist/css/bootstrap.min.css'; // Untuk styling dasar

const API_REVIEWS_URL = 'http://localhost:6543/api/reviews';

function App() {
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchReviews = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get(API_REVIEWS_URL);
      // Sortir dari terbaru (ID terbesar)
      setReviews(response.data.sort((a, b) => b.id - a.id)); 
    } catch (err) {
      console.error('Fetch Reviews Error:', err);
      setError('Gagal mengambil data review dari backend.');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchReviews();
  }, [fetchReviews]);

  const handleAnalysisSuccess = (newReview) => {
    // Tambahkan review baru ke list, letakkan di paling atas
    setReviews(prevReviews => [newReview, ...prevReviews]);
  };

  return (
    <div className="container py-5">
      <header className="text-center mb-5">
        <h1 className="display-4">✨ Product Review Analyzer ✨</h1>
        <p className="lead">Analisis Sentimen (Hugging Face) & Ekstraksi Poin Kunci (Gemini)</p>
      </header>
      
      <ReviewForm onAnalysisSuccess={handleAnalysisSuccess} />
      
      <hr />
      
      {loading && <div className="text-center text-primary">Memuat hasil dari database...</div>}
      {error && <div className="alert alert-danger">{error}</div>}
      {!loading && !error && <AnalysisResult reviews={reviews} />}
      
    </div>
  );
}

export default App;