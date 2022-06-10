Requirements
============

* Python 3.10+ (might work with older versions too)
* [cryptography](https://pypi.org/project/cryptography/) 37.0.2+
* [ipfshttpclient](https://pypi.org/project/ipfshttpclient/) 0.8.0a2
* running [IPFS](https://ipfs.io/) daemon

Setup
=====

To set up in a self-contained, virtual environment, run the following:

    $ git clone https://github.com/dClimate/crypt_ipfs.git
    $ cd crypt_ipfs
    $ python -m venv .
    $ source bin/activate
    $ pip install -r requirements.txt
    
You must also download [IPFS](https://ipfs.io) and launch the daemon on your system

Running
=======

To encrypt a file containing "Hello, World!":

    $ ./crypt_ipfs.py --files hello.txt
    > Key for hello.txt is CBJswmJNCIBqMjfhuOrvAv-xN3WSKT-2gWg-lA62hMc= and IPFS hash is QmQ1ajwuR8uKpK9LcgsnrSYF2FtRtHhLhtMtdYwSBo3c8c

To print the file contents, use `--hash` and `--key`:

    $ ./crypt_ipfs.py --hash QmQ1ajwuR8uKpK9LcgsnrSYF2FtRtHhLhtMtdYwSBo3c8c --key CBJswmJNCIBqMjfhuOrvAv-xN3WSKT-2gWg-lA62hMc=
    > Hello, World!
    
If this hash is read from IPFS without the key and decryption code, encrypted data is printed:

    $ ipfs cat QmQ1ajwuR8uKpK9LcgsnrSYF2FtRtHhLhtMtdYwSBo3c8c
    > gAAAAABiook4_0fACGHcFMRGeZPW7JAh_2cRTdXhXJQJlgODS06BjLcaGXej5qiPn_EwVQLUA3yV2hkHeUiwpmuLe7BSM4LuMw==
