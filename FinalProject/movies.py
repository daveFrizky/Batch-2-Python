from flask import make_response, abort
from config import db
from models import Movies, MoviesSchema, Directors


def read_all():
    """
    This function responds to a request for /api/movies
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    people = Movies.query.order_by(db.desc(Movies.id)).limit(10)

    # Serialize the data for the response
    person_schema = MoviesSchema(many=True)
    data = person_schema.dump(people)
    return data


def read_one(director_id, movie_id):
    """
    This function responds to a request for
    /api/people/{director_id}/notes/{movie_id}
    with one matching note for the associated person
    :param person_id:       Id of person the note is related to
    :param note_id:         Id of the note
    :return:                json string of note contents
    """
    # Query the database for the note
    note = (Movies.query.join(Directors, Directors.id == Movies.director_id).filter(
        Directors.id == director_id).filter(
            Movies.id == movie_id).one_or_none())

    # Was a note found?
    if note is not None:
        note_schema = MoviesSchema()
        data = note_schema.dump(note)
        return data

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Note not found for Id: {movie_id}")


def create(director_id, movie):
    """
    This function creates a new note related to the passed in person id.
    :param person_id:       Id of the person the note is related to
    :param note:            The JSON containing the note data
    :return:                201 on success
    """
    # get the parent person
    person = Directors.query.filter(Directors.id == director_id).one_or_none()

    # Was a person found?
    if person is None:
        abort(404, f"Person not found for Id: {director_id}")

    # Create a note schema instance
    schema = MoviesSchema()
    new_note = schema.load(movie, session=db.session)

    # Add the note to the person and database
    person.movie.append(new_note)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_note)

    return data, 201


def update(director_id, movie_id, movie):
    """
    This function updates an existing note related to the passed in
    person id.
    :param person_id:       Id of the person the note is related to
    :param note_id:         Id of the note to update
    :param content:            The JSON containing the note data
    :return:                200 on success
    """
    update_note = (Movies.query.filter(Movies.director_id == director_id).filter(
        Movies.id == movie_id).one_or_none())

    # Did we find an existing note?
    if update_note is not None:

        # turn the passed in note into a db object
        schema = MoviesSchema()
        update = schema.load(movie, session=db.session)

        # Set the id's to the note we want to update
        update.director_id = update_note.director_id
        update.id = update_note.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated note in the response
        data = schema.dump(update_note)

        return data, 200

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Note not found for Id: {movie_id}")


def delete(director_id, movie_id):
    """
    This function deletes a note from the note structure
    :param person_id:   Id of the person the note is related to
    :param note_id:     Id of the note to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the note requested
    # note = (Note.query.filter(Person.person_id == person_id).filter(
    #     Note.note_id == note_id).one_or_none())

    note = (Movies.query.filter(Movies.director_id == director_id).filter(
        Movies.id == movie_id).one_or_none())

    # did we find a note?
    if note is not None:
        db.session.delete(note)
        db.session.commit()
        return make_response("Movie with Id = {movie_id} deleted".format(movie_id=movie_id),
                             200)

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Note not found for Id: {movie_id}")

def top10_Popular():
    """
    This function responds to a request for /api/movies
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    people = Movies.query.order_by(db.desc(Movies.popularity)).limit(10)

    # Serialize the data for the response
    person_schema = MoviesSchema(many=True)
    data = person_schema.dump(people)
    return data

