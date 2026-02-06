from sqlalchemy import Column , String , Integer
from database import Base
class Data(Base):
    __tablename__ = "Data"
    S_No =Column(Integer )
    Request_Date = Column(String)
    Tentative_On_Air_Date  = Column(String )
    Service_Type  = Column(String )
    Project_Name  = Column(String )
    Circle_Name  = Column(String )
    District_Name = Column(String)
    Town_Name  = Column(String)
    Site_ID  = Column(String )
    Infra_ID  = Column(String )
    NSS_ID = Column(String,primary_key=True,index =True)
    Site_Name= Column(String )
    RF_Cluster= Column(String )
    IPv4_IPv6_2G = Column(String )
    IPv4_IPv6_4G = Column(String )
    Final_Technology= Column(String )
    BTS_Vendor = Column(String )
    Site_2G_TMD_IP = Column(String )
    BSC_ID = Column(String )
    BSC_IP = Column(String )
    MME_ID = Column(String )
    MME_IP = Column(String )
    SGW_ID = Column(String )
    SGW_IP = Column(String )
    OSS_ID = Column(String )
    OSS_IP= Column(String )
    RFAI_Status = Column(String)
    
    
    
#optics 

    gne_optics_pop_mux_hostname_4g_5g = Column(String)
    gne_pop_mux_port_4g_5g = Column(String)
    gne_interface_remarks = Column(String)

    reference_vlan_existing_interface = Column(String)

    router_location_2g_4g_5g = Column(String)
    router_pop_nss_id_2g_4g_5g = Column(String)
    router_hostname_2g_4g_5g = Column(String)
    router_sb_port_2g_4g_5g = Column(String)

    sb_optics_pop_mux_hostname_sb_towards_cen = Column(String)
    sb_optics_pop_mux_ports_sb_towards_cen = Column(String)

    port_status_new_existing_2g_4g_5g = Column(String)

    optics_service_label = Column(String)
    main_path = Column(String)
    protection_path = Column(String)

    optics_plan_received_status = Column(String)   # 🔴 Mandatory (green)
    optics_osm = Column(String)
    optics_remarks = Column(String)
    
    #MW
    
    
    pop_nss_id = Column(String)
    pop_name = Column(String)
    mw_path_pop_to_node = Column(String)
    mw_oem = Column(String)
    media_type_mw_optics_router = Column(String)
    mw_dropping_idu_ne_name = Column(String)
    mw_dropping_idu_ne_port = Column(String)
    mw_port_type_electrical_optical = Column(String)
    mw_gne_idu_ne_name = Column(String)
    mw_gne_idu_port = Column(String)
    mw_port_status = Column(String)
    reference_vlan_site_id_existing_interface = Column(String)
    mw_plan_received_status = Column(String)
    mw_osm = Column(String)
    mw_remarks = Column(String)




