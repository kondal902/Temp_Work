import xml.etree.ElementTree as ET
import pyodbc
import os
funid_db_data = {}
full_db_data  = {}
text_to_append ='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'''
cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host="100.76.143.26:1421";Service Name="FCUBSJC7PDB";User ID="FCUBSUSR";Password="FCUBSUSR"')           
cursor = cnxn.cursor()	
#Getting all the distinct fields and description, store in dictionary
sql= "select distinct field_name,fld_annotation From fcubsjc_dev_cmt.cstb_rad_fields where fld_annotation is not null"
cursor.execute(sql);
for row in cursor:
    full_db_data[row[0]]= row[1];  
cursor.close()
#Read the file name one by one in loop
with open("Data_import.txt", "r") as f:
    xml_file_list = f.readlines()
    for xml_file_name in xml_file_list:
        xml_file=xml_file_name.strip();       
        xml_extn=".xml"
        xsd_extn=".xsd"
        xml_file_path="AnnotationXML/"+xml_file+xml_extn
        xml_file_xsd=xml_file+xsd_extn
        #print(xml_file)
        #print(xml_file_path)
        #print(xml_file_xsd)        
        cursor = cnxn.cursor()	
        #Getting the function id based on file name
        sql= "select FC_FUNCTION_ID from gwtm_operations_master where (FS_REQ_XSD=? OR PK_RES_XSD=? OR FS_RES_XSD=? OR IO_REQ_XSD=?)"
        cursor.execute(sql,xml_file_xsd,xml_file_xsd,xml_file_xsd,xml_file_xsd);
        try:
            row=cursor.fetchone();
            function_id=row[0];
        except:
            print("No Funciton id avaiable"+xml_file_xsd)
            #continue;
        cursor.close();
        print(xml_file_path)
        try:
        #parsing the xml file
            tree = ET.parse(xml_file_path)
        except:
            print("File not found-"+xml_file_path);
            continue;
        root = tree.getroot()        
        cursor = cnxn.cursor()
        #Getting all the distinct fields and description, store in dictionary based on function id	
        sql= "select distinct field_name,fld_annotation from fcubsjc_dev_cmt.cstb_rad_fields where function_id IN ('ALL',?) and fld_annotation is not null"
        cursor.execute(sql,function_id);
        for row in cursor:       
                funid_db_data[row[0]]=row[1];
        cursor.close()
        NodeDetailslists = root.iter('NodeDetails');
        for node in NodeDetailslists:
            #print(node.find('./NodeName').text);
            #Getting the field Name
            nodename=node.find('./NodeName').text;
            try:
                xsd_node_2=node.find('./XSD_NODE_2').text;
            except:
                print("FCUBS_HEADER/FCUBS_BODY is not available:");
                xsd_node_2="";
            lv_comment="";
            try:
                lv_comment=node.find('./Comment').text;
            except:
                print("comment tag is not available:"+nodename);
                continue;
            #print(lv_comment);
            db_comment="";
            try:
                db_comment=funid_db_data[nodename];
            except:
                try:
                    #based on function id, if field value is not there, getting the same from all the distinct fields
                    db_comment=full_db_data[nodename];
                except:
                    db_comment=None;
            # If existing comment is null and db_comment is not null then update the comment tag
            if lv_comment is None and db_comment is not None:                
                node.find('./Comment').text=db_comment; 
            #print(node.find('./Comment').text);
        updated_xml="Updated_xmls/"+xml_file_path;                        
        tree.write(updated_xml)
        dummy_file = updated_xml + '.bak'
        with open(updated_xml, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
            write_obj.write(text_to_append + '\n');
            for line in read_obj:
                 write_obj.write(line.replace("&gt;",">"))
        os.remove(updated_xml)
        os.rename(dummy_file,updated_xml)
