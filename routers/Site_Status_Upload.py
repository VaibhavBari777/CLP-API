
from fastapi import HTTPException,UploadFile ,APIRouter, File
import pandas as pd 
from database import SessionLocal
from models import Data
import os
COLUMN_MAP = {
    "Project": "Project_Name",
    "Site ID": "Site_ID",
    "Vendor": "BTS_Vendor",
    "NSS ID": "NSS_ID",
    "MW OSM": "mw_osm",
    "MW OSM Execution Status": "mw_osm_execution_status",
    "Optics OSM": "optics_osm",
    "Optics OSM Execution Status": "optics_osm_execution_status",
    "IP CR": "code_cr_details_ip_cr",
    "IP CR Execution Status": "ip_cr_execution_status",
    "Tx E2E Readiness Status": "tx_e2e_readiness_status",
    "Site Status": "site_status",
    "Code E2E Status": "code_e2e_status"
}


router = APIRouter(prefix="/upload-Site-Status")
@router.post("/upload-Site-Status", tags=["Site-Status"])
async def upload_Site_status(file: UploadFile = File(...)):

    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as f:
        f.write(await file.read())

    try:
        df = pd.read_excel(temp_file)
        df.rename(columns=COLUMN_MAP, inplace=True)

        # Normalize empty strings
        df = df.replace(r'^\s*$', pd.NA, regex=True)

        # Mandatory column check
        mandatory_cols = [
            "mw_osm_execution_status",
            "optics_osm_execution_status",
            "ip_cr_execution_status"
        ]

        for col in mandatory_cols:
            if col not in df.columns:
                raise HTTPException(400, f"Mandatory column '{col}' missing in Excel")
            if df[col].isna().any():
                raise HTTPException(
                    400,
                    f"Mandatory column '{col}' contains empty values"
                )

        # NSS_ID mandatory for update
        if "NSS_ID" not in df.columns or df["NSS_ID"].isna().any():
            raise HTTPException(400, "NSS_ID missing or empty")

        # Convert NaN → None
        df = df.where(pd.notnull(df), None)
        records = df.to_dict(orient="records")

        db = SessionLocal()
        try:
            model_columns = {c.name for c in Data.__table__.columns}

            for record in records:
                db_obj = db.query(Data).filter(
                    Data.NSS_ID == record["NSS_ID"]
                ).first()

                if not db_obj:
                    raise HTTPException(
                        400,
                        f"NSS_ID {record['NSS_ID']} not found in DB"
                    )
                for key, value in record.items():
                    if key in model_columns and key != "NSS_ID":
                        setattr(db_obj, key, value)
            db.commit()

        except:
            db.rollback()
            raise
        finally:
            db.close()

    finally:
        os.remove(temp_file)

    return {
        "message": "Excel data uploaded successfully",
        "rows_processed": len(records)
    }
