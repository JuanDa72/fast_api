from passlib.context import CryptContext
from config import settings
from datetime import datetime, timedelta, timezone
from jose import jwt 

# Password hashing context using Argon2 algorithm 
#and deprecating any older algorithms automatically
pwd_context=CryptContext(schemes=["argon2"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Hash the provided password using the defined password context."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify that the provided plain password matches the hashed password."""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data:dict):
    to_enconde=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=settings.access_token_expire_minutes)
    to_enconde.update({"exp":expire})
    encoded_jwt=jwt.encode(to_enconde, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt