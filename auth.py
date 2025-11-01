import hashlib
import os
from pathlib import Path
from mastersetup import first_time_setup

def hash_password(password: str, salt: bytes = None) -> tuple:

    if salt is None:
        # Generate a new random salt
        salt = os.urandom(16)

    # Hash the password with the salt using SHA-256
    password_hash = hashlib.sha256(salt + password.encode()).digest()
    #.encode converts the password string to bytes .digest() returns the binary hash value
    # returns the salt and the hashed password
    return salt.hex(), password_hash.hex()

def set_password(stored_salt: bytes, stored_hash:bytes, password: str) -> bool:
    # Hash the provided password with the stored salt
    _, password_hash = hash_password(password, stored_salt)

    # Compare the newly hashed password with the stored hash
    return password_hash == stored_hash

def master_password_authentication():
    masterpassfile = Path(__file__).parent / "masterpass.hash"
    
    if not masterpassfile.exists():
        masterpassword = first_time_setup()
        hashed_salt, hashed_password = hash_password(masterpassword)
        Path.write_text(masterpassfile, f"{hashed_salt}:{hashed_password}")

#    else: logic for entering master password that has already been set





