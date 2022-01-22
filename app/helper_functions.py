from fastapi import status, HTTPException
import json

from base64 import urlsafe_b64encode, urlsafe_b64decode


def encode(index):
    '''
    This function encodes an integer into a base64 representation 
    (the shortest one by removing the '=' characters), returning as
    a result a string.
    '''
    index = str(index)
    index_bytes = index.encode('ascii')
    base64_bytes = urlsafe_b64encode(index_bytes)
    base64_index= base64_bytes.decode('ascii').rstrip('=')
    return base64_index

def decode(base64_index):
    '''
    This function decodes an string into the original integer,
    taking into account that the inputed string may be shorten.
    For that reason as many '=' characters are concatenated to
    it as len(input_string) needs to be multiple of 4.
    '''
    base64_index += "="*(4-len(base64_index)%4)
    base64_bytes = base64_index.encode('ascii')
    index_bytes = urlsafe_b64decode(base64_bytes)
    try:
        index = int(index_bytes.decode('ascii'))
    except UnicodeDecodeError and ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail='URL invalid')
    return index



# Not used, but might be useful for local development if using dictionaries in memory as storage:

def save_json_file(data, filename='data.json'):
    """
    Objective
    ----------
    Save JSON object to a local file.

    Parameters
    ----------
    data: dict
        JSON object to be saved
    filename: str (optional), default 'data.json'
        Absolute or relative path

    Returns
    -------
    None
    """
    data = json.dumps(data, indent=4)
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_json_file(filename='data.json'):
    """
    Objective
    ----------
    Load JSON object from a local file.

    Parameters
    ----------
    filename: str (optional), default 'data.json'
        Absolute or relative path

    Returns
    -------
    data: dict
        JSON object in dictionary format
    """
    with open(filename, 'r') as f:
        data = json.load(f)
        if type(data) is str:
            data = json.loads(data)
    return data