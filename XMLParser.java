package jbr.springmvc;

import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import java.io.File;
import java.util.StringTokenizer;

public class XMLParser {
	public static void main(String[] args) {
		try {
			//System.out.println(
				//	"BLOCK_NAME|BLK_FIELD_ORDER|FIELD_NAME|FIELD_SIZE|DATATYPE|FLD_ANNOTATION|MAX_LENGTH|DEFAULT_VALUE|DISPLAY_TYPE|DBC|DBT|ATTR_NAME|ATTR_VALUE|FUNCTION_ID");
			// File inputFile = new File("D:\\Vins\\Work\\Aiful\\tempwork\\inputfile.xml");
			// File inputFile = new
			// File("D:\\01_WORK\\AIFUL\\JCFCUBSJP_RAD_XMLS\\CLDACCNT_RAD.xml");
			
			String string="CLDACCDT|CLDADCAU|CLDADCHG|CLDEVDRY|CLDINADT|CLDISTAU|CLDISTCH|CLDLQSPN|CLDMDSAU|CLDMSTAU|CLDMSTCH|STDNSFQY|STDNSMNT";
			StringTokenizer stringTokenizer=new StringTokenizer(string,"|");
			
			int count = stringTokenizer.countTokens();
			for (int k=0; k<count; k++) {
			   // System.out.println(stringTokenizer.nextToken());			
			//String fn_id = "CLDINANT";
			String fn_id = stringTokenizer.nextToken();
			String File_name="D:\\01_WORK\\AIFUL\\XSD_Data\\JCFCUBSJP_RAD_XMLS\\"+fn_id+"_RAD.xml";
			//System.out.println("File_name:"+File_name);
			File inputFile = new File(File_name);			
			DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
			Document doc = dBuilder.parse(inputFile);
			doc.getDocumentElement().normalize();
			NodeList blockNodes = doc.getElementsByTagName("RAD_DATA_BLOCKS");
			
			for (int i = 0; i < blockNodes.getLength(); i++) {
				Node blockNode = blockNodes.item(i);
				// System.out.println("######################Block
				// Start###############################");
				if (blockNode.getNodeType() == Node.ELEMENT_NODE) {
					Element blockElement = (Element) blockNode;

					/*
					 * System.out.println( "Block Name : " +
					 * blockElement.getElementsByTagName("BLOCK_NAME").item(0).getTextContent());
					 */
					NodeList fieldsList = blockElement.getElementsByTagName("RAD_BLK_FIELDS");

					String result = "";
					String finresult = "";
					String annotation = "";
					String Block_name = "";
					String Blk_Field_Order="";
					String Field_name="";
					String Field_size="";
					String Data_type="";
					String Max_length="";
					String Default_Value="";
					String Display_Type="";					
					String DBC="";
					String DBT="";
					for (int j = 0; j < fieldsList.getLength(); j++) {
						// System.out.println("######################Field Start
						// ###############################");
						Node fieldNode = fieldsList.item(j);
						result = "";
						finresult = "";
						annotation = "";
						
						if (fieldNode.getNodeType() == Node.ELEMENT_NODE) {
							Element fieldElement = (Element) fieldNode;
							try {

								if (fieldElement.getElementsByTagName("FLD_ANNOTATION").item(0)
										.getTextContent() != null) {
									annotation = fieldElement.getElementsByTagName("FLD_ANNOTATION").item(0)
											.getTextContent();
								}

							} catch (Exception e) {
								annotation = "";
							}						
							
							try {

								if (blockElement.getElementsByTagName("BLOCK_NAME").item(0).getTextContent() != null) {
									Block_name = blockElement.getElementsByTagName("BLOCK_NAME").item(0).getTextContent();
								}

							} catch (Exception e) {
								Block_name = "";
							}
							
							try {

								if (fieldElement.getElementsByTagName("BLK_FIELD_ORDER").item(0)
										.getTextContent() != null) {
									Blk_Field_Order = fieldElement.getElementsByTagName("BLK_FIELD_ORDER").item(0)
											.getTextContent();
								}

							} catch (Exception e) {
								Blk_Field_Order = "";
							}							
							try {

								if (fieldElement.getElementsByTagName("FIELD_NAME").item(0)
										.getTextContent() != null) {
									Field_name = fieldElement.getElementsByTagName("FIELD_NAME").item(0)
											.getTextContent();
								}

							} catch (Exception e) {
								Field_name = "";
							}
							
							try {

								if (fieldElement.getElementsByTagName("FIELD_SIZE").item(0)
										.getTextContent() != null) {
									Field_size = fieldElement.getElementsByTagName("FIELD_SIZE").item(0)
											.getTextContent();
								}

							} catch (Exception e) {
								Field_size = "";
							}
							
							
							try {

								if (fieldElement.getElementsByTagName("DATA_TYPE").item(0)
										.getTextContent() != null) {
									Data_type = fieldElement.getElementsByTagName("DATA_TYPE").item(0)
											.getTextContent();
								}

							} catch (Exception e) {
								Data_type = "";
							}

							try {

								if (fieldElement.getElementsByTagName("MAX_LENGTH").item(0)
										.getTextContent() != null) {
									Max_length = fieldElement.getElementsByTagName("MAX_LENGTH").item(0)
											.getTextContent();
								}

							} catch (Exception e) {
								Max_length = "";
							}
							
							
							try {

								if (fieldElement.getElementsByTagName("DEFAULT_VALUE").item(0)
										.getTextContent() != null) {
									Default_Value = fieldElement.getElementsByTagName("DEFAULT_VALUE").item(0)
											.getTextContent();
								}

							} catch (Exception e) {
								Default_Value = "";
							}
							
							try {

								if (fieldElement.getElementsByTagName("DISPLAY_TYPE").item(0)
										.getTextContent() != null) {
									Display_Type = fieldElement.getElementsByTagName("DISPLAY_TYPE").item(0)
											.getTextContent();
								}

							} catch (Exception e) {
								Display_Type = "";
							}
							

							try {

								if (fieldElement.getElementsByTagName("DBC").item(0)
										.getTextContent() != null) {
									Display_Type = fieldElement.getElementsByTagName("DBC").item(0)
											.getTextContent();
								}

							} catch (Exception e) {
								Display_Type = "";
							}
							
							try {

								if (fieldElement.getElementsByTagName("DBT").item(0)
										.getTextContent() != null) {
									Display_Type = fieldElement.getElementsByTagName("DBT").item(0)
											.getTextContent();
								}

							} catch (Exception e) {
								Display_Type = "";
							}

							
							
							result = Block_name 
									+ "|" + Blk_Field_Order
									+ "|" + Field_name
									+ "|" + Field_size
									+ "|" + Data_type 
									+ "|" + annotation + "|"
									+ Max_length + "|"
									+ Default_Value + "|"
									+ Display_Type + "|"
									+ DBC + "|"
									+ DBT;

							/*
							 * if
							 * (fieldElement.getElementsByTagName("DISPLAY_TYPE").item(0).getTextContent()
							 * .contains("CHECKBOX") ||
							 * fieldElement.getElementsByTagName("DISPLAY_TYPE").item(0).getTextContent()
							 * .contains("RADIO") ||
							 * fieldElement.getElementsByTagName("DISPLAY_TYPE").item(0).getTextContent()
							 * .contains("SELECT")) { // System.out.println("Inside the IF condition");
							 * NodeList childList =
							 * fieldElement.getElementsByTagName("RAD_FIELD_CUSTOM_ATTRS"); for (int k = 0;
							 * k < fieldElement.getElementsByTagName("RAD_FIELD_CUSTOM_ATTRS") .getLength();
							 * k++) { finresult = ""; Node childNode = childList.item(k); if
							 * (childNode.getNodeType() == Node.ELEMENT_NODE) { Element childElement =
							 * (Element) childNode;
							 * 
							 * System.out.println("\t\tAttribute Name : " + childElement
							 * .getElementsByTagName("ATTR_NAME").item(0).getTextContent());
							 * System.out.println("\t\tAttribute Value : " + childElement
							 * .getElementsByTagName("ATTR_VALUE").item(0).getTextContent());
							 * 
							 * finresult = result + "|" +
							 * childElement.getElementsByTagName("ATTR_NAME").item(0) .getTextContent() +
							 * "|" + childElement.getElementsByTagName("ATTR_VALUE").item(0)
							 * .getTextContent(); System.out.println(finresult); }
							 * 
							 * }
							 * 
							 * } if (finresult == null || finresult == "") { finresult = result + "||"; }
							 */
							//finresult = result + "||";
							finresult = result + "|||" + fn_id;
							System.out.println(finresult);
						}

					}
				}
				// System.out.println("######################Block End
				// ###############################");
			}
		}	
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
