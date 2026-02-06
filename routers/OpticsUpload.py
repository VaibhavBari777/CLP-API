
from fastapi import HTTPException,UploadFile ,APIRouter, File
import pandas as pd 
from database import SessionLocal
from models import Data
import os
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


# Map Excel headers to DB column names
COLUMN_MAP = {
    "NSS ID\n(Min & Max Length=10)": "NSS_ID",  # Mandatory
    "Optics Plan Received Status(Yes/No/NR)": "optics_plan_received_status",  # Mandatory
    "GNE-Optics POP/Mux Hostname 4G/5G": "gne_optics_pop_mux_hostname_4g_5g",
    "GNE-POP/Mux Port 4G/5G": "gne_pop_mux_port_4g_5g",
    "GNE Interface Remarks": "gne_interface_remarks",
    "Reference VLAN (Existing Interface)": "reference_vlan_existing_interface",
    "Router Location(2G/4G/5G)": "router_location_2g_4g_5g",
    "Router POP NSS ID(2G/4G/5G)": "router_pop_nss_id_2g_4g_5g",
    "Router Hostname(2G/4G/5G)": "router_hostname_2g_4g_5g",
    "Router SB Port(2G/4G/5G)": "router_sb_port_2g_4g_5g",
    "SB-Optics POP/Mux Hostname SB(Towards CEN)": "sb_optics_pop_mux_hostname_sb_towards_cen",
    "SB-Optics POP/Mux Ports SB(Towards CEN)": "sb_optics_pop_mux_ports_sb_towards_cen",
    "Port Status (New/Existing)(2G/4G/5G)": "port_status_new_existing_2g_4g_5g",
    "Optics Service Label": "optics_service_label",
    "Main Path": "main_path",
    "Protection Path": "protection_path",
    "Optics OSM": "optics_osm",
    "Optics Remarks": "optics_remarks"
}

router = APIRouter(prefix="/upload-optics")

@router.post("/upload-optics-excel" ,tags =["Optics-Upload"])
async def upload_optics_excel(file: UploadFile = File(...)):
    # Save temp file
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as f:
        f.write(await file.read())

    try:
        # Skip first 2 rows if your Excel has a header row on 3rd row
        df = pd.read_excel(temp_file, skiprows=2)

        # Rename columns to match DB
        df.rename(columns=COLUMN_MAP, inplace=True)

        # Check mandatory columns
        mandatory_cols = ["NSS_ID", "optics_plan_received_status"]
        for col in mandatory_cols:
            if col not in df.columns:
                raise HTTPException(status_code=400, detail=f"Mandatory column {col} missing")
            if df[col].isna().any():
                raise HTTPException(status_code=400, detail=f"Mandatory column {col} contains null values")

        # Replace NaN with None for DB
        df = df.where(pd.notnull(df), None)

        records = df.to_dict(orient="records")

        db: Session = SessionLocal()
        try:
            for record in records:
                # Update existing row based on NSS_ID
                db_obj = db.query(Data).filter(Data.NSS_ID == record["NSS_ID"]).first()
                if db_obj:
                    for key, value in record.items():
                        setattr(db_obj, key, value)
                else:
                    # Optionally, reject new NSS_IDs if they are not present in DB
                    raise HTTPException(status_code=400, detail=f"NSS_ID {record['NSS_ID']} not found in database")
            db.commit()
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=409, detail=f"Database integrity error: {e}")
        finally:
            db.close()
    finally:
        os.remove(temp_file)

    return {"message": "Excel data updated successfully", "rows_processed": len(records)}



    
    