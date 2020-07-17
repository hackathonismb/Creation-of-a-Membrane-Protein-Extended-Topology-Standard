import json


def write_mfta(outname, uniprot_data, rcsb_data):
    mfta = {}
    
    mfta['Accession number'] = uniprot_data.acno
    mfta['Entry status'] = uniprot_data.reviewed
    mfta['Sequence'] = uniprot_data.sequence

    for pdbid in uniprot_data.pdbid:
        mfta["pdbids"] = {
                          pdbid: {
                                "TM_domain" : rcsb_data.TMdomain,
                                "HP_domain" : rcsb_data.HPdomain,
                                "Stalk"     : rcsb_data.stalk,
                                "head"      : rcsb_data.head
                          }
        }                          
                          
        
        
        
    
     