import fb
import os
import time

a = fb.db.reference(f"/update").get()



while a == 0:
    a = fb.db.reference(f"/update").get()
    print(a)
    time.sleep(3)


b = fb.db.reference(f"/link").get()

print(b)