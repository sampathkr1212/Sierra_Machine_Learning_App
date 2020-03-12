from flask import render_template, url_for, flash, redirect, request, Blueprint, current_app, send_from_directory
import os
import pandas as pd
from sierramlapp.mlapp.forms import PricePrediction
from sierramlapp.mlapp.utils import save_file, printHttpError, saveBlobToFile, processResults, uploadFileToBlob, invokeBatchExecutionService

mlapp = Blueprint('mlapp', __name__)

@mlapp.route('/mlhome',methods=['GET','POST'])
def mlhome():
    form = PricePrediction()
    if form.validate_on_submit():
        if form.excel.data:
            #global excel_filename
            #excel_filename = form.excel.data.filename
            filename = form.excel.data.filename
            df = pd.read_csv(form.excel.data)
            save_file(form.excel.data)
            global excel_df
            excel_df = df
            dict = df.to_dict(orient='records')
            return render_template('mlhome.html',title='Price Prediction', form=form, dict=dict, len=len, col_names= df.columns, filename=filename)
    return render_template('mlhome.html', title='Price Prediction', form=form)

@mlapp.route('/predict/<filename>', methods=['GET','POST'])
def predict(filename):
    form = PricePrediction()
    print('filename..', filename)
    form.excel.data = os.path.join(current_app.root_path, 'static/data_files/', filename)
    result_download_link = invokeBatchExecutionService(filename)
    df = pd.read_csv(form.excel.data)
    dict = df.to_dict(orient='records')
    return render_template('mlhome.html', title='Price Prediction', form=form, dict=dict, len=len, col_names= df.columns,
                            result_download_link=result_download_link, filename=filename)
