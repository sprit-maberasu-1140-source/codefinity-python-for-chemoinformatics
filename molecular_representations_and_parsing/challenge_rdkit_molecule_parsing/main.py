from rdkit import Chem
from rdkit.Chem import Descriptors

def get_molecular_weights(smiles_list):
    # Write your code here
    pass
    weights = []
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:
            mw = Descriptors.MolWt(mol)
            weights.append(mw)
        else:
            weights.append(None)
    return weights
            
    

# Sample calls
smiles_list = ["CCO", "c1ccccc1", "O=C=O", "invalid"]
weights = get_molecular_weights(smiles_list)
print(weights)