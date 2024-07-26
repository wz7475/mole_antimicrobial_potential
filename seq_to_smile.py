from rdkit import Chem

amino_acids = {'G', 'A', 'L', 'M', 'F', 'W', 'K', 'Q', 'E', 'S', 'P', 'V', 'I', 'C', 'Y', 'H', 'R', 'N', 'D', 'T'}
seq = 'PQITLWQRPIVTIKIGGQLIEALLDTGADDTVLEXXNLPGRWKPKXIGGIGGFXKVRQYDQVPIEIXGHKTXSTVLVGPTPVNIIGRNLMTQIGCTLNFPISPIETVPVKLKPGMDGPKXKQWPLTEEKIKALMEICKELEEEGKISKIGPENPYNTPVFAIKKKNSTKWRKLVDFRELNKRTQDFWEVQLGIPHPAGLKRKKSVTVLDVGDAYFSIPLDKDFRKYTAFTIPSINNETPGIRYQYNVLPQGWKGSPAIFQSSMTKILEPFRKQNPDIVIYQYVDDLYVGSDLEIEQHRTKIKELRQYLWKWGFYTPDXKHQEEPPFHWXGYELHPDKWTVQPIVLPEKESWTVNDIQKLVGKLNWASQIYAGIKVKQLCKLLRG'

edited_seq = ''
for aa in seq:
    if aa not in amino_acids:
        print('Non-standard/missing amino acid:', aa)
    else:
        edited_seq += aa

m1 = Chem.MolFromSequence(seq)
m2 = Chem.MolFromSequence(edited_seq)

print('Read seq successfully:', m1 is not None)
print('Read edited_seq successfully:', m2 is not None)
print(str(m2))

