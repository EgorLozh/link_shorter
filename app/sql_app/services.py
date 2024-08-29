import random
import string

from app.sql_app.base import AsyncAbstractRedirectLinkRepo
from app.sql_app.container import get_container


async def generate_redirect_link(max_len = 10):
    def generate_random_string(max_length):
        length = random.randint(4, max_length)
        letters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
    repo = get_container().resolve(AsyncAbstractRedirectLinkRepo)

    for try_count in range(1000):
        generate_endpoint = generate_random_string(max_len)

        if await repo.get(redirect_endpoint=generate_endpoint) == None:
            return generate_endpoint
        
    raise Exception("Can't generate redirect link")
        
