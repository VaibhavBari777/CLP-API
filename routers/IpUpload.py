IP_COLUMN_MAP = {
    "NSS ID\n(Min & Max Length=10)": "NSS_ID",                     # mandatory
    # 2G BTS IPv4
    "2G-BTS Vlan": "_2g_bts_ipv4_address_2g_bts_vlan",
    "2G-BTS Network": "_2g_bts_ipv4_address_2g_bts_network",
    "2G-BTS Subnet": "_2g_bts_ipv4_address_2g_bts_subnet",
    "2G-BTS IP": "_2g_bts_ipv4_address_2g_bts_ip",
    "2G-BTS GW": "_2g_bts_ipv4_address_2g_bts_gw",

    # 2G BTS IPv6
    "2G-BTS Network.1": "_2g_bts_ipv6_address_2g_bts_network",
    "2G-BTS Subnet.1": "_2g_bts_ipv6_address_2g_bts_subnet",
    "2G-BTS IP.1": "_2g_bts_ipv6_address_2g_bts_ip",
    "2G-BTS GW.1": "_2g_bts_ipv6_address_2g_bts_gw",

    # 2G OAM IPv4
    "2G-BTS Vlan.1": "_2g_oam_ipv4_address_2g_bts_vlan",
    "2G-BTS Network.2": "_2g_oam_ipv4_address_2g_bts_network",
    "2G-BTS Subnet.2": "_2g_oam_ipv4_address_2g_bts_subnet",
    "2G-BTS IP.2": "_2g_oam_ipv4_address_2g_bts_ip",
    "2G-BTS GW.2": "_2g_oam_ipv4_address_2g_bts_gw",

    # 2G OAM IPv6
    "2G-BTS Network.3": "_2g_oam_ipv6_address_2g_bts_network",
    "2G-BTS Subnet.3": "_2g_oam_ipv6_address_2g_bts_subnet",
    "2G-BTS IP.3": "_2g_oam_ipv6_address_2g_bts_ip",
    "2G-BTS GW.3": "_2g_oam_ipv6_address_2g_bts_gw",

    # 4G OAM IPv4
    "OAM Vlan": "_4g_oam_ipv4_address_oam_vlan",
    "OAM Network": "_4g_oam_ipv4_address_oam_netowrk",
    "OAM Subnet": "_4g_oam_ipv4_address_oam_subnet",
    "OAM IP": "_4g_oam_ipv4_address_oam_ip",
    "OAM GW": "_4g_oam_ipv4_address_oam_gw",

    # 4G OAM IPv6
    "OAM Network.1": "_4g_oam_ipv6_address_oam_netowrk",
    "OAM Subnet.1": "_4g_oam_ipv6_address_oam_subnet",
    "OAM IP.1": "_4g_oam_ipv6_address_oam_ip",
    "OAM GW.1": "_4g_oam_ipv6_address_oam_gw",

    # 4G S1-C IPv4
    "S1-C Vlan": "_4g_s1_c_ipv4_address_s1_c_vlan",
    "S1-C Network": "_4g_s1_c_ipv4_address_s1_c_network",
    "S1-C Subnet": "_4g_s1_c_ipv4_address_s1_c_subnet",
    "S1-C IP": "_4g_s1_c_ipv4_address_s1_c_ip",
    "S1-C GW": "_4g_s1_c_ipv4_address_s1_c_gw",

    # 4G S1-C IPv6
    "S1-C Network.1": "_4g_s1_c_ipv6_address_s1_c_network",
    "S1-C Subnet.1": "_4g_s1_c_ipv6_address_s1_c_subnet",
    "S1-C IP.1": "_4g_s1_c_ipv6_address_s1_c_ip",
    "S1-C GW.1": "_4g_s1_c_ipv6_address_s1_c_gw",

    # 4G S1-U IPv4
    "S1-U Vlan": "_4g_s1_u_ipv4_address_s1_u_vlan",
    "S1-U Network": "_4g_s1_u_ipv4_address_s1_u_network",
    "S1_U Subnet": "_4g_s1_u_ipv4_address_s1_u_subnet",
    "S1-U IP": "_4g_s1_u_ipv4_address_s1_u_ip",
    "S1-U GW": "_4g_s1_u_ipv4_address_s1_u_gw",

    # 4G S1-U IPv6
    "S1-U Network.1": "_4g_s1_u_ipv6_address_s1_u_network",
    "S1_U Subnet.1": "_4g_s1_u_ipv6_address_s1_u_subnet",
    "S1-U IP.1": "_4g_s1_u_ipv6_address_s1_u_ip",
    "S1-U GW.1": "_4g_s1_u_ipv6_address_s1_u_gw",

    # 5G OAM
    "OAM Vlan.1": "_5g_oam_ipv6_address_oam_vlan",
    "OAM Network.2": "_5g_oam_ipv6_address_oam_netowrk",
    "OAM Subnet.2": "_5g_oam_ipv6_address_oam_subnet",
    "OAM IP.2": "_5g_oam_ipv6_address_oam_ip",
    "OAM GW.2": "_5g_oam_ipv6_address_oam_gw",

    # 5G S1-C
    "S1-C Vlan.1": "_5g_s1_c_ipv6_address_s1_c_vlan",
    "S1-C Network.2": "_5g_s1_c_ipv6_address_s1_c_network",
    "S1-C Subnet.2": "_5g_s1_c_ipv6_address_s1_c_subnet",
    "S1-C IP.2": "_5g_s1_c_ipv6_address_s1_c_ip",
    "S1-C GW.2": "_5g_s1_c_ipv6_address_s1_c_gw",

    # 5G S1-U
    "S1-U Vlan.1": "_5g_s1_u_ipv6_address_s1_u_vlan",
    "S1-U Network.2": "_5g_s1_u_ipv6_address_s1_u_network",
    "S1-U Subnet": "_5g_s1_u_ipv6_address_s1_u_subnet",
    "S1-U IP.2": "_5g_s1_u_ipv6_address_s1_u_ip",
    "S1-U GW.2": "_5g_s1_u_ipv6_address_s1_u_gw",

    # CR Details
    "IP Plan Received Status(Yes/No/NR)": "code_cr_details_ip_plan_received_status",
    "IP CR": "code_cr_details_ip_cr",
    "IP Remarks": "code_cr_details_ip_remarks",
    "E2E(Yes/No)": "code_cr_details_e2e",
}

