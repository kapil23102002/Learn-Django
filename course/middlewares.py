
# Class based middleware -------



class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('Initial response from Brother....')
    
    def __call__(self, request):
        print('Before View  Response from Brother Side') 
        response =  self.get_response(request)
        print('After View  Response from Brother Side') 
        return response
    
class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('Initial response from Father....')
    
    def __call__(self, request):
        print('Before View  Response from Father Side') 
        response =  self.get_response(request)
        print('After View  Response from Father Side') 
        return response
    
class MummyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('Initial response from Mummy....')
    
    def __call__(self, request):
        print('Before View  Response from Mummy Side') 
        response =  self.get_response(request)
        print('After View  Response from Mummy Side') 
        return response
    