# Libs
## Short description.

Very simple library system
to list and add books to database.
Search is performed in title, author name and in publication language.
Filter is done by publication year.

## How to run?

### Prerequisites
1. You have to have installed [docker](https://www.docker.com/)
   and [docker-compose](https://docs.docker.com/compose/install/) on your computer.

### Starting
1. Rename **.env-default** file to **.env**.
2. Type command `docker-compose up --build` in terminal in project root directory.
3. Open browser with url `http://0.0.0.0:8000` or `http://127.0.0.1:8000` on Windows.
4. Enjoy!

## How to use?
1. You can store your books using `Add book` in the main menu.
2. You can search and import books from Google Books API using `Import books` in the main menu.
3. You can filter and search your stored books (looking for an author, title, language and publication year)

## API description.
You can check documentation for API [here](https://libs-books.herokuapp.com/v1/swagger/).

## Tests (coverage)
<dl>
    <table class="index">
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th class="name left headerSortDown shortkey_n">Module</th>
                <th class="shortkey_s">statements</th>
                <th class="shortkey_m">missing</th>
                <th class="shortkey_x">excluded</th>
                <th class="right shortkey_c">coverage</th>
            </tr>
        </thead>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>132</td>
                <td>41</td>
                <td>0</td>
                <td class="right" data-ratio="355 398">88%</td>
            </tr>
        </tfoot>
        <tbody>
            <tr class="file">
                <td class="name left"><a href="api_serializers_py.html">api/serializers.py</a></td>
                <td>7</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="7 7">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="api_views_py.html">api/views.py</a></td>
                <td>10</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="10 10">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="books_models_py.html">books/models.py</a></td>
                <td>23</td>
                <td>1</td>
                <td>0</td>
                <td class="right" data-ratio="22 23">96%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="books_views_py.html">books/views.py</a></td>
                <td>92</td>
                <td>40</td>
                <td>0</td>
                <td class="right" data-ratio="52 92">57%</td>
            </tr>
        </tbody>
    </table>
</dl>

## Licence
```text
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <phk@FreeBSD.ORG> wrote this file.  As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return.  Poul-Henning Kamp
 * ----------------------------------------------------------------------------
 ```