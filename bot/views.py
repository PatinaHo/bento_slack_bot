from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

import os
import logging
import slack
import ssl as ssl_lib
import certifi

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

SLACK_VERIFICATION_TOKEN = os.environ['SLACK_VERIFICATION_TOKEN']

# SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)

class Events(APIView):
    def post(self, request, *args, **kwargs):
        slack_message = request.data
        print(slack_message.get('challenge'))
        print("SLACK_VERIFICATION_TOKEN =", SLACK_VERIFICATION_TOKEN)
        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            print("Enter 'token' block")
            return Response(status=status.HTTP_403_FORBIDDEN)

        # verification challenge
        if slack_message.get('type') == 'url_verification':    
            print("Enter 'type' block")
            return Response(data=slack_message.get('challenge'),                    #
                            status=status.HTTP_200_OK)             #

        return Response(status=status.HTTP_200_OK)