from decouple import config


HOTELS_BACKEND_HOST = config('HOTELS_BACKEND_HOST', default='127.0.0.1', cast=str)
HOTELS_BACKEND_PORT = config('HOTELS_BACKEND_PORT', default='8000', cast=str)
