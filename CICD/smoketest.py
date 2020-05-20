#!/usr/bin/env python3

import requests
import timeit

from prettytable import PrettyTable

server_url = 'http://localhost:5000'


def perform_test(step_descr, text, endpoint, expected_ret_code, start_time):
    print(text)
    response = requests.get(endpoint)
    status_code = response.status_code
    print('RETURNED STATUS CODE: {}'.format(status_code))
    if status_code != expected_ret_code:
        return [step_descr, 'FAILED', timeit.default_timer() - start_time, endpoint]
    print('-'*120)


def test_fits_files():
    step_descr = 'fits-files'
    start_time = timeit.default_timer()

    perform_test(
        step_descr,
        'Step 1 - fits-files (LIST)',
        '{}/api/v1/fits-files'.format(server_url),
        200, start_time)

    perform_test(
        step_descr,
        'Step 2 - fits-files (GET)',
        '{}/api/v1/fits-files/{}'.format(server_url, 'a59d38bc2bfe0a71c54ce366233997b1'),
        200, start_time)

    perform_test(
        step_descr,
        'Step 3 - fits-files (GET - NOT FOUND)',
        '{}/api/v1/fits-files/{}'.format(server_url, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        404, start_time)

    print('fits-files OK')
    print('-'*120)

    return [step_descr,
            'SUCCESS',
            timeit.default_timer() - start_time,
            '{}/api/v1/fits-files'.format(server_url)]


def print_execution_header():
    print('='*120)
    print('  AstroImages API SMOKE TEST '.center(120, ' '))
    print('='*120)


def print_summary_header():
    print('='*120)
    print('  SMOKE TEST - EXECUTION SUMMARY  '.center(120, ' '))
    print('='*120)


def print_summary_footer():
    print('APPLICATION: AstroImages API')
    print('RELEASE: 1.0')
    print('ENVIRONMENT: GITHUB')
    print('\n\n')


def main():

    print_execution_header()

    table = PrettyTable()
    table.field_names = ['TEST CASE NAME', 'STATUS', 'EXECUTION TIME', 'ENDPOINT']
    table.add_row(test_fits_files())

    print(table)

    print_summary_header()
    print_summary_footer()

    return 0


if __name__ == '__main__':
    exit(main())
