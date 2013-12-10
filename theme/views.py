# This example relies on you having install PyJWT, `sudo easy_install PyJWT` - you can
# read more about this in the GitHub repository https://github.com/progrium/pyjwt

from django.http import HttpResponseRedirect
from django.conf import settings

import time
import jwt
import uuid

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
@never_cache
@login_required
def index(request):

  u = request.user

  first = u.first_name
  last = u.last_name
  if not first and not last:
    first = "Anonymous"
    last = "User"

  payload = {
    "iat": int(time.time()),
    "jti": str(uuid.uuid1()),
    "name": first + last,
    "email": request.user.email
  }

  subdomain = settings.ZENDESK_URL
  shared_key = settings.ZENDESK_TOKEN
  jwt_string = jwt.encode(payload, shared_key)
  return HttpResponseRedirect("https://" + subdomain + ".zendesk.com/access/jwt?jwt=" + jwt_string)