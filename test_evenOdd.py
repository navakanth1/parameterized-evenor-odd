import pytest
import evenodd


@pytest.mark.parametrize("a,b",[(5, False),(6, True),(8, True), (3, False), (5, False), (12, True), (50, True), (47, False)])
def test_evenorOdd(a,b):
    res = evenodd.check(a)
    assert res == b