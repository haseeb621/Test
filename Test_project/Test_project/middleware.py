# 4. Python - ⁠Write a Request and Response 

class SimpleMiddleware:
 def __init__(self, get_response):
  self.get_response = get_response

 def __call__(self, request):
  print("Request Middleware: Before view")
  response = self.get_response(request)
  print("Response Middleware: After view")
  return response