from fastapi import HTTPException,UploadFile ,APIRouter, File
import pandas as pd 
from database import SessionLocal
from models import Data
import os
MW_COLUMN_MAP = {
    "NSS ID\n(Min & Max Length=10)": "NSS_ID",                     # mandatory
    "POP NSS ID\n(Min & Max Length=10)": "pop_nss_id",             # mandatory
    "POP Name": "pop_name",
    "MW path(POP to Node)": "mw_path_pop_to_node",
    "MW OEM": "mw_oem",
    "Media Type\nMW/Optics/Router": "media_type_mw_optics_router",
    "MW Dropping IDU NE Name": "mw_dropping_idu_ne_name",
    "MW Dropping IDU NE Port": "mw_dropping_idu_ne_port",
    "Port Type (Electrical/Optical)": "mw_port_type_electrical_optical",
    "MW GNE IDU NE Name": "mw_gne_idu_ne_name",
    "MW GNE IDU Port": "mw_gne_idu_port",
    "MW Port Status": "mw_port_status",
    "Reference Vlan/Site Id /Existing Interface": "reference_vlan_site_id_existing_interface",
    "MW Plan Received Status(Yes/No/NR)": "mw_plan_received_status",  # mandatory
    "MW OSM": "mw_osm",                                              # mandatory
    "MW Remarks": "mw_remarks"
}

router = APIRouter(
    prefix="/upload-mw"
)
@router.post("/upload-mw", tags=["MW-Upload"])
async def upload_mw_excel(file: UploadFile = File(...)):
    temp_file = f"temp_{file.filename}"

    with open(temp_file, "wb") as f:
        f.write(await file.read())

    try:
        # Header is on 3rd row
        df = pd.read_excel(temp_file, skiprows=2)

        # Rename Excel columns → DB columns
        df.rename(columns=MW_COLUMN_MAP, inplace=True)

        # 🔴 Mandatory green columns
        mandatory_cols = [
            "NSS_ID",
            # "pop_nss_id",
            "mw_plan_received_status",
            "mw_osm"
        ]

        for col in mandatory_cols:
            if col not in df.columns:
                raise HTTPException(400, f"Mandatory column missing: {col}")
            if df[col].isna().any():
                raise HTTPException(400, f"Mandatory column has null values: {col}")

        # Replace NaN → None
        df = df.where(pd.notnull(df), None)

        records = df.to_dict(orient="records")

        db = SessionLocal()
        try:
            for record in records:
                db_obj = db.query(Data).filter(
                    Data.NSS_ID == record["NSS_ID"]
                ).first()

                if not db_obj:
                    raise HTTPException(
                        status_code=400,
                        detail=f"NSS_ID {record['NSS_ID']} not found in DB"
                    )

                for key, value in record.items():
                    if key != "NSS_ID":   # never update PK
                        setattr(db_obj, key, value)

            db.commit()

        except Exception:
            db.rollback()
            raise
        finally:
            db.close()

    finally:
        os.remove(temp_file)

    return {
        "message": "MW Excel data updated successfully",
        "rows_processed": len(records)
    }



