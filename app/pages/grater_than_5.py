from flask import render_template
from app.api.get_earthquake_grater_than_5 import get_earthquake_grater_than_5

from app.api.get_fault_line import get_fault_line
from app.api.get_magnitude_map import get_magnitude_map


def grater_than_5_page():
    df = get_earthquake_grater_than_5()
    fault_line = get_fault_line()
    _magnitude_map = get_magnitude_map(df=df, fault_line=fault_line)
    return render_template('grater_than_5.html', magnitude_map=_magnitude_map)