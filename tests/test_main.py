import sys
import pytest

if __name__ == "__main__":
    sys.exit(
        int(
            pytest.main(
                ["tests"]
            )
        )
    )