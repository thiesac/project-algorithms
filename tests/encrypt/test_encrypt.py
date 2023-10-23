import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # "If the key is odd, it divides the message at the key index,"
    # "reverses the characters of each part, "
    # 'and returns the concatenation of the parts with "_" between them'

    message = "aabbcc"
    long_message = "tenta colocar uma frase"

    assert encrypt_message(message, 3) == "baa_ccb"
    assert encrypt_message(message, 0) == "ccbbaa"
    assert encrypt_message(message, 2) == "ccbb_aa"
    assert encrypt_message(message, 7) == "ccbbaa"
    assert encrypt_message(message, 20) == "ccbbaa"
    assert encrypt_message(long_message, 3) == "net_esarf amu racoloc at"
    assert encrypt_message(long_message, 2) == "esarf amu racoloc atn_et"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, 1.5)

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 3)
