import requests
import click
from flask import jsonify


@click.command()
@click.argument('string')
@click.option('--md5', help='the md5 string')
def md5(string):
    host = '127.0.0.1'
    port = '5000'
    m = requests.get(f'http://{host}:{port}/md5/{string}')
    return jsonify(['m']) 

#group6cli md5 'test' 

if __name__ == '__main__':
    md5()


@click.command()
@click.argument('integer')
@click.option('--fibonacci', help='the fibonacci integer')
def fibonacci(integer):
    host = '127.0.0.1'
    port = '5000'
    m = requests.get(f'http://{host}:{port}/fibonacci/{integer}')
    return jsonify(['m'])

#this could return a fibonacci number 

if __name__ == '__main__':
    fibonacci()


@click.command()
@click.argument('integer')
@click.option('--isprime', help='the isprime integer')
def isprime(integer):
    host = '127.0.0.1'
    port = '5000'
    m = requests.get(f'http://{host}:{port}/isprime/{integer}')
    return jsonify (['m'])

#this could return a prime number or not 

if __name__ == '__main__':
    isprime()


@click.command()
@click.argument('integer')
@click.option('--factorial', help='the factorial integer')
def factorial(integer):
    host = '127.0.0.1'
    port = '5000'
    m = requests.get(f'http://{host}:{port}/factorial/{integer}')
    return jsonify(['m'])

#this could return a factorial integer 

if __name__ == '__main__':
    factorial()






