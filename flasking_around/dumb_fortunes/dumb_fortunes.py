from flask import (Blueprint, g, request, session, url_for, render_template)

from ..db import get_db 

dumb_fortunes_bp = Blueprint('dumb_fortunes_bp', __name__)

@dumb_fortunes_bp.route('/dumb-fortunes', methods=['GET', 'POST'])
def get_dumb_fortunes():
    if request.method == 'POST':    
        fortune = get_db().execute(
            'SELECT fortunes FROM fortunes ORDER BY RANDOM() LIMIT 1'
        ).fetchone()

        return render_template('dumb_fortunes.html', fortune=fortune)
    
    return render_template('dumb_fortunes.html')


