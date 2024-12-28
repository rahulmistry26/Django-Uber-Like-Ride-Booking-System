from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
import jwt

class CustomAPIMiddleware(MiddlewareMixin):
    def isUserAuth(self,request,userRole):
        user_agent = request.headers.get("authorization",None)
        print(user_agent,"user_agent")
        if not user_agent:
            return False
        else:
            try:
                decoded_token = jwt.decode(
                    user_agent.split(" ")[1], "rahul", algorithms=["HS256"]
                )
            except jwt.ExpiredSignatureError:
                return False
            except jwt.InvalidTokenError:
                return False
            role = decoded_token.get("role", None)
            if role in userRole:
                return role
            else:
                return False