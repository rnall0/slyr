#!/usr/bin/env python
"""
Registers all known objects with the registry singleton
"""

from slyr.parser.object_registry import REGISTRY

from slyr.parser.objects.line_template import LineTemplate
from slyr.parser.objects.colors import (
    CMYKColor,
    RgbColor,
    HSVColor,
    HSLColor,
    GrayColor
)
from slyr.parser.objects.decoration import (
    LineDecoration,
    SimpleLineDecoration)
from slyr.parser.objects.line_symbol_layer import (
    SimpleLineSymbolLayer,
    CartographicLineSymbolLayer,
    MarkerLineSymbolLayer
)
from slyr.parser.objects.fill_symbol_layer import (
    SimpleFillSymbolLayer
)
from slyr.parser.objects.marker_symbol_layer import (
    ArrowMarkerSymbolLayer,
    CharacterMarkerSymbolLayer,
    SimpleMarkerSymbolLayer
)
from slyr.parser.objects.font import Font
from slyr.parser.symbol_parser import (
    FillSymbol,
    LineSymbol,
    MarkerSymbol
)


def initialize_registry():
    """
    Registers all known objects with the registry singleton
    """

    REGISTRY.register(LineTemplate)
    REGISTRY.register(CMYKColor)
    REGISTRY.register(RgbColor)
    REGISTRY.register(HSVColor)
    REGISTRY.register(HSLColor)
    REGISTRY.register(GrayColor)
    REGISTRY.register(LineDecoration)
    REGISTRY.register(SimpleLineDecoration)
    REGISTRY.register(SimpleLineSymbolLayer)
    REGISTRY.register(CartographicLineSymbolLayer)
    REGISTRY.register(MarkerLineSymbolLayer)
    REGISTRY.register(SimpleFillSymbolLayer)
    REGISTRY.register(ArrowMarkerSymbolLayer)
    REGISTRY.register(CharacterMarkerSymbolLayer)
    REGISTRY.register(SimpleMarkerSymbolLayer)
    REGISTRY.register(Font)
    REGISTRY.register(FillSymbol)
    REGISTRY.register(LineSymbol)
    REGISTRY.register(MarkerSymbol)
