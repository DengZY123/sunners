# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g
from common.lib.Helper import ops_render

route_index = Blueprint( 'index_page',__name__ )

@route_index.route("/")
def index():
    return "hello world"