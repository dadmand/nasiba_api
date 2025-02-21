from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud.third_party import create_third_party, get_third_party,get_all
from app.schemas.third_party import ThirdPartyCreate, ThirdPartyResponse
from app.dependencies import get_db
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=["third-party"])

@router.post(
    "/third-party/",
    response_model=ThirdPartyResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_third_party_endpoint(
    third_party: ThirdPartyCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_third_party(db, third_party)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Third party with this ID already exists"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get(
    "/third-party/{third_party_id}",
    response_model=ThirdPartyResponse
)
async def get_third_party_endpoint(
    third_party_id: str,
    db: Session = Depends(get_db)
):
    db_third_party = get_third_party(db, third_party_id)
    if not db_third_party:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Third party not found"
        )
    return db_third_party

@router.get(
    "/third-party/",
    response_model=list[ThirdPartyResponse]
)
async def get_all_third_parties_endpoint(
    db: Session = Depends(get_db)
):
    return get_all(db)

