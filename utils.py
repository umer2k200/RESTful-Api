#we always hash passwords before storing a user with username and password in the database
from passlib.context import CryptContext
#library to encrypt the passwords and to hash the password
#-------------------------------------------------------------------------------------------------
#JSON Web Token (JWT) is an open standard (RFC 7519) for securely transmitting information between parties as JSON object.
#It is compact, readable and digitally signed using a private key/ or a public key pair by the Identity Provider(IdP)
#The purpose of using JWT is not to hide data but to ensure the authenticity of the data. JWT is signed and encoded, not encrypted. 
#Jwt token consists of 3 parts header, payload and signature
#->header containds token type and alog used for signing encoding, alogos can be HMAC,SHA256,RSA,HS256,RS256
#->payload contains the session data called as claims
#->signature is calculated by encoding the header and payload using the base64url seperated by dot. 
#steps in jwt token:
#1)User sign-in using username and password or google/facebook.
#2)Authentication server verifies the credentials and issues a jwt signed using either a secret salt or a private key.
#3)User's Client uses the JWT to access protected resources by passing the JWT in HTTP Authorization header.
#4)Resource server then verifies the authenticity of the token using the secret salt/ public key
import os
from datetime import datetime,timedelta
from typing import Union, Any 
from jose import jwt
#These are the imports for creating access and refresh tokens
#now adding the constants that will be passed when creating jwt's
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # should be kept secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']    # should be kept secret
#now here jwt secret key and jwt refresh secret key can by any strings  but make sure to keep them secret and set them as environment variables
#using bycrypt to encrypt the password
password_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
#this method will take string and make hash of a paswword and returns it (a string)
def get_hashed_pass(password:str)-> str:
    return password_context.hash(password)
#this method will take the string pass and a string hash pass and then match if it matches or not 
#return type is of bool,it will return true or false
def verify_pass(password:str,hashed_pass:str)->bool:
    return password_context.verify(password,hashed_pass)
#Now writing the functions for generating access and refresh the tokens
#These functions takes the payload to include inside the JWT
#The only difference between these two functions is that the expiration time for refresh tokens is longer than for access tokens
def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt