import psycopg2
import os
base_path = os.path.dirname(os.path.realpath(__file__))
try:
    from .databases import DBCONFIG
except Exception:
    # ionixx1
    DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': 'portal_backend',
                             'HOST': 'localhost', 'PORT': 5432, 'USER': 'muthukumar', 'PASSWORD': 'muthukumar'}}
else:
    DATABASES = DBCONFIG


# DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': 'dummy',
#                              'HOST': 'localhost', 'PORT': 5432, 'USER': 'muthukumar', 'PASSWORD': 'muthukumar'}}
#

# db connection
try:
    database = DATABASES["default"]["NAME"]
    user = DATABASES["default"]["USER"]
    password = DATABASES["default"]["PASSWORD"]
    host = DATABASES["default"]["HOST"]
    port = DATABASES["default"]["PORT"]

    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cur = conn.cursor()
    print("connnected successully")


    # delete if already exists
    cur.execute("TRUNCATE TABLE company CASCADE;")
    cur.execute("TRUNCATE TABLE defaultaccounttagmapping CASCADE;")
    cur.execute("TRUNCATE TABLE financialstatementtag CASCADE;")
    cur.execute("TRUNCATE TABLE questioncategory CASCADE;")
    cur.execute("TRUNCATE TABLE question CASCADE;")

    conn.commit()


    # comment bellow two lines If required
    cur.execute("ALTER TABLE question ALTER COLUMN answer_data_type TYPE varchar(20);")
    cur.execute("ALTER TABLE question ALTER COLUMN short_tag TYPE varchar(50);")

    conn.commit()

    print("\nDeleted Successfully")

    print("Processing ............")



    # Inserting data

    # Company
    cur.execute(
        """copy company(id,name,external_id,default_currency,website,employee_count,accounting_type,auth_key,secret_key,is_tag_error_notified) from '%s/SELECT_t___FROM_public_company_t.csv' delimiter ',' CSV HEADER;
        """ % base_path)
    conn.commit()


    # default account tag mapping
    cur.execute(
        """copy defaultaccounttagmapping from '%s/SELECT_t___FROM_public_defaultaccounttag.csv' delimiter ',' CSV HEADER;""" % base_path)
    conn.commit()

    # default account tag mapping
    cur.execute(
        """copy defaultaccounttagmapping from '%s/Sage-DefaultTagMaps.csv' delimiter ',' CSV HEADER;""" % base_path)
    conn.commit()


    # financial statement tag
    cur.execute(
        """copy financialstatementtag (id,tag_id,short_label,description,tag_category,abstract,formula,
            name,sort_order,is_total_row,all_sight_name,tag_group
            ) from '%s/SELECT_t___FROM_public_financialstatemen.csv' delimiter ',' CSV HEADER;""" % base_path)
    conn.commit()

    # question category
    cur.execute(
        """copy questioncategory from '%s/SELECT_t___FROM_public_questioncategory_.csv' delimiter ',' CSV HEADER;
        """ % base_path)
    conn.commit()

    # question
    cur.execute(
        """copy question from '%s/SELECT_t___FROM_public_question_t.csv' delimiter ',' CSV HEADER;""" % base_path)
    conn.commit()

    print("Inserted SuccessFully")
    # saving and closing connection
    conn.close()
    print("process End")



except Exception as e:
    print("Error occurs", e)



