from pydantic import BaseModel


class URL_encoder(BaseModel):
    url: str = 'https://www.example_url.com/'

class URL_decoder(BaseModel):
    url: str = 'http://short.est/MQ'
    

class ShowURL(BaseModel):
    original_url: str
    shortened_url: str
    class Config:
        orm_mode = True
