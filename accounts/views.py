from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import *
import logging


logger = logging.getLogger(__name__)


class LoginView(LoginView):
    logger.warning("warning do something")