# from fastapi import HTTPException, APIRouter, UploadFile, File
# import pandas as pd
# from models import Data
# from database import SessionLocal
# import os

# router = APIRouter(prefix="/ip-upload")

# # ---------------- HELPER VALIDATOR ----------------
# def validate_section(
#     df,
#     vlan_col,
#     ipv4_ip_col=None,
#     ipv4_gw_col=None,
#     ipv6_ip_col=None,
#     ipv6_gw_col=None,
#     section_name="",
#     ipv4_allowed=True,
#     ipv6_allowed=True
# ):
#     """
#     Validation rules:
#     - VLAN missing → skip IP/GW check
#     - VLAN present → IP & GW must be filled for either IPv4 or IPv6 (IPv4/IPv6 optional for 2G/4G, IPv6 only for 5G)
#     """
#     for idx, row in df.iterrows():
#         vlan = row.get(vlan_col)

#         # VLAN missing → skip
#         if pd.isna(vlan):
#             for col in [ipv4_ip_col, ipv4_gw_col, ipv6_ip_col, ipv6_gw_col]:
#                 if col and col in df.columns:
#                     df.at[idx, col] = pd.NA
#             continue

#         ipv4_ok = False
#         ipv6_ok = False

#         # IPv4 validation
#         if ipv4_allowed and ipv4_ip_col and ipv4_gw_col:
#             ip4 = row.get(ipv4_ip_col)
#             gw4 = row.get(ipv4_gw_col)
#             if pd.notna(ip4) and pd.notna(gw4):
#                 ipv4_ok = True
#             elif pd.notna(ip4) or pd.notna(gw4):
#                 raise HTTPException(
#                     400,
#                     f"{section_name} IPv4 IP/GW mismatch at row {idx+1}"
#                 )

#         # IPv6 validation
#         if ipv6_allowed and ipv6_ip_col and ipv6_gw_col:
#             ip6 = row.get(ipv6_ip_col)
#             gw6 = row.get(ipv6_gw_col)
#             if pd.notna(ip6) and pd.notna(gw6):
#                 ipv6_ok = True
#             elif pd.notna(ip6) or pd.notna(gw6):
#                 raise HTTPException(
#                     400,
#                     f"{section_name} IPv6 IP/GW mismatch at row {idx+1}"
#                 )

