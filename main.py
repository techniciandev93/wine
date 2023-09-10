import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from services import get_correct_form_word, get_wine_records, year


def start_web_main(file_path):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        year=year,
        word=get_correct_form_word(year),
        records_wine=get_wine_records(file_path)
    )
    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Запустите скрипт, указав путь к excel файлу с товарами вина. "
                                                 "python main.py (путь к файлу, по умолчанию wine3.xlsx)")
    parser.add_argument("excel_path", help="Укажите путь к файлу", nargs='?', default='wine3.xlsx')
    args = parser.parse_args()

    start_web_main(args.excel_path)
