from apps.shield.detector import contains_or, detector_dfa

def test_detector_or():
    assert contains_or("aor") is True
    assert contains_or("ora") is True
    assert contains_or("aoa") is False
    assert contains_or("") is False
    assert contains_or("oar") is False

# test_detector_or()

seen = detector_dfa()._reachable()
completed = detector_dfa()._completed()

# print(f"seen {seen}")
# print(f"completed {completed}")
print(f"accepted:{detector_dfa().stateAlphabet('B')}")