#         # VLAN present → at least one IP/GW pair required
#         if not (ipv4_ok or ipv6_ok):
#             raise HTTPException(
#                 400,
#                 f"{section_name}: VLAN present but no valid IP/GW at row {idx+1}"
#             )



# ---------------- API ----------------
# @router.post("/upload-ip-excel", tags=["IP-upload"])
# async def upload_ip_excel(file: UploadFile = File(...)):
#     temp_file = f"temp_{file.filename}"

#     with open(temp_file, "wb") as f:
#         f.write(await file.read())

#     try:
#         df = pd.read_excel(temp_file, skiprows=2)

#         # Rename columns
#         df.rename(columns=IP_COLUMN_MAP, inplace=True)
# # Normalize empty cells (CRITICAL FIX)
#         df = df.replace(r'^\s*$', pd.NA, regex=True)

#         # NSS_ID must exist
#         if "NSS_ID" not in df.columns:
#             raise HTTPException(400, "NSS_ID column missing")

#         # ---------- VALIDATIONS ----------
#        # 2G Sections
#         validate_section(
#             df,
#             "_2g_bts_ipv4_address_2g_bts_vlan",
#             "_2g_bts_ipv4_address_2g_bts_ip",
#             "_2g_bts_ipv4_address_2g_bts_gw",
#             "_2g_bts_ipv6_address_2g_bts_ip",
#             "_2g_bts_ipv6_address_2g_bts_gw",
#             "2G BTS"
#         )
#         validate_section(
#             df,
#             "_2g_oam_ipv4_address_2g_bts_vlan",
#             "_2g_oam_ipv4_address_2g_bts_ip",
#             "_2g_oam_ipv4_address_2g_bts_gw",
#             "_2g_oam_ipv6_address_2g_bts_ip",
#             "_2g_oam_ipv6_address_2g_bts_gw",
#             "2G OAM"
#         )

#         # 4G Sections
#         validate_section(
#             df,
#             "_4g_oam_ipv4_address_oam_vlan",
#             "_4g_oam_ipv4_address_oam_ip",
#             "_4g_oam_ipv4_address_oam_gw",
#             "_4g_oam_ipv6_address_oam_ip",
#             "_4g_oam_ipv6_address_oam_gw",
#             "4G OAM"
#         )
#         validate_section(
#             df,
#             "_4g_s1_c_ipv4_address_s1_c_vlan",
#             "_4g_s1_c_ipv4_address_s1_c_ip",
#             "_4g_s1_c_ipv4_address_s1_c_gw",
#             "_4g_s1_c_ipv6_address_s1_c_ip",
#             "_4g_s1_c_ipv6_address_s1_c_gw",
#             "4G S1-C"
#         )
#         validate_section(
#             df,
#             "_4g_s1_u_ipv4_address_s1_u_vlan",
#             "_4g_s1_u_ipv4_address_s1_u_ip",
#             "_4g_s1_u_ipv4_address_s1_u_gw",
#             "_4g_s1_u_ipv6_address_s1_u_ip",
#             "_4g_s1_u_ipv6_address_s1_u_gw",
#             "4G S1-U"
#         )

#         # 5G Sections (IPv6 only)
#         validate_section(
#             df,
#             "_5g_oam_ipv6_address_oam_vlan",
#             ipv4_allowed=False,
#             ipv6_ip_col="_5g_oam_ipv6_address_oam_ip",
#             ipv6_gw_col="_5g_oam_ipv6_address_oam_gw",
#             section_name="5G OAM"
#         )
#         validate_section(
#             df,
#             "_5g_s1_c_ipv6_address_s1_c_vlan",
#             ipv4_allowed=False,
#             ipv6_ip_col="_5g_s1_c_ipv6_address_s1_c_ip",
#             ipv6_gw_col="_5g_s1_c_ipv6_address_s1_c_gw",
#             section_name="5G S1-C"
#         )
#         validate_section(
#             df,
#             "_5g_s1_u_ipv6_address_s1_u_vlan",
#             ipv4_allowed=False,
#             ipv6_ip_col="_5g_s1_u_ipv6_address_s1_u_ip",
#             ipv6_gw_col="_5g_s1_u_ipv6_address_s1_u_gw",
#             section_name="5G S1-U"
#         )


