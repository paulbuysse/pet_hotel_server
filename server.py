
import psycopg2
import psycopg2.extras

from flask import Flask, request, make_response, jsonify

con = psycopg2.connect(
                host="localhost", 
                database="pet_hotel",
                user="Paul",
                password="postgres",
                cursor_factory=psycopg2.extras.RealDictCursor
)

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/owners', methods=['GET', 'POST'])

def ownerRoute():
    if (request.method == 'GET'):
        try:
            cur = con.cursor()
            queryText = """SELECT "owners".name, "owners".id, COUNT("pets".owner_id) FROM "pets"
            JOIN "owners" ON "pets".owner_id = "owners".id
            GROUP BY "owners".name, "owners".id;"""
            cur.execute(queryText)
            records = cur.fetchall()
            cur.close()
            return jsonify(records), 201
        except Exception as e:
            return (str(e))

    elif (request.method == 'POST'):
        data = request.json
        cur = con.cursor()
        queryInsertText = "insert into owners (name) values (%s);"
        cur.execute(queryInsertText, (data["name"], ))
        con.commit()
        cur.close()
        return jsonify(data), 201


@app.route('/pets', methods=['GET','POST'])
def getPost():
    if (request.method == 'POST'):
        cur = con.cursor()
        data = request.json
        print(data)
        queryText = """INSERT INTO "pets" ("owner_id", "pet_name", "breed", "color") VALUES (%s, %s, %s, %s);"""
        cur.execute(queryText, (data['owner_id'], data['pet_name'], data['breed'], data['color'] ,))
        con.commit()
        cur.close()
        return f"posted {(data['pet_name'])}", 201
    elif (request.method == 'GET'):
        cur = con.cursor()
        cur.execute("""SELECT * FROM "pets" JOIN "owners" ON "owners".id = "pets".owner_id;""")
        records = cur.fetchall()
        print(records)
        cur.close()
        return jsonify(records), 201


def putDelete(id):
    if (request.method == 'PUT'):
        cur = con.cursor()
        data = request.json
        queryText = """UPDATE "pets" SET "checked_in" = %s WHERE id = %s; """
        cur.execute(queryText, data['checked_in'], request.args)

        # inOrOut = request.form[“check”]
        # if (inOrOut == ‘in’):
          
        #     queryText = ‘UPDATE “pet” SET “checked_in” = TRUE WHERE id = %s;’
        #     cur.execute(queryText, (id))
        #     conn.commit()
        #     cur.close()
        #     return “checked in!“, 200
        # elif (inOrOut == ‘out’):
          
        #     queryText = ‘UPDATE “pet” SET “checked_in” = FALSE WHERE id = %s;’
        #     cur.execute(queryText, (id))
        #     conn.commit()
        #     cur.close()
        #     return “checked out!“, 200
       
#     elif (request.method == ‘DELETE’):
#         cur = conn.cursor()
#         petId = id
#         queryText = (f’DELETE FROM “pet” WHERE id = {petId} RETURNING “pet”.pet_name;’)
#         cur.execute(queryText)
#         petName = cur.fetchall()
#         petName = petName[0]
#         print(“printing our thing”)
#         print(petName[‘pet_name’])
#         # conn.commit()
#         cur.close()
#         return jsonify(petName), 200

# if making put or delete req.params == request.args.get("name", "")