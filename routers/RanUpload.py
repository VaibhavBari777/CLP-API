from fastapi import HTTPException, UploadFile, APIRouter, File
import pandas as pd
from database import SessionLocal
from models import Data
from sqlalchemy.exc import IntegrityError
import os

router = APIRouter(prefix="/upload-ran")

@router.post("/upload-ran", tags=["Upload-RAN"])
async def upload_excel(file: UploadFile = File(...)):

    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        df = pd.read_excel(file_path, skiprows=2)

        # Rename columns
        df.rename(columns={
            'S.No': 'S_No',
            'Request Date\n(DD-MM-YY)\n': 'Request_Date',
            'Tentative On-Air\nDate(DD-MM-YY)': 'Tentative_On_Air_Date',
            'Service Type': 'Service_Type',
            'Project name': 'Project_Name',
            'Circle Name': 'Circle_Name',
            'District Name': 'District_Name',
            'Town Name': 'Town_Name',
            'Site ID': 'Site_ID',
            'Infra ID': 'Infra_ID',
            'NSS ID\n(Min & Max Length=10)': 'NSS_ID',
            'Site Name': 'Site_Name',
            'RF Cluster': 'RF_Cluster',
            'IPv4/IPv6\n(2G)': 'IPv4_IPv6_2G',
            'IPv4/IPv6\n(4G)': 'IPv4_IPv6_4G',
            'Final Technology (2G/4G/5G/SRAN)': 'Final_Technology',
            'BTS Vendor': 'BTS_Vendor',
            '2G Site (TDM/IP)': 'Site_2G_TMD_IP',
            'BSC ID': 'BSC_ID',
            'BSC IP': 'BSC_IP',
            'MME ID': 'MME_ID',
            'MME IP': 'MME_IP',
            'SGW ID': 'SGW_ID',
            'SGW IP': 'SGW_IP',
            'OSS ID': 'OSS_ID',
            'OSS IP': 'OSS_IP',
            'RFAI Status': 'RFAI_Status'
        }, inplace=True)

        MANDATORY_COLUMNS = [
            "Request_Date",
            "Tentative_On_Air_Date",
            "Project_Name",
            "Circle_Name",
            "BTS_Vendor",
            "NSS_ID"
        ]

        # Check mandatory columns existence
        missing_cols = [c for c in MANDATORY_COLUMNS if c not in df.columns]
        if missing_cols:
            raise HTTPException(400, f"Missing columns: {missing_cols}")

        # Null check
        if df["NSS_ID"].isna().any():
            raise HTTPException(400, "NSS_ID contains null values")

        # Duplicate NSS_ID in file
        if df["NSS_ID"].duplicated().any():
            raise HTTPException(400, "Duplicate NSS_ID in uploaded file")
        
        mismatch = (
            df["NSS_ID"].astype(str).str[:3]
            !=
            df["Circle_Name"].astype(str).str[:3]
        )

        if mismatch.any():
            raise HTTPException(
                status_code=400,
                detail="The circle name and NSS ID first 3 characters must be the same"
            )
        # NSS_ID validation
        df["NSS_ID"] = df["NSS_ID"].astype(str)

        if not df["NSS_ID"].apply(lambda x: len(x) == 10).all():
            raise HTTPException(400, "NSS_ID must be exactly 10 characters")

        if not df["NSS_ID"].apply(lambda x: x.isalnum()).all():
            raise HTTPException(400, "NSS_ID must be alphanumeric")

        if df[MANDATORY_COLUMNS].isnull().values.any():
            raise HTTPException(400, "Null values in mandatory columns")
        
        # Convert NaN → None
        df = df.replace(r'^\s*$', pd.NA, regex=True)
        df = df.where(pd.notnull(df), None)
        records = df.to_dict(orient="records")
        db = SessionLocal()
        try:
            db.bulk_insert_mappings(Data, records)
            db.commit()
        except IntegrityError:
            db.rollback()
            raise HTTPException(409, "Duplicate NSS_ID found in database")
        finally:
            db.close()

        return {
            "message": "File processed successfully",
            "rows_inserted": len(records)
        }
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
