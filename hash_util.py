import json
import hashlib as hl


def hash_string_256(string):
    """ Hashes a string with SHA256.

    Arguments:
        :string: The string that should be hashed.
    """
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """ Hashes a block and returns a string representation of it.

    Arguments:
        :block: The block that should be hashed.
    """
    hashable_block = block.__dict__.copy()
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
    # return "-".join([str(block[key]) for key in block])
