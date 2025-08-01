# test_app.py 
 
import pytest 
 
from app import app as dash_app 
 
# Test 1: The header is present. 
def test_header_is_present(): 
    """ 
    Verifies that the main header with the text 'Pink Morsel Sales Visualizer' is present 
    by inspecting the app's layout object. 
    """ 
    assert any( 
        getattr(component, 'children', None) == 'Pink Morsel Sales Visualizer' 
        for component in dash_app.layout.children 
    ) 
 
# Test 2: The visualisation is present. 
def test_visualisation_is_present(): 
    """ 
    Verifies that the dcc.Graph component with the ID 'sales-graph' is present 
    in the app's layout. 
    """ 
    assert any( 
        getattr(component, 'id', None) == 'sales-graph' 
        for component in dash_app.layout.children 
    ) 
 
# Test 3: The region picker is present. 
def test_region_picker_is_present(): 
    """ 
    Verifies that the dcc.RadioItems component with the ID 'region-radio' is present 
    in the app's layout. 
    """ 
    assert any( 
        getattr(component, 'id', None) == 'region-radio' 
        for component in dash_app.layout.children)