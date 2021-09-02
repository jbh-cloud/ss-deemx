import requests
from deemix.utils.crypto import _md5
from deemix.utils import USER_AGENT_HEADER
CLIENT_ID = "172365"
CLIENT_SECRET = "fb0bec7ccc063dab0417eb7b0d847f34"

def getAccessToken(email, password):
    password = _md5(password)
    request_hash = _md5(''.join([CLIENT_ID, email, password, CLIENT_SECRET]))
    response = requests.get(
        'https://api.deezer.com/auth/token',
        params={
            'app_id': CLIENT_ID,
            'login': email,
            'password': password,
            'hash': request_hash
        },
        headers={"User-Agent": USER_AGENT_HEADER}
    ).json()
    return response.get('access_token')

def getArlFromAccessToken(accessToken):
    session = requests.Session()
    session.get(
        "https://api.deezer.com/platform/generic/track/3135556",
        headers={"Authorization": f"Bearer {accessToken}", "User-Agent": USER_AGENT_HEADER}
    )
    response = session.get(
        'https://www.deezer.com/ajax/gw-light.php?method=user.getArl&input=3&api_version=1.0&api_token=null',
        headers={"User-Agent": USER_AGENT_HEADER}
    ).json()
    return response.get('results')
