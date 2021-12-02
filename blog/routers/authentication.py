from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from .. import JWTToken
from .. import schemas, models
from ..database import get_db
from ..hashing import Hash

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login")
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials!")

    access_token = JWTToken.create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
