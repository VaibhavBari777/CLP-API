# from fastapi import APIRouter, HTTPException
# from fastapi.responses import FileResponse
# from sqlalchemy import select
# from database import SessionLocal
# from models import Data
# from openpyxl import load_workbook
# import shutil
# import os
# from uuid import uuid4

# router = APIRouter()
# EXCEL_COLUMN_MAP = {
#     "Circle": "Circle_Name",
#     "Project": "Project_Name",
#     "Site ID": "Site_ID",
#     "Vendor": "BTS_Vendor",
#     "NSS ID": "NSS_ID",
#     "MW OSM": "mw_osm",
#     "Optics OSM": "optics_osm",
#     "IP CR": "code_cr_details_ip_cr",

# }


# MW_TEMPLATE_PATH = r"Provisioning/Sample_MW PROVISIONING_Provisoning_Update_Template (1).xlsx"
# TEMP_DIR = "temp_downloads"
# HEADER_ROW = 1
# DATA_START_ROW = 2
# @router.get("/mw-provsioning", tags=["MW-Download"])
# def download_mw_e2e_status():

#     if not os.path.exists(MW_TEMPLATE_PATH):
#         raise HTTPException(500, "Template not found")

#     os.makedirs(TEMP_DIR, exist_ok=True)

#     temp_file = os.path.join(
#         TEMP_DIR, f"MW_E2E_{uuid4().hex}.xlsx"
#     )
#     shutil.copy(MW_TEMPLATE_PATH, temp_file)

#     wb = load_workbook(temp_file)
#     ws = wb.active

#     # Map Excel headers → DB fields
#     excel_columns = {}
#     for col in range(1, ws.max_column + 1):
#         header = ws.cell(row=1, column=col).value
#         if header in EXCEL_COLUMN_MAP:
#             excel_columns[col] = EXCEL_COLUMN_MAP[header]

#     if len(excel_columns) != 14:
#         raise HTTPException(
#             500,
#             f"Expected 14 columns, found {len(excel_columns)}"
#         )

#     db = SessionLocal()
#     try:
#         rows = db.query(Data).all()
#     finally:
#         db.close()

#     row_idx = 2
#     for row in rows:
#         for col_idx, db_field in excel_columns.items():
#             ws.cell(row=row_idx, column=col_idx).value = getattr(row, db_field)
#         row_idx += 1

#     wb.save(temp_file)

#     return FileResponse(
#         temp_file,
#         filename="MW_E2E_Status.xlsx",
#         media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#     )
