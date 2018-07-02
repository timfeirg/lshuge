#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging

import click
import delegator


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
VERBOSITY_MAP = {0: logging.WARNING, 1: logging.DEBUG, 2: logging.DEBUG, 3: logging.DEBUG}
logger = logging.getLogger('lshuge')


def ncdu(path):
    command = 'ncdu {} -o -'.format(path)
    logger.debug('Running command: %s', command)
    command_result = delegator.run(command)
    if command_result.return_code:
        raise Exception(command_result.err)
    logger.debug('Command output: %s', command_result.out)
    return json.loads(command_result.out)


def get_huge_files(path, percentage):
    report = ncdu(path)
    __import__('pdb').set_trace()
    huge_files = ['I dont know yet']
    return huge_files


def parse_verbosity(ctx, param, verbosity):
    log_level = VERBOSITY_MAP.get(verbosity)
    if not log_level:
        raise ValueError('invalid verbosity, choose from 1~3, got {}'.format(verbosity))
    return log_level


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--type', '-t', 'type_', default='file', help='choose file or directory, or use f / d for short')
@click.option('--verbose', '-v', 'log_level', count=True, callback=parse_verbosity)
@click.option('--percentage', '-p', type=float, default=0.3, help='list files / directories that takes up to a certain percentage of the cwd size')
@click.argument('path', required=False, default='.')
def main(type_, log_level, percentage, path):
    logging.basicConfig(level=log_level, format='[%(asctime)s] [%(process)d] [%(levelname)s] [%(filename)s @ %(lineno)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S %z')
    logger.debug('Looking for huge files larger than %s of the total size in %s, type %s, log_level %s', percentage, path, type_, log_level)
    huge_files = get_huge_files(path, percentage)
    print('huge files are: {}'.format(huge_files))


if __name__ == '__main__':
    main()
