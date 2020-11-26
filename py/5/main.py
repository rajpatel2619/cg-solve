# Import the pysqlite library
import sqlite3
import math

# The separator of our CSV files
SEP = ','

def create_table_region(db, f):
    con = sqlite3.connect(db)
    cur = con.cursor()
    # drop the table if it already exists; re-create it.
    cur.execute('DROP TABLE IF EXISTS StatelessCountByRegion')
    # create two variables for storing Region and Population
    cur.execute('CREATE TABLE StatelessCountByRegion '
                '(Region TEXT, Population INTEGER)')
    for line in f:
        content = line.strip().split(SEP)
        sql = ''' INSERT INTO StatelessCountByRegion(Region,Population)
              VALUES(?,?) '''
        params = (content[0],content[1])
        cur.execute(sql,params)
        print(cur.lastrowid)


    con.commit()

# f = open("t.txt")
# create_table_region("taskp",f)




    # don't forget to close the cursor, commit the changes and close the
    # connection

def create_table_country(db, f):
    """Creates and populates the table StatelessCountByCountry
    from file StatelessCountByCountry.csv

    Args:
        db: the filename of a SQLite database to connect to
        f: a freshly opened file in the format of StatelessCountByCountry.csv

    Returns:
        None
    """
    # connect to the database and create a cursor

    # drop the table if it already exists; re-create it

    # Populate the StatelessCountByRegion Table
    # Loop through each line in the file:
    # for line in f:
        # Write the body of this loop yourself. Handle the whitespace around
        # each line, split each line on SEP, and insert the relevant values
        # into the table.
    # Hint: line.strip().split(SEP) will return you a list.

    # don't forget to close the cursor, commit the changes and close
    # the connection


def print_tables(db):
    """Prints rows from tables StatelessCountByCountry and
    StatelessCountByRegion

    Args:
        db: the filename of a SQLite database to connect to

    Returns:
        None
    """
    # connect to the database and create a cursor

    # select all columns using SQL command
    # 'SELECT * FROM StatelessCountByCountry'

    # print the data from StatelessCountByCountry

    # select all columns using SQL command
    # 'SELECT * FROM StatelessCountByRegion'

    # print the data from StatelessCountByRegion


def run_query(db, query, args=None):
    """Returns the results of running the given query on database db

    Args:
        db: the filename of a SQLite database to connect to
        query: query to run on the database

    Returns:
        result of the query
        """
    # You don't have to do anything for this function! It's already written for
    # you. It's meant as a helper function to reduce the amount of copy-pasting
    # you'd have to do.
    con = sqlite3.connect(db)
    cur = con.cursor()
    if args is None:
        cur.execute(query)
    else:
        cur.execute(query, args)
    # Note that we're using cur.fetchall() here instead of a for loop because
    # we WANT a list of the values we've SELECTed.
    data = cur.fetchall()
    cur.close()
    con.close()
    return data


def get_total_stateless(db):
    """ Returns the total stateless count from database db

    Args:
        db: The filename of a sqlite database to connect to

    Returns:
        total count of stateless people
    """
    pass


def get_avg_stateless(db, region):
    """ Returns the average stateless count from database db in given region

    Args:
        db: The filename of a sqlite database to connect to
        region: The name of the region

Returns:
        average of stateless people in region
    """
    # Example of running a query using run_query
    # return(run_query(db, query, (region,)))


def get_less_than_avg_country(db, region):
    """ Returns countries with population less than average population
        in that region

    Args:
        db:The filename of a sqlite database to connect to
        region: name of region

    Returns:
        Countries with population less than average
    """
    # Hint: Use get_avg_stateless(db, region)[0][0] to get average population
    # in given region. get_avg_stateless(db, region)[0][0] converts tuple into
    # a number that can be used for comparisons
    pass


def get_country_percentage(db, percent):
    """ Returns countries with at least percent population of total population

    Args:
        db:The filename of a sqlite database to connect to
        percent: percentage of population

    Return:
        Countries with percent population of total population
    """
    # Hint: Use get_total_stateless(db)[0][0] to get the total population
    # total_population = get_total_stateless(db)[0][0]
    # percent = (percent / 100)
    pass


def get_country_lessthan_percent(db, percent):
    """ Returns records from the table StatelessCountByCountry
    such that countries do not have percent population of total population

    Args:
        db:The filename of a sqlite database to connect to
        percent: percentage of population

    Return:
        Records excluding percent population of total population
    """
    # Hint: Find out countries that do contain percent population of total
    # population.
    # then exclude those countries using nested query.
    # refer to the example showed in class for nested query
    # Nested Query
    pass


def get_countries_percent_of_region(db, region, percent):
    """ Returns countries with population more than percent population
    for that region

    Args:
        db:The filename of a sqlite database to connect to
        percent: percentage of population

    Return:
        countries with population more than percent population for that region
    """
    # Hint: Use INNER JOIN to join both the tables StatelessCountByCountry
    # and StatelessCountByRegion.
    # Select rows in WHERE based on three conditions:
    # 1: Region should be selected based on argument
    # 2: Both the tables should have same region
    # 3: Population of region should be compared with population from country
    # to check whether it meets criteria
    pass