"""Game fix for Metro 2033"""

from protonfixes import util


def main() -> None:
    """Installs d3dx11_42"""
    # Fixes D3D10 and D3D11 render path crash on launch.
    util.protontricks('d3dx11_42')
    util.protontricks('d3dcompiler_42')
