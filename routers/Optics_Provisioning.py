# from fastapi.responses import FileResponse
# from openpyxl import load_workbook
# import os, shutil
# from uuid import uuid4
# from typing import List
# from fastapi import APIRouter
# from fastapi import HTTPException
# from database import SessionLocal
# from sqlalchemy import select
# from models import Data



# OPTICS_EXCEL_COLUMN_MAP = {
#     "Circle": "Circle_Name",
#     "Project": "Project_Name",
#     "Site ID": "Site_ID",
#     "Vendor": "BTS_Vendor",
#     "NSS ID": "NSS_ID",
#     "MW OSM": "mw_osm",
#     "Optics OSM": "optics_osm",
#     "IP CR": "code_cr_details_ip_cr",
# }

# OPTICS_TEMPLATE_PATH = r"Provisioning/Sample_MW PROVISIONING_Provisoning_Update_Template (1).xlsx"
# TEMP_DIR = "temp_downloads"
# HEADER_ROW = 1
# DATA_START_ROW = 2
# router = APIRouter()

# @router.get("/optics-e2e-status", tags=["Optics-Download"])
# def download_optics_e2e_status():

#     OPTICS_TEMPLATE_PATH = r"Provisioning\Sample_MW PROVISIONING_Provisoning_Update_Template (1).xlsx"

#     if not os.path.exists(OPTICS_TEMPLATE_PATH):
#         raise HTTPException(500, "Optics template not found")

#     os.makedirs(TEMP_DIR, exist_ok=True)

#     temp_file = os.path.join(
#         TEMP_DIR, f"OPTICS_{uuid4().hex}.xlsx"
#     )
#     shutil.copy(OPTICS_TEMPLATE_PATH, temp_file)

#     wb = load_workbook(temp_file)
#     ws = wb.active

#     # Map Excel headers → DB fields
#     excel_columns = {}
#     for col in range(1, ws.max_column + 1):
#         header = ws.cell(row=HEADER_ROW, column=col).value
#         if header in OPTICS_EXCEL_COLUMN_MAP:
#             excel_columns[col] = OPTICS_EXCEL_COLUMN_MAP[header]

#     if not excel_columns:
#         raise HTTPException(500, "No Optics columns matched in Excel")

#     db = SessionLocal()
#     try:
#         rows = db.query(Data).all()
#     finally:
#         db.close()

#     row_idx = DATA_START_ROW
#     for row in rows:
#         for col_idx, db_field in excel_columns.items():
#             ws.cell(row=row_idx, column=col_idx).value = getattr(row, db_field)
#         row_idx += 1

#     wb.save(temp_file)

#     return FileResponse(
#         temp_file,
#         filename="Optics_E2E_Status.xlsx",
#         media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#     )
