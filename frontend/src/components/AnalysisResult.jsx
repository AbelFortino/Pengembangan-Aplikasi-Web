import React from 'react';

const sentimentStyles = {
    POSITIVE: { color: 'green', icon: '👍' },
    NEGATIVE: { color: 'red', icon: '👎' },
    NEUTRAL: { color: 'gray', icon: '😐' },
};

function AnalysisResult({ reviews }) {
  if (reviews.length === 0) {
    return <p className="text-center text-muted">Belum ada hasil analisis. Coba input review!</p>;
  }

  return (
    <div className="mt-4">
      <h3>Hasil Analisis Tersimpan (Total: {reviews.length})</h3>
      <div className="row">
        {reviews.map((review) => {
          const style = sentimentStyles[review.sentiment] || sentimentStyles.NEUTRAL;
          // Mengubah string key points "Poin 1; Poin 2" menjadi array
          const keyPointsArray = review.key_points ? review.key_points.split(';').map(p => p.trim()) : [];

          return (
            <div key={review.id} className="col-md-6 mb-4">
              <div className="card h-100 shadow-sm border-2" style={{ borderColor: style.color }}>
                <div className="card-body">
                  <h5 className="card-title d-flex justify-content-between">
                    <span>Analisis #{review.id}</span>
                    <span style={{ color: style.color }}>
                      {style.icon} {review.sentiment}
                    </span>
                  </h5>
                  <hr />
                  <p className="card-text"><strong>Review:</strong> <em>"{review.product_review}"</em></p>
                  
                  <h6 className="mt-3">Poin Kunci (Key Points):</h6>
                  <ul className="list-group list-group-flush">
                    {keyPointsArray.map((point, index) => (
                      <li key={index} className="list-group-item p-1 border-0">{point}</li>
                    ))}
                  </ul>
                  <small className="text-muted d-block mt-3">
                    Tanggal: {new Date(review.analysis_date).toLocaleDateString()}
                  </small>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default AnalysisResult;