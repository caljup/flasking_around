from flask import (Blueprint, render_template)


chili_dogs_bp = Blueprint('chili_dogs_bp', __name__)

@chili_dogs_bp.route('/this-is-a-painting-of-chili-dogs', methods=['GET'])
def chili_dogs_painting():
    return render_template('chili_dogs_painting.html')