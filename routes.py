import flask
import httpx

import settings
import utils

main = flask.Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET'])
def get_main():
    """
    Render the main page with a list of available requests.
    """
    return flask.render_template('main.html')


@main.route('/search', methods=['GET', 'POST'])
def search():
    """
    An endpoint for retrieving initial filtered hotels records with a search word given.
    """
    if flask.request.method == 'POST':
        search_word = flask.request.form.get('search_word')
        flask.session['search_word'] = search_word
        return flask.redirect(flask.url_for('main.get_filtered_hotels'))
    return flask.render_template('search.html')


@main.route('/filtered_hotels', methods=['GET', 'POST'])
async def get_filtered_hotels():
    """
    Retrieve filtered hotel records based on a search word.

    Sets a 'search_word' parameter into the user session to support filtered iteration.
    """
    request = flask.request
    page, limit = utils.get_page_and_limit(request)
    base_request_url = (f'http://{settings.HOTELS_BACKEND_HOST}:{settings.HOTELS_BACKEND_PORT}'
                        f'/hotels/retrieve_filtered')
    built_url = utils.build_url_to_request(page=page, limit=limit, url=base_request_url)

    search_word = flask.session.get('search_word')
    async with httpx.AsyncClient() as client:
        response = await client.post(url=built_url, data=f'"{search_word}"')
        data = response.json()

    return flask.render_template('table.html', **data)


@main.route('/all_hotels', methods=['GET', 'POST'])
async def get_all_hotels():
    """
    Retrieve all hotel records.

    Shares a template for displaying entries with the 'get_filtered_hotels' route.
    Clears the 'search_word' from the user session to iterate over data without filters applied.
    """
    if 'search_word' in flask.session:
        flask.session.pop('search_word')

    request = flask.request
    page, limit = utils.get_page_and_limit(request)
    base_request_url = (f'http://{settings.HOTELS_BACKEND_HOST}:{settings.HOTELS_BACKEND_PORT}'
                        f'/hotels/retrieve')
    built_url = utils.build_url_to_request(page=page, limit=limit, url=base_request_url)

    async with httpx.AsyncClient() as client:
        response = await client.get(url=built_url)
        data = response.json()

    return flask.render_template('table.html', **data)
