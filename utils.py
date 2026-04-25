from passlib.context import CryptContext

# Password hashing context using Argon2 algorithm 
#and deprecating any older algorithms automatically
pwd_context=CryptContext(schemes=["argon2"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Hash the provided password using the defined password context."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify that the provided plain password matches the hashed password."""
    return pwd_context.verify(plain_password, hashed_password)
