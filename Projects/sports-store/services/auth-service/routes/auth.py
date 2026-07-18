from datetime import datetime, timezone

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, Depends, HTTPException
from pymongo.errors import DuplicateKeyError

from database import users_collection
from models import LoginRequest, RegisterRequest, TokenResponse, UserPublic
from security import create_token, get_current_user, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserPublic, status_code=201)
async def register(payload: RegisterRequest):
    doc = {
        "email": payload.email.lower(),
        "password_hash": hash_password(payload.password),
        "full_name": payload.full_name,
        "role": "customer",
        "created_at": datetime.now(timezone.utc),
    }
    try:
        result = await users_collection.insert_one(doc)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Email already registered")
    return UserPublic(
        id=str(result.inserted_id),
        email=doc["email"],
        full_name=doc["full_name"],
        role=doc["role"],
    )


@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest):
    user = await users_collection.find_one({"email": payload.email.lower()})
    if user is None or not verify_password(payload.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    user_public = UserPublic(
        id=str(user["_id"]),
        email=user["email"],
        full_name=user["full_name"],
        role=user["role"],
    )
    token = create_token(user_public.id, user_public.email, user_public.role)
    return TokenResponse(access_token=token, user=user_public)


@router.get("/me", response_model=UserPublic)
async def me(claims: dict = Depends(get_current_user)):
    try:
        user = await users_collection.find_one({"_id": ObjectId(claims["sub"])})
    except InvalidId:
        raise HTTPException(status_code=401, detail="Invalid token subject")
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserPublic(
        id=str(user["_id"]),
        email=user["email"],
        full_name=user["full_name"],
        role=user["role"],
    )
