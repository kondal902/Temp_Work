import pyodbc
with open("Data_import.txt", "r") as f:
    xml_file_list = f.readlines()
    for xml_file_name in xml_file_list:
        xml_file=xml_file_name.strip();       
        xml_extn=".xml"
        xsd_extn=".xsd"
        xml_file_path=xml_file+xml_extn
        xml_file_xsd=xml_file+xsd_extn
        print(xml_file)
        print(xml_file_path)
        print(xml_file_xsd)
        cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host="100.76.143.26:1421";Service Name="FCUBSJC7PDB";User ID="FCUBSUSR";Password="FCUBSUSR"')           
        cursor = cnxn.cursor()	
        sql= "select FC_FUNCTION_ID from gwtm_operations_master where (FS_REQ_XSD=? OR PK_RES_XSD=? OR FS_RES_XSD=? OR IO_REQ_XSD=?)"
        cursor.execute(sql,xml_file_xsd,xml_file_xsd,xml_file_xsd,xml_file_xsd);
        row=cursor.fetchone();
        print(row[0]);

        