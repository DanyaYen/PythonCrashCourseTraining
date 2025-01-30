from city_functions import city_country

def test_city_country():
    """Test that city_country function works correctly."""
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'