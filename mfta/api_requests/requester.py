import urllib.error
import requests
from xml.etree import ElementTree
from collections import namedtuple

from mfta.debugg.errors import QueryRequestError, QueryReturnedZero
from mfta.parser.parseXML import UniprotXMLParser


class UnipRequests:

    
    def __init__(self, acno, species, name=None, reviewed=True):
        self.acno       = acno
        self.species    = species
        self.reviewed   = "Reviwed" if True else "Not Reviwed"
        self.name       = name
        self.baseURL    = "http://www.uniprot.org/uniprot/"
        self.sequence   = None
        self.accession  = None
        self.pdbids     = None


    def search_by_name(self):
        """ returns a list of unirpot id associated with the querey"""
        payload ={'query':'name:"{}" AND taxonomy:{} AND reviewed:{}'.format(self.name, self.species, self.reviwed)
                  , 'format':'fasta'} 

        result = requests.get(self.baseURL, params=payload)
        data = result.text.strip().split('>')
        if not result.ok:
            raise QueryRequestError("Error encountered [CODE: {}".format(result.status_code))

        elif len(data) == 0 or result.status_code == 400:
            raise QueryReturnedZero("No results were found")
       
        else: 
            accession = []
            query     = []
            seqs      = []
            for raw_data in data:

                if len(raw_data) == 0: 
                    continue
                
                fasta_data = raw_data.split('\n')
                header   = fasta_data[0].split('|')
                accs_num = header[1]
                title    = header[2] 
                fasta_seq  = ''.join(fasta_data[1:])
                
                accession.append(accs_num)
                query.append(title)
                #NOTE: odd artifact is formed when parsing (empty list element)
                if not len(fasta_seq) == 0:
                    seqs.append(fasta_seq)
                    
            # updating instance varaible      
            self.query      = query
            self.accession  = accession
            self.fasta_seqs = seqs

            return self.fasta_seqs, self.accession, self.query

    def collect(self): 
        """ conducts a search via accension and retrieves data """

        # TODO: Figure out how to get the URI without hard coding it 
        
        # important links for requesting data 
        xml_file = self.baseURL + self.acno + '.xml'
        gff_file = self.baseURL + self.acno + '.gff'
        fasta_file = self.baseURL + self.acno +'.fasta'
        
        # requesting data 
        xml_resp = requests.get(xml_file)
        gff_resp = requests.get(gff_file)
        fasta_resp = requests.get(fasta_file)

        # parssing the obtained data 
        if not xml_resp.ok: 
            raise QueryRequestError
        
        pdb_ids = []
        tree = ElementTree.fromstring(xml_resp.content)
        for elm in tree.iter("{http://uniprot.org/uniprot}dbReference"):
            search_type = elm.get('type')
            if search_type == 'PDB':
                pdbid = elm.get('id')
                if pdbid not in pdb_ids:
                    pdb_ids.append(pdbid)
        
        sequence = [ sequence.text for sequence in tree.iter("{http://uniprot.org/uniprot}sequence")]

        self.sequence = ''.join(sequence)
        self.pdbids = pdb_ids
        
        return self.sequence, self.pdbids


    def describe(self): 
        """ Returns a description of your request object """
        
        details = {
            "Accession" : "{}".format(self.acno    ),
            "Species"   : "{}".format(self.species ),
            "reviewed"  : "{}".format(self.reviewed),
            "sequence"  : "{}".format(self.sequence),
            "pdb_ids"   : "{}".format(self.pdbids  )
        }

        print("this is print in function", details)
        return details

    def compile_data(self):
        """ compiles the data into named tuple"""
    
        setup_nt = namedtuple(self.acno, "acno species sequence pdbid reviewed") 
        compiled_data = setup_nt(self.acno,
                                 self.species,
                                 self.sequence,
                                 self.pdbids,
                                 self.reviewed)
        return compiled_data

class RCSBRequest:
    

    def __init__(self, pdb_id):
        self.pdb_id   = pdb_id
        self.chains   = None
        self.HBregion = None
        self.TMdomain = None
        self.stalk    = None
    

    # TODO: talk with ravi about this 
    def collect_rcsb(self):
        self.chains   = ["A", "B", "C"]
        self.HBregion = None
        self.TMdomain = None
        self.stalk    = None
        
        
    def compile_data(self):
        """ Creates a named tuple of the data """

        setup_nt = namedtuple(self.pdb_id, "species sequence pdbid reviewed") 
        compiled_data = setup_nt(self.pdb_id,
                                 self.chains,
                                 self.HBregion,
                                 self.TMdomain,
                                 self.staldomain)
        return compiled_data

        
class OPMRequests:
    """ API that connect to the OPM server database and extract data """ 
    def __init__(self):
        pass


class PDBTMRequests:
    """ Connects to the PDBTM server in order to extract data """
    
     
    def __init__(self):
        pass 
