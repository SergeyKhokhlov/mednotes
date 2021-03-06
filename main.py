# -*-coding: utf-8 -*-

from flask import Flask, render_template, redirect
from data import db_session, notes, addNoteForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MedNote$'


@app.route("/")
def index():
    session = db_session.create_session()
    all = session.query(notes.Note).all()
    all_names = []
    for i in all:
        all_names.append(i.name)
    return render_template("index.html", notes_list=all_names,
                           title="MedNotes | Медицинские Заметки",
                           description="MedNotes - сайт со статьями о медицине. "
                                       "Читайте о медицине у нас!")


@app.route("/note/<int:id_page>")
def page(id_page):
    session = db_session.create_session()
    note = session.query(notes.Note).filter(notes.Note.id == id_page).all()
    txt = note[0].text.split("\n")
    return render_template("page.html", name=note[0].name, text=txt,
                           title="MedNotes | " + note[0].name, description=txt)


@app.route("/addNote/<int:password>", methods=["GET", "POST"])
def addNote(password):
    if password == 7355608:
        form = addNoteForm.addNote()
        if form.validate_on_submit():
            session = db_session.create_session()
            note = notes.Note(name=form.title.data,
                              text=form.text.data)
            session.add(note)
            session.commit()
            return redirect("/")
        return render_template("addNote.html", form=form)
    else:
        return redirect("/")


def main():
    db_session.global_init("db/database.db")
    app.run()


if __name__ == '__main__':
    main()
