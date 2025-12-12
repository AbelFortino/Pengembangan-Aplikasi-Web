import React, { useState } from 'react';
import axios from 'axios';

const API_BASE_URL = 'http://localhost:6543/api/analyze-review';

function ReviewForm({ onAnalysisSuccess }) {
  const [review, setReview] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!review.trim()) return;

    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(API_BASE_URL, { review });
      onAnalysisSuccess(response.data.review);
      setReview(''); // Clear input
    } catch (err) {
      console.error('Analysis Error:', err);
      setError('Gagal menganalisis. Cek koneksi API atau Server Backend.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card shadow-sm p-4 mb-4">
      <h3 className="mb-3">Input Ulasan Produk</h3>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <textarea
            className="form-control"
            rows="4"
            placeholder="Masukkan ulasan produk Anda di sini..."
            value={review}
            onChange={(e) => setReview(e.target.value)}
            required
            disabled={loading}
          />
        </div>
        <button 
          type="submit" 
          className="btn btn-primary" 
          disabled={loading}
        >
          {loading ? 'Menganalisis...' : 'Analisis Review'}
        </button>
        {error && <p className="text-danger mt-2">{error}</p>}
      </form>
    </div>
  );
}

export default ReviewForm;