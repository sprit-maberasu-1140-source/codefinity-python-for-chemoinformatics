from rdkit import Chem
from rdkit.Chem import Descriptors, Crippen

def compute_descriptors(smiles_list):
    result = {}
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:
            mw = Descriptors.MolWt(mol)
            logp = Crippen.MolLogP(mol)
            result[smi] = {'molecular_weight': mw, 'logP': logp}
        else:
            result[smi] = None
    return result

# Sample calls
smiles_list = ["CCO", "c1ccccc1", "CC(=O)O", "invalid"]
descriptors = compute_descriptors(smiles_list)
print(descriptors)