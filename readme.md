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