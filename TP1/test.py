import pytest
import fonctions as f

def test_1():
        assert f.puissance(2,3) == 8
        assert f.puissance(2,2) == 4

def test_2():
        assert f.puissance(2,4) ==16
        assert f.puissance(8,0) ==1

def test_3():
        assert f.puissance(-1,3) == -1
        assert f.puissance(-2,2) == 4
        assert f.puissance(0,1) == 0
