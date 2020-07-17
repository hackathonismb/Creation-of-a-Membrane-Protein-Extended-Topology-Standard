from collections import namedtuple
from xml.etree.ElementTree import ElementTree 


class UniprotXMLParser: 
    
    def __init__(self, xml_data):
        self.xml_data = xml_data 
        self.URI = '{http://uniprot.org/uniprot}'
        self.pdbid = None

        
        
    def parse_xml(self):
        # going threough all the elments within the entyry tag 
        
        pdb_ids = []
        
        for entry in self.xml_data[0]:
            elemnt_dict = entry.attrib
            next_el = entry.tail
            print(next_el)
            search_type = elemnt_dict.get('type') 

            
            # filtering and only geting pdb data 
            if search_type == 'PDB':
                pdb_id = elemnt_dict.get('id')
                if pdb_id not in pdb_ids:
                    pdb_ids.append(pdb_id)
                
            
            
                    
            
                    
                    
    def compile(self):
        """ compiles data into """
        tuple_setup = namedtuple("UniprotXML", 'id methods resolution')
        compile_data = tuple_setup()

        pass
        
class ParseUniprotGFF():
    
    def __init__(self):
        pass