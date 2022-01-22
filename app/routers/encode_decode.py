from fastapi import APIRouter, status, Response, HTTPException, WebSocket
from fastapi.responses import HTMLResponse

from app.schemas import URL_encoder, URL_decoder, ShowURL
from app.helper_functions import encode, decode

router = APIRouter()

index_by_original_urls = {
                            'https://www.example_url.com/': 1
                         }

original_url_by_index = {
                            1 : 'https://www.example_url.com/'
                        }

@router.post('/encode', status_code=status.HTTP_201_CREATED, response_model = ShowURL, tags=['Encode'])
def encode_url(request_body: URL_encoder, response: Response):

    original_url = request_body.url

    if original_url in index_by_original_urls:
        shortened_url =  'http://short.est/' + encode(index_by_original_urls[original_url])
        response.status_code = status.HTTP_302_FOUND
        return {'original_url': original_url, 'shortened_url': shortened_url}

    else:
        index = len(index_by_original_urls) + 1
        shortened_url = 'http://short.est/' + encode(index)
        index_by_original_urls[original_url] = index
        original_url_by_index[index] = original_url

        return {'original_url': original_url, 'shortened_url': shortened_url}


@router.post('/decode', status_code=status.HTTP_200_OK, response_model = ShowURL, tags=['Decode'])
def decode_url(request_body: URL_decoder):

    shortened_url = request_body.url
    index = decode(shortened_url.removeprefix('http://short.est/'))

    if index in original_url_by_index:
        original_url = original_url_by_index[index]
        return {'original_url': original_url, 'shortened_url': shortened_url}

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='URL not found')





html = open('./app/routers/html_code/frontpage.html', 'r').read()

@router.get('/', include_in_schema=False)
async def get():
    return HTMLResponse(html)

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        original_url = await websocket.receive_text()

        if original_url in index_by_original_urls:
            shortened_url =  'http://short.est/' + encode(index_by_original_urls[original_url])

        else:
            index = len(index_by_original_urls) + 1
            shortened_url = 'http://short.est/' + encode(index)
            index_by_original_urls[original_url] = index
            original_url_by_index[index] = original_url

        await websocket.send_text(shortened_url)