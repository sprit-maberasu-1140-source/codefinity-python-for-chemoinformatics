from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs

def find_similar_molecules(reference_smiles, candidate_smiles_list):
    pass
    reference_mol = Chem.MolFromSmiles(reference_smiles)
    if reference_mol is None:
        raise ValueError
    reference_fp = AllChem.GetMorganFingerprintAsBitVect(reference_mol,radius=2)
    similar_smiles = []
    for smi in candidate_smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            continue
        fp = AllChem.GetMorganFingerprintAsBitVect(mol,radius=2)

        sim = DataStructs.TanimotoSimilarity(reference_fp,fp)

        if sim > 0.7:
            similar_smiles.append(smi)
    return similar_smiles
            
reference = "CCO"
candidates = ["CCC", "CCN", "CCCO", "CCCl", "CCO", "CCCCO"]
result = find_similar_molecules(reference, candidates)
print(result)
