import xml.dom.minidom as md
import pyodbc
def main():
    file = md.parse("CL_TEST.xml")
    print("Hello")
    print( file.firstChild.tagName);
    cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host="100.76.143.26:1421";Service Name="FCUBSJC7PDB";User ID="FCUBSUSR";Password="FCUBSUSR"')       
    cursor = cnxn.cursor()	
    sql= "select FLD_ANNOTATION from fcubsjc_dev_cmt.cstb_rad_fields where field_name= ? and function_id='CLDACCNT' and rownum<2;"
    book_date="BOOKDT";
    cursor.execute(sql, (book_date))
    #cursor.execute("SELECT FLD_ANNOTATION FROM fcubsjc_dev_cmt.CSTB_RAD_FIELDS WHERE ROWNUM<2") 
    row = cursor.fetchall() 
    print(row)
    #while row:
    #    print (row)            
        #comment=row;
    #    row = cursor.fetchone(); 
    NodeDetailslists = file.getElementsByTagName( "NodeDetails")
    print(NodeDetailslists.length)
    i=0;    
    for nodelist in NodeDetailslists:
        nodename= nodelist.getElementsByTagName("NodeName")[0].firstChild.data;
        print (nodename);   

        file.getElementsByTagName("Comment")[i].childNodes[0].nodeValue="29"        
        #file.getElementsByTagName("Comment")[i].childNodes[0].nodeValue="row"; 
        
        #nodelist.getElementsByTagName("Comment")[0].firstChild.setUserData="29" ;   
        #print(xsd_node);       
        i=i+1;

    # modifying the value of a tag(here "age")
    #file.getElementsByTagName( "NodeDetails" )
   # for neighbor in file.getElementsByTagName('NodeDetails'):
    #    print(neighbor.firstChild)

    # writing the changes in "file" object to 
    # the "test.xml" file
    with open( "CL_TEST.xml", "w" ) as fs:   
        fs.write( file.toxml() )
        fs.close() 
  
if __name__=="__main__":
    main();