from flask import Flask
from app import connex_app 
import unittest
import json
import requests


class TestMovies(unittest.TestCase):
    url = 'http://127.0.0.1:5000/api/movies'

    def test_getAll (self):
        r = requests.get(TestMovies.url)
        self.assertEqual(r.status_code, 200)

    def test_top10Popular (self):
        r = requests.get(TestMovies.url+'/top_10_popular')
        self.assertEqual(r.status_code, 200)

        
