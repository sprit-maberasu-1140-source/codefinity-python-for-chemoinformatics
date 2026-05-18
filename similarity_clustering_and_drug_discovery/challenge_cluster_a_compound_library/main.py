from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs

def cluster_by_similarity(smiles_list, threshold=0.6):
    mols = [Chem.MolFromSmiles(smi) for smi in smiles_list]
    fps = [AllChem.GetMorganFingerprintAsBitVect(m, 2) for m in mols]
    n = len(fps)
    clusters = []
    assigned = [False] * n

    for i in range(n):
        if not assigned[i]:
            cluster = [i]
            assigned[i] = True
            to_check = [i]
            while to_check:
                idx = to_check.pop()
                for j in range(n):
                    if not assigned[j]:
                        sim = DataStructs.TanimotoSimilarity(fps[idx], fps[j])
                        if sim > threshold:
                            cluster.append(j)
                            assigned[j] = True
                            to_check.append(j)
            clusters.append([smiles_list[k] for k in cluster])
    return clusters

# Example usage
smiles = [
    "CCO",          # ethanol
    "CCCO",         # propanol
    "CCCCO",        # butanol
    "c1ccccc1",     # benzene
    "c1ccncc1",     # pyridine
    "CCN",          # ethylamine
    "CCCN",         # propylamine
    "CC(C)O"        # isopropanol
]

clusters = cluster_by_similarity(smiles)
print(clusters)