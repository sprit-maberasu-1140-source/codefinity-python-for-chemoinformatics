def count_atoms_in_smiles(smiles):
    two_letter_atoms = [
        "Cl", "Br", "Si", "Na", "Al", "Ca", "Li", "Mg", "Zn", "Fe", "Cu", "Ag", "Sn", "Pb"
    ]
    bond_and_ring_chars = "-=#:()/\\"
    count = 0
    i = 0
    while i < len(smiles):
        char = smiles[i]
        # Skip ring closure digits and bond symbols
        if char.isdigit() or char in bond_and_ring_chars:
            i += 1
            continue
        # Check for two-letter atom symbols first
        if i + 1 < len(smiles) and smiles[i:i+2] in two_letter_atoms:
            count += 1
            i += 2
            continue
        # Check for single-letter atom symbol (alphabetic character)
        if char.isalpha():
            count += 1
            i += 1
            continue
        i += 1
    return count

# Sample calls
print(count_atoms_in_smiles("CCO"))
print(count_atoms_in_smiles("C1=CC=CC=C1"))
print(count_atoms_in_smiles("ClCBr"))
print(count_atoms_in_smiles("CC(=O)O"))
