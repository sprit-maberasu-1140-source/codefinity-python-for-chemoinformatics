from rdkit import Chem
from rdkit.Chem import Descriptors
from sklearn.linear_model import LinearRegression
import numpy as np

def compute_descriptors(smiles_list):
    descriptors = []
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:
            mw = Descriptors.MolWt(mol)
            logp = Descriptors.MolLogP(mol)
            hbd = Descriptors.NumHDonors(mol)
            hba = Descriptors.NumHAcceptors(mol)
            descriptors.append([mw, logp, hbd, hba])
        else:
            descriptors.append([np.nan, np.nan, np.nan, np.nan])
    return np.array(descriptors)

def build_qsar_model(smiles, properties):
    X = compute_descriptors(smiles)

    mask = ~np.isnan(X).any(axis=1)
    X_clean = X[mask]
    y_clean = np.array(properties)[mask]
    model = LinearRegression()
    model.fit(X_clean,y_clean)
    return model

smiles_list = ["CCO", "CC(=O)O", "c1ccccc1", "CCN", "CCCC"]
property_values = [0.5, 1.2, 2.3, 0.7, 1.0]

model = build_qsar_model(smiles_list, property_values)
coefficients = model.coef_
intercept = model.intercept_

print(coefficients)
print(intercept)
