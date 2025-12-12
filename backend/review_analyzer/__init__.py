from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from dotenv import load_dotenv
import os

load_dotenv()

def main(global_config, **settings):
    """ Fungsi yang mengembalikan Pyramid WSGI application. """
    
    if 'db.url' not in settings:
        settings['db.url'] = os.environ.get('DATABASE_URL')
    
    from .models import get_engine, initialize_db
    engine = get_engine(settings)
    initialize_db(engine)

    with Configurator(settings=settings) as config:
        
        config.include('pyramid_tm')
        
        from .models import get_session_factory
        session_factory = get_session_factory(engine)
        config.registry['dbsession_factory'] = session_factory
        
        def get_dbsession(request):
            return session_factory()
        
        config.add_request_method(
            get_dbsession,
            'dbsession',
            reify=True
        )
        
        config.add_route('home', '/')
        config.add_route('analyze_review', '/api/analyze-review')
        config.add_route('get_reviews', '/api/reviews')
        
        config.scan('.views')
        
        def add_cors_headers(event):
            event.response.headers['Access-Control-Allow-Origin'] = '*'
            event.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, DELETE, PUT'
            event.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        
        config.add_subscriber(add_cors_headers, 'pyramid.events.NewResponse')
        
    return config.make_wsgi_app()