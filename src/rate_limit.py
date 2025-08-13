from slowapi import Limiter
from slowapi.util import get_remote_address

# In-memory limiter for dev; use API Gateway Usage Plans for real rate limiting
limiter = Limiter(key_func=get_remote_address, default_limits=["2/minute",
"20/day"])