import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

def filter_druglike_smiles(smiles_list):
    """
    Given a list of SMILES strings, return a list of those that pass Lipinski's Rule of Five.
    Each returned SMILES must correspond to a valid molecule that:
      - Has molecular weight <= 500
      - Has logP <= 5
      - Has hydrogen bond donors <= 5
      - Has hydrogen bond acceptors <= 10
    Ignore any SMILES that cannot be parsed by RDKit.
    """
    # Your code here
    filtered = []
    for smi in smiles_list:
        mol=Chem.MolFromSmiles(smi)
        if mol is None:
            continue
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        h_donors = Descriptors.NumHDonors(mol)
        h_acceptors = Descriptors.NumHAcceptors(mol)
        if(
          mw <= 500 and 
          logp <= 5 and
          h_donors <= 5 and
          h_acceptors <= 10
        ):
            filtered.append(smi)
    return filtered
    

# Example usage
test_smiles = [
    "CC(=O)OC1=CC=CC=C1C(=O)O",  # Aspirin
    "CCN(CC)CCCC(C)NC1=C2C=CC(=CC2=NC=C1)Cl",  # Chlorpromazine
    "C1=CC=CC=C1",  # Benzene
    "CC1(C)SCC(N1C(=O)NC2=CC=CC=C2)C(=O)O",  # Amoxicillin
]
filtered = filter_druglike_smiles(test_smiles)
print(filtered)