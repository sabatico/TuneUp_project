from threading import Thread

from factory.data_factory import DataFactory
from flask import Blueprint, jsonify, render_template, request

pages = Blueprint("pages", __name__, template_folder="templates", static_folder="static")


@pages.route("/", methods=["POST", "GET"])
def index():

    # catch the start button press action, initiate the data collection in NEW thread
    if request.args.get("collect") == "start":
        global data_collection
        data_collection = DataFactory()

        data_collection_thread = Thread(target=data_collection.collect_data_framework, name="data_collection_thread")
        data_collection_thread.start()

    return render_template("index.html")


@pages.route("/get_data_collection_progress", methods=["GET"])
def get_data_collection_progress():
    data = data_collection
    return jsonify(data.collection_progress)
