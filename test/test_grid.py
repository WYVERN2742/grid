from ..grid import Grid
import pytest


@pytest.mark.parametrize("gWidth, gHeight", [
	(2, 2),
	(4, 4),
	(200, 200),
	(1, 3),
	(30, 1),
])
def test_grid_size(gWidth,gHeight):
	grid = Grid(gWidth, gHeight)
	assert grid.width() == gWidth
	assert grid.height() == gHeight
