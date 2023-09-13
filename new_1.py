import pyodbc
db_data ={}
cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host="100.76.143.26:1421";Service Name="FCUBSJC7PDB";User ID="FCUBSUSR";Password="FCUBSUSR"')           
cursor = cnxn.cursor()	
sql= "select distinct field_name,fld_annotation from fcubsjc_dev_cmt.cstb_rad_fields where function_id='CLDACCNT' and fld_annotation is not null"
cursor.execute(sql);
for row in cursor:
      try:
          old_len= len(db_data[row[0]]);  
      except:
           old_len=0;
      if old_len < len(row[1]):        
        db_data[row[0]]=row[1];
for i in db_data:
    print(i, db_data[i])
