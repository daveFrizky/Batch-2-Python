from flask import Flask
from app import connex_app 
import unittest
import json
import requests


class TestDirector(unittest.TestCase):
    url = 'http://h8ocbc2-milestone1-001.herokuapp.com/api/directors'
    director = {"department": "Dept",
                    "gender": 1,
                        "id": 1,
                      "name": "David",
                       "uid": 1
               }
    directorUpdate = {"department": "Dept",
                          "gender": 1,
                              "id": 1,
                            "name": "nama David ",
                             "uid": 1
                     }


    def test_getAll (self):
        r = requests.get(TestDirector.url)
        self.assertEqual(r.status_code, 200)
    
    def test_getOne (self):
        r = requests.get(TestDirector.url+'/1')
        self.assertEqual(r.status_code, 200)

    def test_getByGender (self):
        r = requests.get(TestDirector.url+'ByGender/1')
        self.assertEqual(r.status_code, 200)

    def test_insert (self):
        r = requests.post(TestDirector.url, json=TestDirector.director)
        self.assertEqual(r.status_code, 201)

    def test_update (self):
        r = requests.put(TestDirector.url+'/1', json=TestDirector.directorUpdate)
        self.assertEqual(r.status_code, 200)
        
    def test_delete (self):
        r = requests.delete(TestDirector.url+'/1')
        self.assertEqual(r.status_code, 200)
