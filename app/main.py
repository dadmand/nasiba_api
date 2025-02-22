from fastapi import FastAPI
from app.api import third_party
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine

app = FastAPI(title="Third Party API")

# Create tables at startup
Base.metadata.create_all(bind=engine)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(third_party.router, prefix="/api/v1")