#IP
    _2g_bts_ipv4_address_2g_bts_vlan = Column(String)
    _2g_bts_ipv4_address_2g_bts_network = Column(String)
    _2g_bts_ipv4_address_2g_bts_subnet = Column(String)
    _2g_bts_ipv4_address_2g_bts_ip = Column(String)
    _2g_bts_ipv4_address_2g_bts_gw = Column(String)

    _2g_bts_ipv6_address_2g_bts_network = Column(String)
    _2g_bts_ipv6_address_2g_bts_subnet = Column(String)
    _2g_bts_ipv6_address_2g_bts_ip = Column(String)
    _2g_bts_ipv6_address_2g_bts_gw = Column(String)
    
    _2g_oam_ipv4_address_2g_bts_vlan = Column(String)
    _2g_oam_ipv4_address_2g_bts_network = Column(String)
    _2g_oam_ipv4_address_2g_bts_subnet = Column(String)
    _2g_oam_ipv4_address_2g_bts_ip = Column(String)
    _2g_oam_ipv4_address_2g_bts_gw = Column(String)
    
    _2g_oam_ipv6_address_2g_bts_network = Column(String)
    _2g_oam_ipv6_address_2g_bts_subnet = Column(String)
    _2g_oam_ipv6_address_2g_bts_ip = Column(String)
    _2g_oam_ipv6_address_2g_bts_gw = Column(String)
    
    _4g_oam_ipv4_address_oam_vlan = Column(String)
    _4g_oam_ipv4_address_oam_netowrk = Column(String)
    _4g_oam_ipv4_address_oam_subnet = Column(String)
    _4g_oam_ipv4_address_oam_ip = Column(String)
    _4g_oam_ipv4_address_oam_gw = Column(String)
    

    _4g_oam_ipv6_address_oam_netowrk = Column(String)
    _4g_oam_ipv6_address_oam_subnet = Column(String)
    _4g_oam_ipv6_address_oam_ip = Column(String)
    _4g_oam_ipv6_address_oam_gw = Column(String)
    
    _4g_s1_c_ipv4_address_s1_c_vlan = Column(String)
    _4g_s1_c_ipv4_address_s1_c_network = Column(String)
    _4g_s1_c_ipv4_address_s1_c_subnet = Column(String)
    _4g_s1_c_ipv4_address_s1_c_ip = Column(String)
    _4g_s1_c_ipv4_address_s1_c_gw = Column(String)

    _4g_s1_c_ipv6_address_s1_c_network = Column(String)
    _4g_s1_c_ipv6_address_s1_c_subnet = Column(String)
    _4g_s1_c_ipv6_address_s1_c_ip = Column(String)
    _4g_s1_c_ipv6_address_s1_c_gw = Column(String)
    
    _4g_s1_u_ipv4_address_s1_u_vlan = Column(String)
    _4g_s1_u_ipv4_address_s1_u_network = Column(String)
    _4g_s1_u_ipv4_address_s1_u_subnet = Column(String)
    _4g_s1_u_ipv4_address_s1_u_ip = Column(String)
    _4g_s1_u_ipv4_address_s1_u_gw = Column(String)
    
    _4g_s1_u_ipv6_address_s1_u_network = Column(String)
    _4g_s1_u_ipv6_address_s1_u_subnet = Column(String)
    _4g_s1_u_ipv6_address_s1_u_ip = Column(String)
    _4g_s1_u_ipv6_address_s1_u_gw = Column(String)
    
    
    _5g_oam_ipv6_address_oam_vlan = Column(String)
    _5g_oam_ipv6_address_oam_netowrk = Column(String)
    _5g_oam_ipv6_address_oam_subnet = Column(String)
    _5g_oam_ipv6_address_oam_ip = Column(String)
    _5g_oam_ipv6_address_oam_gw = Column(String)
    
    _5g_s1_c_ipv6_address_s1_c_vlan = Column(String)
    _5g_s1_c_ipv6_address_s1_c_network = Column(String)
    _5g_s1_c_ipv6_address_s1_c_subnet = Column(String)
    _5g_s1_c_ipv6_address_s1_c_ip = Column(String)
    _5g_s1_c_ipv6_address_s1_c_gw = Column(String)
    
    _5g_s1_u_ipv6_address_s1_u_vlan = Column(String)
    _5g_s1_u_ipv6_address_s1_u_network = Column(String)
    _5g_s1_u_ipv6_address_s1_u_subnet = Column(String)
    _5g_s1_u_ipv6_address_s1_u_ip = Column(String)
    _5g_s1_u_ipv6_address_s1_u_gw = Column(String)
    
    code_cr_details_ip_plan_received_status = Column(String)
    code_cr_details_ip_cr= Column(String)
    code_cr_details_ip_remarks = Column(String)
    code_cr_details_e2e = Column(String)


    
    mw_osm_execution_status = Column(String)
    optics_osm_execution_status = Column(String)
    ip_cr_execution_status = Column(String)
    tx_e2e_readiness_status = Column(String)
    site_status = Column(String)
    code_e2e_status = Column(String)