#         # Replace NaN → None
#         df = df.where(pd.notnull(df), None)
#         records = df.to_dict(orient="records")

#         db = SessionLocal()
#         try:
#             for record in records:
#                 db_obj = db.query(Data).filter(
#                     Data.NSS_ID == record["NSS_ID"]
#                 ).first()

#                 if not db_obj:
#                     raise HTTPException(
#                         400,
#                         f"NSS_ID {record['NSS_ID']} not found"
#                     )

#                 for key, value in record.items():
#                     if key != "NSS_ID":
#                         setattr(db_obj, key, value)

#             db.commit()
#         except Exception:
#             db.rollback()
#             raise
#         finally:
#             db.close()

#     finally:
#         os.remove(temp_file)

#     return {
#         "message": "IP Excel data updated successfully",
#         "rows_processed": len(records)
#     }


from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from sqlalchemy.inspection import inspect
from database import SessionLocal
from models import Data

router = APIRouter(
    prefix="/ip",
    tags=["IP Upload"]
)

# -------------------------------
# HELPERS
# -------------------------------
def is_filled(v):
    return not pd.isna(v) and str(v).strip() != ""

def filter_df_to_model(df: pd.DataFrame):
    model_cols = {c.key for c in inspect(Data).attrs}
    return df[[c for c in df.columns if c in model_cols]]

