from unittest.mock import Mock, patch

from my_package import get_url


@patch('requests.get')
def test_get_url(mock_get):
    expected_value = 'content'
    mock_get.return_value = Mock(text=expected_value)
    assert get_url(url='https://google.com') == expected_value

