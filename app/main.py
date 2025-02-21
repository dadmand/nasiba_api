from fastapi import FastAPI
from app.api import third_party
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Third Party API")

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