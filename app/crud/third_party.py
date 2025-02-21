from sqlalchemy.orm import Session
from app.models.third_party import ThirdParty
from app.schemas.third_party import ThirdPartyCreate

def create_third_party(db: Session, third_party: ThirdPartyCreate):
    db_third_party = ThirdParty(
        c_third_party_id=third_party.third_party_id,
        c_first_name=third_party.first_name,
        c_last_name=third_party.last_name,
        c_national_id=third_party.national_id,
        c_phone_number=third_party.phone_number,
        c_birth_date=third_party.birth_date,
        c_amount=third_party.amount,
        c_number_of_repayments=third_party.number_of_repayments
    )
    db.add(db_third_party)
    db.commit()
    db.refresh(db_third_party)
    return db_third_party

def get_third_party(db: Session,third_party_id):
    return db.query(ThirdParty).filter(ThirdParty.c_third_party_id == third_party_id).first()

def get_all(db: Session):
    return db.query(ThirdParty).order_by(ThirdParty.c_third_party_id).all()
