from click.testing import CliRunner

from client.cli import get_news_items, rand_list


# TODO: Use MagicMock/Patch or one of the requests auto mocking libraries
# for the remote calls.
# TODO: Test that your code knows how to catch exceptions properly,

def test_get_news():
    runner = CliRunner()
    result = runner.invoke(get_news_items,
                           input=rand_list[2])
    assert result.exit_code == 0
    assert 'title' in result.output
