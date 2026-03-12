from fastapi import Request, HTTPException, status
from app.db.session import AsyncSessionLocal


def get_pinecone_service(request: Request):
    return request.app.state.pinecone_service


def get_groq_service(request: Request):
    return request.app.state.groq_service


async def get_db():
    try:
        async with AsyncSessionLocal() as session:
            yield session
    except:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database is unavailable. Please try again later.",
        )
