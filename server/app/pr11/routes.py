from flask import render_template, send_file


from . import pr11
from .models import get_news_date_range
from .forms import DataRangeFormatForm
from ..utils.file_creation import get_file


@pr11.route('/', methods=['POST', 'GET'])
def index():
    form = DataRangeFormatForm()
    if form.validate_on_submit():
        file_format = form.file_format.data
        start_date = form.start_date.data
        end_date = form.end_date.data
        mem_file = get_file(get_news_date_range(start_date, end_date), file_format)
        return send_file(
            mem_file,
            as_attachment=True,
            download_name=f'{start_date}_{end_date}.{file_format}',
            mimetype=f'text/{file_format}')
    return render_template('pr11/index.html', form=form)
