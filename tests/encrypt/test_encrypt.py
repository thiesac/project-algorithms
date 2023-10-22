from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    "If the key is odd, it divides the message at the key index,"
    "reverses the characters of each part, "
    'and returns the concatenation of the parts with "_" between them'
    assert encrypt_message("aabbcc", 3) == "baa_ccb"
