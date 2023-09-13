import xml.dom.minidom as md
import pyodbc
def main():
    
    file = md.parse("CL-CreateAccount-Req-Full-MSG.xml")
    print("Hello")
    print( file.firstChild.tagName);
    cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host="100.76.143.26:1421";Service Name="FCUBSJC7PDB";User ID="FCUBSUSR";Password="FCUBSUSR"')           
    NodeDetailslists = file.getElementsByTagName( "NodeDetails")
    print(NodeDetailslists.length)
    i=0;    
    for nodelist in NodeDetailslists:
        nodename= nodelist.getElementsByTagName("NodeName")[0].firstChild.data;
        #nodename= file.getElementsByTagName("NodeName")[i].childNodes[0].nodeValue;
        xsd_node_2=file.getElementsByTagName("XSD_NODE_2")[i].childNodes[0].nodeValue; 
        try:            
            lv_comment=file.getElementsByTagName("Comment")[i].childNodes[0].nodeValue;
        except:
            i=i+1;
            print("no comment");
            continue;
        print("i:"+str(i));
        print (nodename); 
        print( xsd_node_2);
        if xsd_node_2 == "FCUBS_BODY" :
            cursor = cnxn.cursor()	
            sql= "select FLD_ANNOTATION from fcubsjc_dev_cmt.cstb_rad_fields where field_name= ? and function_id='CLDACCNT' and rownum<2;"
            cursor.execute(sql, (nodename))
            row = cursor.fetchone();
            db_comment="";
            if row is not None:
                db_comment=row[0];
            else:
                db_comment="None";
            print(db_comment);
            print("before comment"+file.getElementsByTagName("Comment")[i].childNodes[0].nodeValue);        
            file.getElementsByTagName("Comment")[i].childNodes[0].nodeValue=db_comment;
            print("after comment"+file.getElementsByTagName("Comment")[i].childNodes[0].nodeValue);
        
        i=i+1;

    with open( "CL-CreateAccount-Req-Full-MSG_2.xml", "w" ) as fs:   
        fs.write( file.toxml() )
        fs.close() 
  
if __name__=="__main__":
    main();