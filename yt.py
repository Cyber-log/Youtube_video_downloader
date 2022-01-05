# Developed by Al Jabir

import base64, codecs
magic = 'aW1wb3J0IG9zDQppbXBvcnQgcmFuZG9tDQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwDQppbXBvcnQgc2h1dGlsDQoNCnZlcnNpb24gPSAiMS41Ig0KDQpub24gPSAiXDAzM1swbSIgICMgTm8gY29sb3INCnJlZCA9ICJcMDMzWzA7MzFtIiAgIyBSZWQNCmdyZWVuID0gIlwwMzNbOTJtIiAgIyBncmVlbg0KeWVsbG93ID0gIlwwMzNbMDszM20iICAjIFllbGxvdw0KYmx1ZSA9ICJcMDMzWzA7MzRtIiAgIyBCbHVlDQp2aW8gPSAiXDAzM1swOzM1bSIgICMgUHVycGxlDQpjeWFuID0gIlwwMzNbMDszNm0iICAjIEN5YW4NCg0KcmVkMSA9ICJcMDMzWzE7OTFtIiAgIyBSZWQNCmdyZWVuMSA9ICJcMDMzWzE7OTJtIiAgIyBncmVlbg0KeWVsbG93MSA9ICJcMDMzWzE7OTNtIiAgIyBZZWxsb3cNCmJsdWUxID0gIlwwMzNbMTs5NG0iICAjIEJsdWUNCnZpbzEgPSAiXDAzM1sxOzk1bSIgICMgUHVycGxlDQpjeWFuMSA9ICJcMDMzWzE7OTZtIiAgIyBDeWFuDQoNCnRyeToNCiAgICBpbXBvcnQgeW91dHViZV9kbA0KZXhjZXB0IEltcG9ydEVycm9yOg0KICAgIG9zLnN5c3RlbSgncGlwIGluc3RhbGwgeW91dHViZV9kbCcpDQogICAgaW1wb3J0IHlvdXR1YmVfZGwNCg0KDQpkZWYgY2xyKCk6DQogICAgaWYgb3MubmFtZSA9PSAnbnQnOg0KICAgICAgICBvcy5zeXN0ZW0oJ2NscycpDQogICAgZWxzZToNCiAgICAgICAgb3Muc3lzdGVtKCdjbGVhcicpDQoNCg0KZGVmIGxnbygpOg0KICAgIGNvbG9ycyA9IFsnXDAzM1sxOzMxbScsICdcMDMzWzE7MzJtJywgJ1wwMzNbMTszM20nLCAnXDAzM1sxOzM0bScsICdcMDMzWzE7MzVtJywgJ1wwMzNbMTszNm0nXQ0KICAgIFcgPSAnXDAzM1swbScNCg0KICAgIGRlZiBjbHIoKToNCiAgICAgICAgaWYgb3MubmFtZSA9PSAnbnQnOg0KICAgICAgICAgICAgb3Muc3lzdGVtKCdjbHMnKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgb3Muc3lzdGVtKCdjbGVhcicpDQoNCiAgICBkZWYgbG9nbygpOg0KICAgICAgICBjbHIoKQ0KICAgICAgICBzbGVlcCgxKQ0KICAgICAgICBsZyA9ICIiIlwwMzNbMTszNG0NCiAgICAgICAgICAgICAgLjg4ODg4ODg4OC4gICAgICAgICAgICAgICA4ODggICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgIDAwMDAgICAgMDAwMCAgICAgICAgICAgICAgMDAwICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgIDg4OCAgICAgIDg4OCAgICAgICAgICAgICAgODg4DQogICAgICAgICAgICAgIDg4OCAgICAgICAgICAgUjg4ODg4ODhSICAgODg4ICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICAwMDAgICAgICAgICAgIFI4ODg4ODg4UiAgIDAwMCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgODg4ICAgICAwMDAgICAgICAgICAgICAgICA4ODggICAgICAgICAgODggIA0KICAgICAgICAgICAgICAwMDAwICAgMDAwMCAgICAgICAgICAgICAgIDAwMDAgICAgICAgIDAwMCAgICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgICIwMDAwMDAwMDAiICAgICAgICAgICAgICAgODg4ODg4'
love = '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'
god = 'MDAwMCAgICAgICAgICAgICAgIDAwMDAgICAgICAgIDAwMCAgICAgICAgICAgICAgICAgICAgDQogICIwMDAwMDAwMDAiICAgICAgICAgICAgICAgODg4ODg4ODg4ODg4ODggICAgIA0KDQogICAgICBcMDMzWzE7MzRtICAgICAgICBEZXZlbG9wZWQgQnkgOlwwMzNbMTszNG0gQWwgSmFiaXIgICAiIiINCiAgICBwcmludChyYW5kb20uY2hvaWNlKGNvbG9ycykgKyBsb2dvICsgVykNCiAgICBwcmludChjeWFuMSArICItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSIpDQogICAgcHJpbnQoeWVsbG93ICsgIiAgICAgICAgICAgICAgICAgVmVyc2lvbiA6ICIgKyByZWQxICsgdmVyc2lvbikNCiAgICBwcmludChjeWFuMSArICItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSIpDQoNCg0KZGVmIGNyZWF0ZV9mb2xkZXIocGF0aCk6DQogICAgdHJ5Og0KICAgICAgICBpZiBub3Qgb3MucGF0aC5leGlzdHMocGF0aCk6DQogICAgICAgICAgICBvcy5tYWtlZGlycyhwYXRoKQ0KICAgICAgICAgICAgcmV0dXJuICJzdWNjZXNzIg0KICAgIGV4Y2VwdCBPU0Vycm9yOg0KICAgICAgICByZXR1cm4gImZhaWxlZCINCiAgICAgICAgcGFzcw0KDQoNCmRlZiBkb3duKHVybCwgZm9ybWF0KToNCiAgICBvcHMgPSB7DQogICAgICAgICdmb3JtYXQnOiBmb3JtYXQsDQogICAgICAgICdvdXR0bXBsJzogJy9zZGNhcmQvJSh0aXRsZSlzLSUoaWQpcy4lKGV4dClzJywNCiAgICAgICAgJ25vcGxheWxpc3QnOiBUcnVlLA0KICAgICAgICAjICAgICAncHJvZ3Jlc3NfaG9va3MnOiBbbXlfaG9va10sDQogICAgfQ0KICAgIHRyeToNCiAgICAgICAgYSA9IHlvdXR1YmVfZGwuWW91dHViZURMKG9wcykuZG93bmxvYWQoW3VybF0pDQogICAgICAgIHByaW50KGdyZWVuMSArICJcbkRvbmUhXG5WaWRlbyBvciBhdWRpbyBzYXZlZCBpbiBwaG9uZSBzdG9yYWdlIHZpZGVvcyIpDQogICAgZXhjZXB0IDoNCiAgICAgICAgcHJpbnQoIk1heWJlIHJlcXVzdGVkIHBpeGVsIGlzIG5vdCBhdmFpbGFiZSBmb3IgdGhpcyB2aWRlbyBvciBtYXliZSB0aGlzIHZpZGVvIGlzIHByaXZhdGUiKQ0KICAgICAgICBzbGVlcCgyKQ0KICAgICAgICBjbHIoKQ0KDQoNCmRlZiB5dHZpZGVvX2F1ZGlvKHVybCk6DQogICAgcHJpbnQoIjEuIDE0NHAgKDNncClcbjIuIDI0MHAgKDNncClcbjMuIDI0MHAgKGZsdilcbjQuIDM2MHAgKHdlYm0pXG41LiAzNjBwIChtcDQpXG42LiA3MjBwIChtcDQpIikNCiAgICBwaXhlbCA9IHN0cihpbnB1dChncmVlbiArICJFbnRlciBwaXhlbCA6ICIpKQ0KICAgIGlmIHBpeGVsID09ICIxIjoNCiAgICAgICAgZm9ybWF0ID0gIjE3Ig0KICAgICAgICBkb3duKHVybCwgZm9ybWF0KQ0KICAgIGlmIHBpeGVsID09ICIyIjoNCiAgICAgICAgZm9ybWF0ID0gIjM2Ig0KICAgICAgICBkb3duKHVybCwgZm9ybWF0KQ0KICAgIGlmIHBpeGVsID09ICIzIjoNCiAgICAgICAgZm9ybWF0ID0gIjUiDQogICAgICAgIGRvd24odXJsLCBmb3JtYXQpDQogICAgaWYgcGl4ZWwgPT0gIjQiOg0KICAgICAgICBmb3JtYXQgPSAi'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))