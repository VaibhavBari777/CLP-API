from fastapi import FastAPI
import models
from database import SessionLocal, engine
from routers import (
    IpMwOpticsDownload,IpUpload, MwUpload,OpticsUpload,
    Provisioning_Download,RanUpload,Provisioning_Upload,
    TxE2E_Download,TxE2E_Uplaod,Site_Status_Upload,Site_Status_Download)
app = FastAPI()
models.Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app.include_router(RanUpload.router)
app.include_router(IpMwOpticsDownload.router)
app.include_router(IpUpload.router)
app.include_router(MwUpload.router)
app.include_router(OpticsUpload.router)
app.include_router(Provisioning_Download.router)
app.include_router(Provisioning_Upload.router)
app.include_router(TxE2E_Download.router)
app.include_router(TxE2E_Uplaod.router)
app.include_router(Site_Status_Upload.router)
app.include_router(Site_Status_Download.router)

# app.include_router(MW_Provisioning.router)
# app.include_router(Optics_Provisioning.router)