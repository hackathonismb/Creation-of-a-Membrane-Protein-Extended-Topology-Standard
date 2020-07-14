# iMPETuS: A Membrane Protein Extended Topology Standard

## What are membrane proteins?
Membrane proteins (MPs) make up about one-third of the human genome, and are targets of 50% of drugs. MPs are functionally diverse, necessary for signal transduction, transport, adhesion, and many other cellular responses. Therefore, understanding MP structure is critically important for understanding biological processes and treatment of disease.

## What's the problem?
Membrane proteins are difficult to study despite their ubiquity: hydrophobic regions embedded in the membrane can be difficult to examine using conventional methods, and sequence annotation is often limited beyond whether or not a portion of the protein is inserted into the membrane or not. There is a critical need for an accessible and informative representation of membrane protein topology in structural bioinformatics workflows.

## What is iMPETuS?
iMPETuS is an extended topology format for membrane protein structural annotation implemented in JSON. It combines primary amino acid sequences with structural information to extend data typically found in PDB files to allow for informative comparisons between proteins with related membrane topologies. Notably, iMPETuS
is built to cover complex cases such as proteins with "stalk" regions - transmembrane domains with long protrusions not embedded into the membrane - and to directly compare one or more the sequences of two or more protein domains.

## iMPETuS Features
* Annotation of complex structural domains, including transmembrane and stalk regions of membrane proteins
* Comparison of conserved domains between proteins
* iMPETuS files can be combined with other features such as iCn3D sequence conservation and interaction analysis
* Extensible, flat-file format

## Workflow / Usage
1. User provides a UniProt accession number or PDB ID
2. An iMPETuS file is generated based on available topological information
3. Output file can be used in downstream workflows (e.g. iCn3D analysis).

More detailed instructions coming soon!

## To-Do
- [ ] Manually extract data for SARS-CoV-2 spike glycoprotein and human ACE2
- [ ] Parsers
- [ ] Database server options
- [ ] "Nice to have": Functional annotation

## The Team
* Azza Ahmed @azzaea
* Erik Serrano @axiomcura
* Jeff Zahratka @jzahratka
* Olaitan Awe @laitanawe
* Ravi Abrol @raviabrol
