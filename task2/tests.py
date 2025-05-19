import unittest
from unittest.mock import patch, Mock

from solution import scrape


HTML_PAGE_1 = '''
<div class="mw-category mw-category-columns">
  <div class="mw-category-group">
    <h3>А</h3>
    <ul>
      <li><a href="/wiki/Аист">Аист</a></li>
      <li><a href="/wiki/Акула">Акула</a></li>
    </ul>
  </div>
  <div class="mw-category-group">
    <h3>Б</h3>
    <ul>
      <li><a href="/wiki/Бегемот">Бегемот</a></li>
    </ul>
  </div>
</div>
<div id="mw-pages">
  <a href="/wiki/Категория:Животные_по_алфавиту?pagefrom=Б">Предыдущая страница</a>
  <a href="/wiki/Категория:Животные_по_алфавиту?pagefrom=В">Следующая страница</a>
</div>
'''

HTML_PAGE_2 = '''
<div class="mw-category mw-category-columns">
  <div class="mw-category-group">
    <h3>В</h3>
    <ul>
      <li><a href="/wiki/Волк">Волк</a></li>
      <li><a href="/wiki/Ворон">Ворон</a></li>
      <li><a href="/wiki/Выдра">Выдра</a></li>
    </ul>
  </div>
</div>
<div id="mw-pages">
  <a href="/wiki/Категория:Животные_по_алфавиту?pagefrom=В">Предыдущая страница</a>
  <!-- Нет следующей страницы -->
</div>
'''


class MyTestCase(unittest.TestCase):

    @patch('requests.get')
    def test_scrape(self, mock_get):
        mock_1 = Mock()
        mock_1.content = HTML_PAGE_1.encode('utf-8')

        mock_2 = Mock()
        mock_2.content = HTML_PAGE_2.encode('utf-8')

        mock_get.side_effect = [mock_1, mock_2]

        result = scrape()

        expected = {'А': 2, 'Б': 1, 'В': 3}

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
