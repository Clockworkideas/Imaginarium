import argparse
import base64
import os
from pathlib import Path
from io import BytesIO
import time
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
