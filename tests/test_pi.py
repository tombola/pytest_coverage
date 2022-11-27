import platform

import pytest

linuxonly = pytest.mark.skipif(
    platform.system() != "Linux", reason="requires linux system"
)


@linuxonly
@pytest.mark.pionly
@pytest.mark.serial
def test_pi_serial():
    """
    Select pi tests using `pytest -m pionly`

    Or exclude tests that will only work on the Pi with `pytest -m "not pionly"`
    """
    assert True
