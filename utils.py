import flask


def get_page_and_limit(request: flask.Request) -> tuple[int | str | None, int | str | None]:
    """
    Retrieve current 'page' and 'limit' query parameters values.

    Args:
        request (flask.Request): The Flask request object.

    Returns:
        tuple[int | str | None, int | str | None]: A tuple containing 'page' and 'limit' values.
    """
    page = flask.request.args.get('page')
    if request.method == 'POST':
        limit = request.form.get('limit')
        page = 1
    else:
        limit = request.args.get('limit')
    return page, limit


def build_url_to_request(
    url: str,
    page: int | str | None = None,
    limit: int | str | None = None
) -> str:
    """
    Build a URL with 'page' and 'limit' query parameters.

    Args:
        url (str): The base URL to which query parameters will be added.
        page (int | str | None): The query parameter for the page number to retrieve.
        limit (int | str | None): The query parameter for the limit of records per page.

    Returns:
        str: The URL with specified query parameters for further request.
    """
    if page:
        url += f'?page={page}'
    if page and limit:
        url += f'&limit={limit}'
    elif limit:
        url += f'?limit={limit}'
    return url
