#!/usr/bin/env python3

import cryptography.fernet, argparse, pathlib, ipfshttpclient

def encrypt(files, ipfs_client):
    for path in files:
        key = cryptography.fernet.Fernet.generate_key()
        encrypter = cryptography.fernet.Fernet(key)
        with path.open() as unencrypted:
            token = encrypter.encrypt(unencrypted.read().encode())
            ipfs_hash = ipfs_client.add_bytes(token)
            print(f"Key for {path} is {key.decode()} and IPFS hash is {ipfs_hash}")

def decrypt(ipfs_hash, key, ipfs_client):
    token = ipfs_client.cat(ipfs_hash)
    decrypter = cryptography.fernet.Fernet(key.encode())
    print(decrypter.decrypt(token).decode("utf-8"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", type=pathlib.Path)
    parser.add_argument("--hash")
    parser.add_argument("--key")
    arguments = parser.parse_args()
    if arguments.files or (arguments.hash and arguments.key):
        client = ipfshttpclient.connect()
        if arguments.files:
            encrypt(arguments.files, client)
        else:
            decrypt(arguments.hash, arguments.key, client)
    else:
        argparse.print_help()