# -------------------------------
# VALIDATION LOGIC
# -------------------------------
def validate_constraints(df: pd.DataFrame):
    errors = []

    mandatory = [
        "NSS_ID",
        "code_cr_details_ip_plan_received_status",
        "code_cr_details_ip_cr",
        "code_cr_details_e2e"
    ]

    # ----------------------------
    # 1. Mandatory column check
    # ----------------------------
    for col in mandatory:
        if col not in df.columns:
            errors.append({"row": None, "column": col, "error": "Missing column"})

    if errors:
        return errors

    # ----------------------------
    # 2. Row-wise validation
    # ----------------------------
    for idx, row in df.iterrows():
        row_no = idx + 4

        # Mandatory value check
        for col in mandatory:
            if not is_filled(row[col]):
                errors.append({
                    "row": row_no,
                    "column": col,
                    "error": "Mandatory value missing"
                })

        # ----------------------------
        # 2G / 4G VLAN groups
        # ----------------------------
        IPV4_IPV6_GROUPS = [
            {
                "name": "2G BTS",
                "vlan": "_2g_bts_ipv4_address_2g_bts_vlan",
                "ipv4_ip": "_2g_bts_ipv4_address_2g_bts_ip",
                "ipv4_gw": "_2g_bts_ipv4_address_2g_bts_gw",
                "ipv6_ip": "_2g_bts_ipv6_address_2g_bts_ip",
                "ipv6_gw": "_2g_bts_ipv6_address_2g_bts_gw",
            },
            {
                "name": "2G OAM",
                "vlan": "_2g_oam_ipv4_address_2g_bts_vlan",
                "ipv4_ip": "_2g_oam_ipv4_address_2g_bts_ip",
                "ipv4_gw": "_2g_oam_ipv4_address_2g_bts_gw",
                "ipv6_ip": "_2g_oam_ipv6_address_2g_bts_ip",
                "ipv6_gw": "_2g_oam_ipv6_address_2g_bts_gw",
            },
            {
                "name": "4G OAM",
                "vlan": "_4g_oam_ipv4_address_oam_vlan",
                "ipv4_ip": "_4g_oam_ipv4_address_oam_ip",
                "ipv4_gw": "_4g_oam_ipv4_address_oam_gw",
                "ipv6_ip": "_4g_oam_ipv6_address_oam_ip",
                "ipv6_gw": "_4g_oam_ipv6_address_oam_gw",
            },
            {
                "name": "4G S1-C",
                "vlan": "_4g_s1_c_ipv4_address_s1_c_vlan",
                "ipv4_ip": "_4g_s1_c_ipv4_address_s1_c_ip",
                "ipv4_gw": "_4g_s1_c_ipv4_address_s1_c_gw",
                "ipv6_ip": "_4g_s1_c_ipv6_address_s1_c_ip",
                "ipv6_gw": "_4g_s1_c_ipv6_address_s1_c_gw",
            },
            {
                "name": "4G S1-U",
                "vlan": "_4g_s1_u_ipv4_address_s1_u_vlan",
                "ipv4_ip": "_4g_s1_u_ipv4_address_s1_u_ip",
                "ipv4_gw": "_4g_s1_u_ipv4_address_s1_u_gw",
                "ipv6_ip": "_4g_s1_u_ipv6_address_s1_u_ip",
                "ipv6_gw": "_4g_s1_u_ipv6_address_s1_u_gw",
            }
        ]

        for g in IPV4_IPV6_GROUPS:
            if not is_filled(row.get(g["vlan"])):
                continue

            ipv4_ok = is_filled(row.get(g["ipv4_ip"])) and is_filled(row.get(g["ipv4_gw"]))
            ipv6_ok = is_filled(row.get(g["ipv6_ip"])) and is_filled(row.get(g["ipv6_gw"]))

            if not (ipv4_ok or ipv6_ok):
                errors.append({
                    "row": row_no,
                    "column": g["vlan"],
                    "error": f"{g['name']}: VLAN present but IP/GW missing"
                })

            elif ipv4_ok and ipv6_ok:
                errors.append({
                    "row": row_no,
                    "column": g["vlan"],
                    "error": f"{g['name']}: Dual stack not allowed"
                })

        # ----------------------------
        # 5G (IPv6 ONLY)
        # ----------------------------
        IP_5G_GROUPS = [
            {
                "name": "5G OAM",
                "vlan": "_5g_oam_ipv6_address_oam_vlan",
                "ip": "_5g_oam_ipv6_address_oam_ip",
                "gw": "_5g_oam_ipv6_address_oam_gw"
            },
            {
                "name": "5G S1-C",
                "vlan": "_5g_s1_c_ipv6_address_s1_c_vlan",
                "ip": "_5g_s1_c_ipv6_address_s1_c_ip",
                "gw": "_5g_s1_c_ipv6_address_s1_c_gw"
            },
            {
                "name": "5G S1-U",
                "vlan": "_5g_s1_u_ipv6_address_s1_u_vlan",
                "ip": "_5g_s1_u_ipv6_address_s1_u_ip",
                "gw": "_5g_s1_u_ipv6_address_s1_u_gw"
            }
        ]

        for g in IP_5G_GROUPS:
            if is_filled(row.get(g["vlan"])):
                if not (is_filled(row.get(g["ip"])) and is_filled(row.get(g["gw"]))):
                    errors.append({
                        "row": row_no,
                        "column": g["vlan"],
                        "error": f"{g['name']}: VLAN present but IPv6 IP/GW missing"
                    })

    return errors


# -------------------------------
# API ENDPOINT (UPDATE ONLY)
# -------------------------------
@router.post("/upload-excel")
async def upload_ip_excel(file: UploadFile = File(...)):
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(400, "Only Excel (.xlsx) allowed")

    try:
        df = pd.read_excel(file.file, header=2)
    except Exception:
        raise HTTPException(400, "Invalid Excel file")

    # Rename columns
    df.rename(columns=IP_COLUMN_MAP, inplace=True)

    # Validate
    errors = validate_constraints(df)
    if errors:
        raise HTTPException(status_code=400, detail=errors)

    # Keep only DB columns
    df = filter_df_to_model(df)

    db = SessionLocal()
    try:
        for _, row in df.iterrows():
            nss_id = row["NSS_ID"]

            # 🔑 FETCH EXISTING ROW
            obj = db.query(Data).filter(Data.NSS_ID == nss_id).first()

            if not obj:
                raise HTTPException(
                    status_code=400,
                    detail=f"NSS_ID {nss_id} not found in database"
                )

            # 🔁 UPDATE FIELDS
            for col, val in row.items():
                if col != "NSS_ID":
                    setattr(obj, col, None if pd.isna(val) else val)

        db.commit()
        
    except HTTPException:
        db.rollback()
        raise

    except Exception as e:
        db.rollback()
        raise HTTPException(500, str(e))

    finally:
        db.close()

    return {"message": "IP data updated successfully"}
