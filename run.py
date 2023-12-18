import os
import json
import pip._vendor.requests 


def main(params):
  headers = {"Content-Type": "application/json"}
  response = pip._vendor.requests.get('https://function-76.1at6rgz00yjr.eu-de.codeengine.appdomain.cloud')
  