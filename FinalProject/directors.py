from flask import make_response, abort
from config import db
from models import Directors, DirectorsSchema


def read_all():
    """
    This function responds to a request for /api/directors
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    people = Directors.query.order_by(Directors.id).limit(5)

    # Serialize the data for the response
    person_schema = DirectorsSchema(many=True)
    data = person_schema.dump(people)
    return data


def read_one(id):
    """
    This function responds to a request for /api/directors/{id}
    with one matching person from people
    :param id:   Id of person to find
    :return:            person matching id
    """
    # Get the person requested
    person = Directors.query.filter(Directors.id == id).one_or_none()

    # Did we find a person?
    if person is not None:

        # Serialize the data for the response
        person_schema = DirectorsSchema()
        data = person_schema.dump(person)
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            "Person not found for Id: {id}".format(id=id),
        )


def create(directors):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    
    id = directors.get("id")

    existing_person = (
        Directors.query.filter(Directors.id == id)
        .filter(Directors.id == id)
        .one_or_none()
    )

    # Can we insert this person?
    if existing_person is None:

        # Create a person instance using the schema and the passed in person
        schema = DirectorsSchema()
        new_person = schema.load(directors, session=db.session)

        # Add the person to the database
        db.session.add(new_person)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(new_person)

        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(
            409,
            "Director with Id = {id} exists already",
        )


def update(id, directors):
    """
    This function updates an existing person in the people structure
    Throws an error if a person with the name we want to update to
    already exists in the database.
    :param id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    # Get the person requested from the db into session
    update_person = Directors.query.filter(
        Directors.id == id
    ).one_or_none()

    # Try to find an existing person with the same name as the update
    id = directors.get("id")

    existing_person = (
        Directors.query.filter(Directors.id == id)
        .filter(Directors.id == id)
        .one_or_none()
    )

    # Are we trying to find a person that does not exist?
    if update_person is None:
        abort(
            404,
            "Director not found for Id: {id}".format(id=id),
        )

    # Would our update create a duplicate of another person already existing?
    elif (
        existing_person is not None and existing_person.id != id
    ):
        abort(
            409,
            "Director with Id = {id} exists already",
        )

    # Otherwise go ahead and update!
    else:

        # turn the passed in person into a db object
        schema = DirectorsSchema()
        update = schema.load(directors, session=db.session)

        # Set the id to the person we want to update
        update.id = update_person.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_person)

        return data, 200


def delete(id):
    """
    This function deletes a person from the people structure
    :param id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    person = Directors.query.filter(Directors.id == id).one_or_none()

    # Did we find a person?
    if person is not None:
        db.session.delete(person)
        db.session.commit()
        return make_response(
            "Person {id} deleted".format(id=id), 200
        )

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            "Person not found for Id: {id}".format(id=id),
        )

def read_byGender(gender):
    """
    This function responds to a request for /api/directors/{gender}
    with one matching person from people
    :param id:   Id of person to find
    :return:            person matching id
    """
    # Get the person request
    people = Directors.query.filter(Directors.gender == gender)

    # Did we find a person?
    person_schema = DirectorsSchema(many=True)
    data = person_schema.dump(people)
    return data

