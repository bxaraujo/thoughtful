from robot_arm import sort
import pytest

def test_bulky_by_volume():
    """Package is bulky due to volume >= 1,000,000."""
    assert sort(100, 100, 100, 10) == "SPECIAL"

def test_bulky_by_max_dimension():
    """Package is bulky due to max dimension >= 150."""
    assert sort(151, 10, 10, 10) == "SPECIAL"

def test_not_bulky():
    """Package is not bulky."""
    assert sort(10, 10, 10, 10) == "STANDARD"

def test_heavy():
    """Package is heavy (mass >= 20)."""
    assert sort(10, 10, 10, 20) == "SPECIAL"

def test_not_heavy():
    """Package is not heavy."""
    assert sort(10, 10, 10, 19) == "STANDARD"

def test_rejected_bulky_and_heavy():
    """Package is rejected (bulky + heavy)."""
    assert sort(100, 100, 100, 20) == "REJECTED"

def test_rejected_bulky_dim_and_heavy():
    """Package is rejected (bulky by dimension + heavy)."""
    assert sort(151, 10, 10, 20) == "REJECTED"

#Edge cases
def test_zero_mass():
    """Package has mass = 0."""
    assert sort(100, 100, 100, 0) == "SPECIAL" 

def test_zero_dimensions():
    """Package has zero dimensions (not bulky)."""
    assert sort(0, 0, 0, 20) == "SPECIAL"
