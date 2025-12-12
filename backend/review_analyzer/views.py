from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from sqlalchemy.exc import DBAPIError
import transaction
from .models import Review
from .analysis_service import analyze_sentiment, extract_key_points

@view_config(route_name='home', renderer='json', request_method='GET')
def home(request):
    return {
        'message': 'Product Review Analyzer API',
        'version': '1.0',
        'endpoints': {
            'POST /api/analyze-review': 'Analyze product review',
            'GET /api/reviews': 'Get all reviews'
        }
    }

@view_config(route_name='analyze_review', renderer='json', request_method='POST')
def analyze_review(request):
    """
    POST /api/analyze-review: Menganalisis review baru dan menyimpannya.
    """
    try:
        data = request.json_body
    except ValueError:
        raise HTTPBadRequest('Invalid JSON')

    review_text = data.get('review')
    if not review_text:
        raise HTTPBadRequest('Missing "review" field in request body.')

    sentiment = analyze_sentiment(review_text)
    key_points = extract_key_points(review_text)

    new_review = Review(
        product_review=review_text,
        sentiment=sentiment,
        key_points=key_points,
    )

    try:
        session = request.dbsession
        session.add(new_review)
        session.flush()
        
        return {
            'status': 'success',
            'id': new_review.id,
            'review': new_review.to_dict()
        }
    except Exception as e:
        request.response.status = 500
        return {'status': 'error', 'message': f'Database error: {str(e)}'}


@view_config(route_name='get_reviews', renderer='json', request_method='GET')
def get_reviews(request):
    """
    GET /api/reviews: Mengambil semua review yang tersimpan.
    """
    try:
        reviews = request.dbsession.query(Review).all()
        return [review.to_dict() for review in reviews]
    except DBAPIError as e:
        request.response.status = 500
        return {'status': 'error', 'message': f'Database error: {e}'}