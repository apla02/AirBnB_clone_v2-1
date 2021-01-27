#!/usr/bin/python3
"""new view for Place objects that handles all
default RestFul API actions
"""
from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City