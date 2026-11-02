
from datetime import datetime, timedelta, timezone
from typing import Annotated
import os

import jwt
from jwt.exceptions import InvalidTokenError

from fastapi import FastAPI, Depends, HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

from pwdlib import PasswordHash
from pydantic import BaseModel


app = FastAPI(title="Email Assistant API")

# JWT configuration
SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "change-this-secret-before-production"
)
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

password_hasher = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)


# Demo user database
users_db = {
    "alice": {
        "username": "alice",
        "password": password_hasher.hash("alice123"),
        "permissions": ["read_emails"]
    },
    "bob": {
        "username": "bob",
        "password": password_hasher.hash("bob123"),
        "permissions": [
            "read_emails",
            "send_emails"
        ]
    }
}


# Step 1: Verify user credentials
def authenticate_user(username, password):

    user = users_db.get(username)

    if user is None:
        return None

    if not password_hasher.verify(
        password,
        user["password"]
    ):
        return None

    return user


# Step 2: Generate JWT token
def create_access_token(username):

    expiry = datetime.now(timezone.utc) + timedelta(
        minutes=TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": username,
        "exp": expiry
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# Step 3: Login API
@app.post("/token")
def login(
    form_data: Annotated[
        OAuth2PasswordRequestForm,
        Depends()
    ]
):

    user = authenticate_user(
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        user["username"]
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# Step 4: Identify logged-in user
def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)]
):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if not isinstance(username, str):
            raise InvalidTokenError("Invalid subject")

    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    user = users_db.get(username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user


# Step 5: Check user permissions
def require_permission(permission):

    def check_permission(
        user: Annotated[dict, Depends(get_current_user)]
    ):

        if permission not in user["permissions"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission"
            )

        return user

    return check_permission


# Email request model
class EmailRequest(BaseModel):
    recipient: str
    subject: str
    message: str


# Public route
@app.get("/")
def home():
    return {
        "message": "Welcome to Email Assistant"
    }


# Protected route: User profile
@app.get("/me")
def profile(
    user: Annotated[dict, Depends(get_current_user)]
):

    return {
        "username": user["username"],
        "permissions": user["permissions"]
    }


# Protected route: Read emails
@app.get("/emails")
def read_emails(
    user: Annotated[
        dict,
        Depends(require_permission("read_emails"))
    ]
):

    return {
        "emails": [
            {
                "sender": "hr@company.com",
                "subject": "Interview Schedule",
                "message": "Your interview is scheduled tomorrow."
            },
            {
                "sender": "team@company.com",
                "subject": "Project Update",
                "message": "Please check the latest project update."
            }
        ]
    }


# Protected route: Send emails
@app.post("/emails/send")
def send_email(
    email: EmailRequest,
    user: Annotated[
        dict,
        Depends(require_permission("send_emails"))
    ]
):

    # Demo: Email is not actually sent
    return {
        "message": "Email sent successfully",
        "sent_by": user["username"],
        "recipient": email.recipient,
        "subject": email.subject
    }
