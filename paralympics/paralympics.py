from flask import current_app as app
from paralympics.schemas import RegionSchema, EventSchema
from paralympics import db
from paralympics.models import Region, Event


# Flask-Marshmallow Schemas
regions_schema = RegionSchema(many = True)
region_schema = RegionSchema()
events_schema = EventSchema(many = True)
event_schema = EventSchema()

@app.route('/')
def hello():
    return f"Hello!"

@app.get("/regions")
def get_regions():
    """Returns a list of NOC region codes and their details in JSON."""
    # Select all the regions using Flask-SQLAlchemy
    all_regions = db.session.execute(db.select(Region)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = regions_schema.dump(all_regions)
    # Return the data
    return result

@app.get("/events/<event_id>")
def get_id(event_id):
    """ Returns the event with the given id JSON.

    :param event_id: The id of the event to return
    :param type event_id: int
    :returns: JSON
    """
    event = db.session.execute(
        db.select(Event).filter_by(id = event_id)).scalar_one_or_none()
    return events_schema.dump(event)

@app.get("/regions/<NOC_input>")
def NOC(NOC_input):
    """ Returns the region with the given NOC.

    :param NOC: The id of the event to return
    :param type NOC: str
    :returns: JSON
    """
    region = db.session.execute(
        db.select(Region).filter_by(NOC = NOC_input)
    ).scalar_one_or_none()
    return events_schema.dump(region)